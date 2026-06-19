"""
Odis Creator Expert — Web App RAG su Streamlit.

Recupera contesto dalla documentazione Markdown indicizzata su Pinecone
e risponde tramite Google Gemini.
"""

from __future__ import annotations

import streamlit as st
from google import genai
from google.genai import types
from pinecone import Pinecone

from rag_config import LLM_MODEL, TOP_K, load_settings
from rag_embeddings import create_genai_client, embed_query

SYSTEM_PROMPT_TEMPLATE = """Sei "Odis Creator Expert", un assistente tecnico specializzato e un esperto senior del software proprietario Odis Creator. Il tuo unico obiettivo è supportare l'utente nella configurazione, risoluzione dei problemi e utilizzo del software, basandoti esclusivamente sulla documentazione ufficiale fornita.

Istruzioni operative tassative:
1. FONTE DELLE INFORMAZIONI: Rispondi alle domande dell'utente utilizzando REGOLE, PROCEDURE e DATI estratti unicamente dai file Markdown (.md) forniti nel tuo contesto. Non fare affidamento su conoscenze esterne o supposizioni generali su altri software simili.

2. TRATTAMENTO DELLE LACUNE (NO ALLUCINAZIONI): Se la risposta alla domanda dell'utente non è presente nei file .md forniti, o se le informazioni sono parziali, dichiara chiaramente e onestamente: "Mi dispiace, ma questa specifica informazione/procedura non è presente nella documentazione di Odis Creator a mia disposizione". Non inventare passaggi o parametri.

3. STILE DI RISPOSTA:
   - Sii estremamente preciso, tecnico, chiaro e orientato alla risoluzione del problema.
   - Rispondi sempre nella stessa lingua in cui ti viene posta la domanda (di default in Italiano).
   - Quando spieghi una procedura, usa elenchi puntati o numerati passo-passo per renderla facilmente eseguibile.
   - Se nel testo originale ci sono percorsi di menu (es. File > Impostazioni > Categoria), riportali esattamente così come sono scritti.

4. FORMATTAZIONE: Utilizza il grassetto per evidenziare i nomi di pulsanti, menu, codici di errore o parametri critici (es. Clicca su **Applica**). Se devi mostrare frammenti di codice o configurazioni, usa i blocchi di codice markdown.

Contesto disponibile:
{context}"""


def init_session_state() -> None:
    if "messages" not in st.session_state:
        st.session_state.messages = []


@st.cache_resource(show_spinner="Connessione ai servizi in corso...")
def get_clients():
    settings = load_settings()
    genai_client = create_genai_client(settings.google_api_key)
    pinecone_client = Pinecone(api_key=settings.pinecone_api_key)
    index = pinecone_client.Index(settings.pinecone_index_name)
    return settings, genai_client, index


def retrieve_context(index, genai_client, question: str) -> tuple[str, list[dict[str, str]]]:
    query_vector = embed_query(genai_client, question)
    results = index.query(
        vector=query_vector,
        top_k=TOP_K,
        include_metadata=True,
    )

    context_blocks: list[str] = []
    sources: list[dict[str, str]] = []

    for rank, match in enumerate(results.matches or [], start=1):
        metadata = match.metadata or {}
        text = str(metadata.get("text", "")).strip()
        source = str(metadata.get("source", "sconosciuto")).strip()
        score = float(match.score or 0.0)

        if not text:
            continue

        context_blocks.append(f"[Frammento {rank} | Fonte: {source}]\n{text}")
        sources.append(
            {
                "source": source,
                "score": f"{score:.3f}",
                "preview": text[:220] + ("..." if len(text) > 220 else ""),
            }
        )

    return "\n\n---\n\n".join(context_blocks), sources


def build_gemini_history(messages: list[dict[str, str]]) -> list[types.Content]:
    history: list[types.Content] = []
    for message in messages[:-1]:
        role = "user" if message["role"] == "user" else "model"
        history.append(
            types.Content(
                role=role,
                parts=[types.Part(text=message["content"])],
            )
        )
    return history


def generate_answer(
    genai_client: genai.Client,
    question: str,
    context: str,
    history: list[types.Content],
) -> str:
    system_prompt = SYSTEM_PROMPT_TEMPLATE.format(context=context or "Nessun frammento rilevante recuperato.")

    chat = genai_client.chats.create(
        model=LLM_MODEL,
        config=types.GenerateContentConfig(
            system_instruction=system_prompt,
            temperature=0.2,
        ),
        history=history,
    )

    response = chat.send_message(question)
    answer = response.text
    if not answer:
        raise RuntimeError("Gemini non ha restituito una risposta testuale.")
    return answer.strip()


def render_sidebar(index) -> None:
    with st.sidebar:
        st.header("Odis Creator Expert")
        st.markdown(
            "Assistente RAG basato sulla documentazione ufficiale Odis Creator, "
            "con recupero semantico da Pinecone e generazione tramite Gemini."
        )

        try:
            stats = index.describe_index_stats()
            total_vectors = stats.total_vector_count or 0
            st.metric("Chunk indicizzati", total_vectors)
        except Exception as exc:
            st.warning(f"Impossibile leggere le statistiche Pinecone: {exc}")

        if st.button("Nuova conversazione", use_container_width=True):
            st.session_state.messages = []
            st.rerun()


def main() -> None:
    st.set_page_config(
        page_title="Odis Creator Expert",
        page_icon="🛠️",
        layout="wide",
    )

    init_session_state()

    try:
        settings, genai_client, index = get_clients()
    except Exception as exc:
        st.error(
            "Configurazione incompleta. Verifica le chiavi in Streamlit Secrets o nel file `.streamlit/secrets.toml`."
        )
        st.exception(exc)
        st.stop()

    render_sidebar(index)

    st.title("Odis Creator Expert")
    st.caption("Chatbot RAG per la documentazione tecnica di Odis Creator")

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
            if message["role"] == "assistant" and message.get("sources"):
                with st.expander("Fonti utilizzate"):
                    for source in message["sources"]:
                        st.markdown(
                            f"- **{source['source']}** (rilevanza: {source['score']})\n\n"
                            f"  {source['preview']}"
                        )

    prompt = st.chat_input("Scrivi la tua domanda su Odis Creator...")

    if prompt:
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            with st.spinner("Sto consultando la documentazione..."):
                try:
                    context, sources = retrieve_context(index, genai_client, prompt)
                    history = build_gemini_history(st.session_state.messages)
                    answer = generate_answer(
                        genai_client=genai_client,
                        question=prompt,
                        context=context,
                        history=history,
                    )
                except Exception as exc:
                    st.error("Si è verificato un errore durante la generazione della risposta.")
                    st.exception(exc)
                    st.stop()

                st.markdown(answer)

                if sources:
                    with st.expander("Fonti utilizzate"):
                        for source in sources:
                            st.markdown(
                                f"- **{source['source']}** (rilevanza: {source['score']})\n\n"
                                f"  {source['preview']}"
                            )

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer,
                "sources": sources,
            }
        )


if __name__ == "__main__":
    main()
