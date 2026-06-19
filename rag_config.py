"""Configurazione condivisa tra ingest.py e app.py."""

from __future__ import annotations

import os
from dataclasses import dataclass

EMBEDDING_MODEL = "text-embedding-004"
EMBEDDING_DIMENSION = 768
LLM_MODEL = "gemini-2.5-flash"
CHUNK_SIZE = 1200
CHUNK_OVERLAP = 200
TOP_K = 3
DEFAULT_INDEX_NAME = "odis-creator-rag"
DEFAULT_GITHUB_REPO = "riccardo0326/html-files-odis"
DEFAULT_GITHUB_BRANCH = "main"
DEFAULT_MD_PATH = "md"
EMBED_BATCH_SIZE = 32
UPSERT_BATCH_SIZE = 100


@dataclass(frozen=True)
class RAGSettings:
    google_api_key: str
    pinecone_api_key: str
    pinecone_index_name: str
    github_repo: str
    github_branch: str
    md_source_path: str


def _get_secret(key: str, default: str = "") -> str:
    try:
        import streamlit as st

        if key in st.secrets:
            return str(st.secrets[key])
    except Exception:
        pass
    return os.getenv(key, default)


def load_settings() -> RAGSettings:
    google_api_key = _get_secret("GOOGLE_API_KEY")
    pinecone_api_key = _get_secret("PINECONE_API_KEY")

    if not google_api_key:
        raise ValueError("GOOGLE_API_KEY non configurata.")
    if not pinecone_api_key:
        raise ValueError("PINECONE_API_KEY non configurata.")

    return RAGSettings(
        google_api_key=google_api_key,
        pinecone_api_key=pinecone_api_key,
        pinecone_index_name=_get_secret("PINECONE_INDEX_NAME", DEFAULT_INDEX_NAME),
        github_repo=_get_secret("GITHUB_REPO", DEFAULT_GITHUB_REPO),
        github_branch=_get_secret("GITHUB_BRANCH", DEFAULT_GITHUB_BRANCH),
        md_source_path=_get_secret("MD_SOURCE_PATH", DEFAULT_MD_PATH),
    )


def load_settings_from_env() -> RAGSettings:
    """Carica le impostazioni solo da variabili d'ambiente (per ingest.py locale)."""
    google_api_key = os.getenv("GOOGLE_API_KEY", "")
    pinecone_api_key = os.getenv("PINECONE_API_KEY", "")

    if not google_api_key:
        raise ValueError("GOOGLE_API_KEY non configurata nelle variabili d'ambiente.")
    if not pinecone_api_key:
        raise ValueError("PINECONE_API_KEY non configurata nelle variabili d'ambiente.")

    return RAGSettings(
        google_api_key=google_api_key,
        pinecone_api_key=pinecone_api_key,
        pinecone_index_name=os.getenv("PINECONE_INDEX_NAME", DEFAULT_INDEX_NAME),
        github_repo=os.getenv("GITHUB_REPO", DEFAULT_GITHUB_REPO),
        github_branch=os.getenv("GITHUB_BRANCH", DEFAULT_GITHUB_BRANCH),
        md_source_path=os.getenv("MD_SOURCE_PATH", DEFAULT_MD_PATH),
    )
