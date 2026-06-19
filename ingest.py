#!/usr/bin/env python3
"""
Script di indicizzazione per Odis Creator RAG.

Carica i file Markdown dalla repository GitHub (o dalla cartella locale),
genera embedding con Google Gemini text-embedding-004 e li carica su Pinecone.
"""

from __future__ import annotations

import argparse
import hashlib
import logging
import os
import sys
import time
from pathlib import Path

import requests
from dotenv import load_dotenv
from langchain_text_splitters import MarkdownTextSplitter
from pinecone import Pinecone, ServerlessSpec
from tqdm import tqdm

from rag_config import (
    CHUNK_OVERLAP,
    CHUNK_SIZE,
    DEFAULT_GITHUB_BRANCH,
    DEFAULT_GITHUB_REPO,
    DEFAULT_INDEX_NAME,
    DEFAULT_MD_PATH,
    EMBED_BATCH_SIZE,
    EMBEDDING_DIMENSION,
    UPSERT_BATCH_SIZE,
    load_settings_from_env,
)
from rag_embeddings import create_genai_client, embed_texts

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)
logger = logging.getLogger(__name__)


def load_markdown_from_local(md_path: str) -> dict[str, str]:
    base_path = Path(md_path)
    if not base_path.exists():
        raise FileNotFoundError(f"Cartella Markdown non trovata: {base_path.resolve()}")

    documents: dict[str, str] = {}
    for file_path in sorted(base_path.rglob("*.md")):
        relative_source = str(file_path.relative_to(base_path)).replace("\\", "/")
        documents[relative_source] = file_path.read_text(encoding="utf-8")

    if not documents:
        raise ValueError(f"Nessun file .md trovato in {base_path.resolve()}")

    logger.info("Caricati %d file Markdown dalla cartella locale '%s'.", len(documents), md_path)
    return documents


def load_markdown_from_github(repo: str, branch: str, md_path: str) -> dict[str, str]:
    api_url = f"https://api.github.com/repos/{repo}/git/trees/{branch}?recursive=1"
    response = requests.get(
        api_url,
        headers={"Accept": "application/vnd.github+json"},
        timeout=60,
    )
    response.raise_for_status()
    tree = response.json().get("tree", [])

    md_prefix = f"{md_path.strip('/')}/"
    md_files = [
        item["path"]
        for item in tree
        if item.get("type") == "blob"
        and item.get("path", "").startswith(md_prefix)
        and item.get("path", "").endswith(".md")
    ]

    if not md_files:
        raise ValueError(
            f"Nessun file .md trovato in '{md_path}' per la repository {repo}@{branch}."
        )

    documents: dict[str, str] = {}
    for file_path in tqdm(md_files, desc="Download Markdown da GitHub"):
        raw_url = f"https://raw.githubusercontent.com/{repo}/{branch}/{file_path}"
        file_response = requests.get(raw_url, timeout=60)
        file_response.raise_for_status()
        relative_source = file_path[len(md_prefix) :] if file_path.startswith(md_prefix) else file_path
        documents[relative_source] = file_response.text

    logger.info("Scaricati %d file Markdown da GitHub (%s).", len(documents), repo)
    return documents


def split_documents(documents: dict[str, str]) -> list[dict[str, str]]:
    splitter = MarkdownTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
    )

    chunks: list[dict[str, str]] = []
    for source, content in documents.items():
        for index, chunk_text in enumerate(splitter.split_text(content)):
            normalized_text = chunk_text.strip()
            if not normalized_text:
                continue
            chunks.append(
                {
                    "id": build_chunk_id(source, index, normalized_text),
                    "text": normalized_text,
                    "source": source,
                }
            )

    if not chunks:
        raise ValueError("Nessun chunk generato dai file Markdown.")

    logger.info("Generati %d chunk da %d documenti.", len(chunks), len(documents))
    return chunks


def build_chunk_id(source: str, chunk_index: int, text: str) -> str:
    digest = hashlib.sha256(f"{source}:{chunk_index}:{text[:120]}".encode("utf-8")).hexdigest()
    return digest[:32]


def ensure_pinecone_index(pc: Pinecone, index_name: str, recreate: bool) -> None:
    existing_indexes = set(pc.list_indexes().names())

    if index_name in existing_indexes:
        if recreate:
            logger.warning("Eliminazione indice esistente '%s'...", index_name)
            pc.delete_index(index_name)
            time.sleep(5)
        else:
            logger.info("Indice Pinecone '%s' già esistente.", index_name)
            return

    logger.info("Creazione indice Pinecone '%s' (dimension=%d)...", index_name, EMBEDDING_DIMENSION)
    pc.create_index(
        name=index_name,
        dimension=EMBEDDING_DIMENSION,
        metric="cosine",
        spec=ServerlessSpec(cloud="aws", region="us-east-1"),
    )

    while True:
        description = pc.describe_index(index_name)
        if description.status.ready:
            break
        logger.info("Attesa disponibilità indice Pinecone...")
        time.sleep(2)

    logger.info("Indice Pinecone '%s' pronto.", index_name)


def upsert_chunks(
    index,
    chunks: list[dict[str, str]],
    genai_client,
) -> None:
    vectors: list[tuple[str, list[float], dict[str, str]]] = []

    for start in tqdm(range(0, len(chunks), EMBED_BATCH_SIZE), desc="Generazione embedding"):
        batch = chunks[start : start + EMBED_BATCH_SIZE]
        embeddings = embed_texts(
            genai_client,
            [item["text"] for item in batch],
            task_type="RETRIEVAL_DOCUMENT",
        )

        for item, embedding in zip(batch, embeddings, strict=True):
            vectors.append(
                (
                    item["id"],
                    embedding,
                    {
                        "text": item["text"],
                        "source": item["source"],
                    },
                )
            )

    logger.info("Caricamento di %d vettori su Pinecone...", len(vectors))
    for start in tqdm(range(0, len(vectors), UPSERT_BATCH_SIZE), desc="Upsert su Pinecone"):
        batch = vectors[start : start + UPSERT_BATCH_SIZE]
        index.upsert(vectors=batch)

    stats = index.describe_index_stats()
    logger.info("Indicizzazione completata. Totale vettori nell'indice: %s", stats.total_vector_count)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Indicizza la documentazione Odis Creator su Pinecone.")
    parser.add_argument(
        "--source",
        choices=("local", "github"),
        default=os.getenv("INGEST_SOURCE", "local"),
        help="Origine dei file Markdown: cartella locale o repository GitHub.",
    )
    parser.add_argument(
        "--recreate-index",
        action="store_true",
        help="Elimina e ricrea l'indice Pinecone prima del caricamento.",
    )
    return parser.parse_args()


def main() -> int:
    load_dotenv()
    args = parse_args()

    try:
        settings = load_settings_from_env()
    except ValueError as exc:
        logger.error("%s", exc)
        return 1

    if args.source == "local":
        documents = load_markdown_from_local(settings.md_source_path)
    else:
        documents = load_markdown_from_github(
            repo=settings.github_repo,
            branch=settings.github_branch,
            md_path=settings.md_source_path,
        )

    chunks = split_documents(documents)

    genai_client = create_genai_client(settings.google_api_key)
    pc = Pinecone(api_key=settings.pinecone_api_key)

    ensure_pinecone_index(
        pc=pc,
        index_name=settings.pinecone_index_name,
        recreate=args.recreate_index,
    )

    index = pc.Index(settings.pinecone_index_name)
    upsert_chunks(index=index, chunks=chunks, genai_client=genai_client)

    logger.info("Operazione completata con successo.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
