"""Funzioni condivise per embedding Gemini."""

from __future__ import annotations

from google import genai
from google.genai import types

from rag_config import EMBEDDING_DIMENSION, EMBEDDING_MODEL


def create_genai_client(api_key: str) -> genai.Client:
    return genai.Client(api_key=api_key)


def embed_texts(
    client: genai.Client,
    texts: list[str],
    task_type: str,
) -> list[list[float]]:
    if not texts:
        return []

    response = client.models.embed_content(
        model=EMBEDDING_MODEL,
        contents=texts,
        config=types.EmbedContentConfig(
            output_dimensionality=EMBEDDING_DIMENSION,
            task_type=task_type,
        ),
    )

    embeddings: list[list[float]] = []
    for embedding in response.embeddings:
        values = embedding.values
        if values is None:
            raise RuntimeError("Embedding Gemini restituito senza valori.")
        embeddings.append(list(values))

    if len(embeddings) != len(texts):
        raise RuntimeError(
            f"Numero di embedding ({len(embeddings)}) diverso dal numero di testi ({len(texts)})."
        )

    return embeddings


def embed_query(client: genai.Client, query: str) -> list[float]:
    return embed_texts(client, [query], task_type="RETRIEVAL_QUERY")[0]
