# Odis Creator RAG — Guida completa al setup

Web App RAG (Retrieval-Augmented Generation) per interrogare la documentazione Markdown di **Odis Creator** tramite chatbot Streamlit, con vettori su **Pinecone** (piano gratuito) e LLM **Google Gemini**.

---

## Architettura

```text
Repository GitHub (cartella md/)
        │
        ▼
   ingest.py  ──►  Google text-embedding-004 (768 dim)
        │
        ▼
   Pinecone Index (cosine, serverless us-east-1)
        │
        ▼
   app.py (Streamlit) ──►  Top-K=3 retrieval + gemini-2.5-flash
```

---

## Prerequisiti

- Account **Google AI Studio** (API Key gratuita)
- Account **Pinecone** (piano Starter/Free)
- Account **GitHub** (per il deploy su Streamlit Community Cloud)
- Python **3.10+** installato in locale (per test e indicizzazione)

---

## 1. Ottenere la API Key di Google AI Studio (Gemini)

1. Apri [Google AI Studio](https://aistudio.google.com/).
2. Accedi con il tuo account Google.
3. Vai su **Get API key** (o **API Keys** nel menu).
4. Clicca **Create API key**.
5. Seleziona un progetto Google Cloud esistente oppure creane uno nuovo.
6. Copia la chiave generata (formato tipo `AIza...`) e conservala in un posto sicuro.

La chiave gratuita consente l’uso di:

- **Embedding**: `text-embedding-004` (768 dimensioni)
- **LLM chat**: `gemini-2.5-flash`

---

## 2. Configurare Pinecone (piano gratuito)

### 2.1 Creare l’account

1. Vai su [https://www.pinecone.io/](https://www.pinecone.io/) e registrati.
2. Conferma l’email e accedi alla console.

### 2.2 Recuperare la API Key

1. Nella console Pinecone, apri **API Keys**.
2. Copia la chiave (formato `pcsk_...`).

### 2.3 Creare l’indice vettoriale

Sul piano **Starter (free)** gli indici serverless sono disponibili **solo nella regione AWS `us-east-1`**.

Puoi creare l’indice in due modi:

#### Opzione A — Automatica (consigliata)

Esegui `ingest.py` (vedi sezione 3). Lo script crea l’indice se non esiste, con questi parametri:

| Parametro   | Valore              |
|------------|---------------------|
| Nome       | `odis-creator-rag`  |
| Tipo       | Dense               |
| Dimensione | **768**             |
| Metrica    | **cosine**          |
| Cloud      | **aws**             |
| Regione    | **us-east-1**       |

#### Opzione B — Manuale dalla console Pinecone

1. Clicca **Create index**.
2. Imposta:
   - **Name**: `odis-creator-rag`
   - **Dimensions**: `768`
   - **Metric**: `cosine`
   - **Cloud**: `AWS`
   - **Region**: `us-east-1`
3. Conferma la creazione.

### 2.4 Metadati dei vettori

Ogni chunk caricato da `ingest.py` include:

| Campo    | Descrizione                                      |
|----------|--------------------------------------------------|
| `text`   | Testo originale del frammento Markdown           |
| `source` | Percorso relativo del file `.md` di provenienza |

---

## 3. Test locale sul PC

### 3.1 Clonare la repository

```bash
git clone https://github.com/riccardo0326/html-files-odis.git
cd html-files-odis
```

### 3.2 Creare l’ambiente virtuale

```bash
python3 -m venv .venv
source .venv/bin/activate        # Linux/macOS
# .venv\Scripts\activate         # Windows
pip install -r requirements.txt
```

### 3.3 Configurare le variabili d’ambiente

Copia il file di esempio e inserisci le tue chiavi:

```bash
cp .env.example .env
```

Modifica `.env` con i valori reali:

```env
GOOGLE_API_KEY=AIza...
PINECONE_API_KEY=pcsk_...
PINECONE_INDEX_NAME=odis-creator-rag
GITHUB_REPO=riccardo0326/html-files-odis
GITHUB_BRANCH=main
MD_SOURCE_PATH=md
INGEST_SOURCE=local
```

In alternativa, per testare Streamlit in locale con secrets:

```bash
mkdir -p .streamlit
cp .streamlit/secrets.toml.example .streamlit/secrets.toml
# Modifica .streamlit/secrets.toml con le tue chiavi
```

### 3.4 Eseguire l’indicizzazione

Dalla cartella `md/` locale (320+ file Markdown):

```bash
python ingest.py --source local
```

Per scaricare i file direttamente da GitHub:

```bash
python ingest.py --source github
```

Per ricreare l’indice da zero:

```bash
python ingest.py --source local --recreate-index
```

L’operazione può richiedere diversi minuti (embedding + upsert su Pinecone).

### 3.5 Avviare la Web App

```bash
streamlit run app.py
```

Apri il browser all’indirizzo indicato (di default `http://localhost:8501`).

---

## 4. Deploy su Streamlit Community Cloud

### 4.1 Preparare la repository GitHub

Assicurati che nella root del repository siano presenti:

- `app.py`
- `ingest.py`
- `requirements.txt`
- `rag_config.py`
- `rag_embeddings.py`
- cartella `md/` con i file Markdown

> **Nota**: l’indicizzazione (`ingest.py`) va eseguita **in locale** (o in CI) prima del deploy. Streamlit Cloud esegue solo `app.py`; i vettori devono già essere presenti su Pinecone.

### 4.2 Creare l’app su Streamlit Cloud

1. Vai su [https://share.streamlit.io/](https://share.streamlit.io/) e accedi con GitHub.
2. Clicca **New app**.
3. Seleziona:
   - **Repository**: `riccardo0326/html-files-odis` (o la tua fork)
   - **Branch**: `main`
   - **Main file path**: `app.py`
4. Apri **Advanced settings**.

### 4.3 Secrets — blocco TOML esatto

Incolla nel pannello **Secrets** il seguente blocco TOML (sostituisci i placeholder):

```toml
GOOGLE_API_KEY = "INSERISCI_QUI_LA_TUA_GOOGLE_API_KEY"
PINECONE_API_KEY = "INSERISCI_QUI_LA_TUA_PINECONE_API_KEY"
PINECONE_INDEX_NAME = "odis-creator-rag"
GITHUB_REPO = "riccardo0326/html-files-odis"
GITHUB_BRANCH = "main"
MD_SOURCE_PATH = "md"
```

5. Clicca **Deploy**.

### 4.4 Verifica post-deploy

- La sidebar deve mostrare il numero di **chunk indicizzati** (> 0).
- Prova una domanda, ad esempio: *"Come si avvia Odis Creator?"*
- Espandi **Fonti utilizzate** per verificare i file `.md` recuperati.

---

## 5. Struttura file del progetto RAG

```text
.
├── app.py                      # Web App Streamlit (chatbot)
├── ingest.py                   # Script di indicizzazione
├── rag_config.py               # Configurazione condivisa
├── rag_embeddings.py           # Wrapper embedding Gemini
├── requirements.txt            # Dipendenze Python
├── GUIDA_SETUP.md              # Questa guida
├── .env.example                # Template variabili d'ambiente
├── .streamlit/
│   ├── config.toml             # Tema e impostazioni Streamlit
│   └── secrets.toml.example    # Template secrets locale
└── md/                         # Documentazione Odis Creator (.md)
```

---

## 6. Risoluzione problemi comuni

| Problema | Soluzione |
|----------|-----------|
| `GOOGLE_API_KEY non configurata` | Verifica `.env` o Streamlit Secrets |
| `Chunk indicizzati = 0` | Esegui `python ingest.py --source local` |
| Errore regione Pinecone | Sul piano free usa solo `us-east-1` |
| Risposta generica / senza fonti | Verifica che l’indice contenga vettori e che i metadati `text`/`source` siano presenti |
| Rate limit Gemini | Attendi qualche secondo e riprova; riduci `EMBED_BATCH_SIZE` in `rag_config.py` se necessario |

---

## 7. Aggiornare la documentazione

Quando aggiungi o modifichi file `.md` nella repository:

```bash
python ingest.py --source local --recreate-index
```

Oppure, per aggiornamento incrementale (sovrascrive chunk con stesso ID):

```bash
python ingest.py --source local
```

---

## Licenza e note

- La documentazione in `md/` appartiene al manuale Odis Creator.
- Le API Google Gemini e Pinecone sono soggette ai limiti dei rispettivi piani gratuiti.
- Non committare mai file `.env` o `.streamlit/secrets.toml` con chiavi reali nel repository.
