# Guida a ODIS Creator: Interfaccia e Introduzione

## 📋 Indice dei Punti Chiave per una Guida da Zero

Prima di addentrarsi nell'utilizzo pratico di ODIS Creator, è importante comprendere la struttura generale del software. Ecco i punti fondamentali che ogni nuova guida dovrebbe toccare all'inizio:

1. **Cos'è ODIS Creator** - Definizione e scopo del software nel contesto dei dati OEM
2. **Requisiti di sistema** - Cosa serve per far funzionare correttamente l'applicazione
3. **L'interfaccia principale** - Panoramica dei componenti fondamentali
4. **Navigazione di base** - Come muoversi tra le diverse sezioni
5. **I menu laterali** - Spiegazione dei diversi moduli funzionali
6. **Concetti chiave** - Terminologia essenziale (moduli di controllo, variabili di marca, progetti veicoli, ecc.)
7. **Workflow tipico** - Il flusso di lavoro generale dall'apertura all'esportazione
8. **Salvataggio e gestione dati** - Come mantenere i propri progetti al sicuro

---

## 🎨 Introduzione alla UI (User Interface) di ODIS Creator

### Panoramica Generale dell'Interfaccia

L'interfaccia di ODIS Creator è progettata con un layout intuitivo che divide lo schermo in tre zone principali:

```
┌─────────────────────────────────────────────────────────┐
│              BARRA DEL TITOLO E MENU                    │
├────────────────┬──────────────────────┬─────────────────┤
│                │                      │                 │
│  PANEL         │   AREA PRINCIPALE    │  PANEL DATI     │
│  LATERALE      │   DI LAVORO          │  (Proprietà)    │
│  SINISTRO      │                      │                 │
│                │                      │                 │
│  (Menu)        │  (Editor/Visualizer) │  (Info dettagli)│
│                │                      │                 │
└────────────────┴──────────────────────┴─────────────────┘
```

### 1. Componenti Principali dell'Interfaccia

#### 1.1 Barra del Menu Superiore

La barra superiore contiene:
- **File** - Gestione dei documenti (Apri, Salva, Esporta)
- **Edit** - Operazioni di modifica (Copia, Incolla, Elimina)
- **View** - Opzioni di visualizzazione e layout
- **Extras** - Strumenti aggiuntivi e utilità
- **Help** - Documentazione e supporto

La barra include anche barre di strumento con pulsanti di accesso rapido per le operazioni più frequenti (Salva, Annulla, Ripeti, ecc.).

#### 1.2 Panel Laterale Sinistro - Navigazione Principale

Il panel sinistro è il cuore della navigazione in ODIS Creator. Contiene un menu strutturato gerarchicamente con i seguenti moduli principali:

**🔷 Order management** (Gestione degli Ordini)
- Punto di partenza per la gestione dei progetti
- Accesso ai file di ordine e alle loro proprietà

**🔷 Editing** (Modifica)
- Sezione dedicata alla modifica dei dati
- Strumenti per l'editing avanzato

**🔷 Equipment Network** (Rete di Apparecchiature)
- Visualizzazione della rete di componenti hardware
- Lista di componenti disponibili con identificativi come:
  - `Audi@00000`
  - `Bentley@00000`
  - `Bugatti@00000`
  - `Lamborghini@00000`
  - `MAN@00000`
  - `Seat@00000`
  - `Skoda@00000`
  - `Volkswagen@00000`
  - `Ford@00000`
  - E altre marche

**🔷 Knowledge base** (Base di Conoscenza)
- Repository centrale di informazioni e dati di riferimento
- Contiene documentazione tecnica condivisa

**🔷 Function Library** (Libreria delle Funzioni)
- Collezione di funzioni disponibili per il progetto
- Include:
  - Function tests (Test delle funzioni)
  - General tests (Test generali)
  - Measured values tables (Tabelle di valori misurati)
  - Test procedures (Procedure di test)
  - Traversal tests (Test di traversata)
  - Default measurements (Misurazioni predefinite)

**🔷 Control Module Tree** (Albero dei Moduli di Controllo)
- Struttura gerarchica dei moduli di controllo del veicolo
- Due categorie principali:
  - **Base control modules** - Moduli di controllo fondamentali
  - **Functional control module groups** - Gruppi di moduli funzionali

**🔷 DTC memory** (Memoria DTC - Diagnostic Trouble Code)
- Gestione dei codici di diagnostica guasti
- Elenco organizzato di DTC disponibili con identificativi come:
  - `0000002816_P000800_"B" Camshaft Position Bank 1`
  - `0000002860_P000B2C_"B" Camshaft Position Bank 2`
  - E molti altri...

**🔷 Vehicle project** (Progetto Veicolo)
- Dati specifici del veicolo sotto diagnosi
- Informazioni sulla configurazione del veicolo
- Lista di marche supportate:
  - VOLKSWAGEN
  - VOLKSWAGEN_NUTZFAHRZEUGE
  - BENTLEY
  - SEAT
  - SKODA
  - LAMBORGHINI
  - AUDI
  - MAN
  - BUGATTI
  - FORD

**🔷 Supplemental documents** (Documenti Supplementari)
- Raccolta di documentazione tecnica aggiuntiva
- Contiene:
  - Adjusting guidelines (Linee guida di regolazione)
  - Block diagram (Diagrammi a blocchi)
  - Code table (Tabelle di codice)
  - Component description (Descrizione dei componenti)
  - Component location (Ubicazione dei componenti)
  - Connector view (Visualizzazione dei connettori)
  - Drawing (Disegni tecnici)
  - Function description (Descrizione delle funzioni)
  - Function test guide (Guida ai test delle funzioni)
  - Fuse assignment (Assegnazione dei fusibili)
  - Interactive wiring diagram (Diagrammi di cablaggio interattivi)
  - Measuring equipment (Apparecchiature di misurazione)
  - Networking Diagram (Diagrammi di rete)
  - Pin assignment (Assegnazione dei pin)
  - Repair manual (Manuale di riparazione)
  - Specified values (Valori specificati)
  - System circuit diagram (Diagrammi dei circuiti di sistema)
  - System description (Descrizione del sistema)
  - Technical service bulletin (Bollettini di servizio tecnico)
  - Tools (Strumenti necessari)
  - Wiring diagram (Diagrammi di cablaggio)

**🔷 XML Templates** (Modelli XML)
- Template predefiniti in formato XML
- Utilizzati per standardizzare la struttura dei dati

**🔷 Brand Variables** (Variabili di Marca)
- Variabili specifiche della marca automobilistica
- Esempio: `[LAMBORGHINI@00000]`
- Permettono la personalizzazione per diverse marche OEM

---

### 2. Area Principale di Lavoro (Centro)

L'area centrale della UI è dove si visualizzano e si modificano i dati. Quando si seleziona un elemento dal menu laterale sinistro, il suo contenuto appare in questa zona.

#### 2.1 Finestra di Dialogo Principale

La finestra principale contiene diverse sezioni informative:

**Sistema name (Nome Sistema)**
- Identifica univocamente il componente selezionato
- Esempio: `0000002816_P000800_"B" Camshaft Position Bank 1`
- È il codice di identificazione ufficiale nel sistema

**Display name (Nome Visualizzato)**
- Il nome amichevole che appare nell'interfaccia utente
- Esempio: `"B" Camshaft Position Bank 1`
- Più leggibile per l'utente rispetto al nome sistema

**Version (Versione)**
- Traccia la versione del componente/dato
- Formato numerico (es. 1.0, 2.5)
- Importante per il controllo dei cambiamenti

**Version comment (Commento di Versione)**
- Descrive le modifiche effettuate in questa versione
- Testo libero che documenta la storia delle modifiche
- Esempio: "importierte Version"

**Version history (Cronologia delle Versioni)**
- Tabella che mostra tutte le versioni precedenti
- Colonne: Version, Date, Version comment
- Permette il tracciamento completo della storia

**Comment (Commento)**
- Campo di note generale per documentare il componente
- Supporta testo libero
- Utile per aggiungere informazioni contestuali

**External version (Versione Esterna)**
- Numero di versione utilizzato in comunicazioni esterne
- Esempio: 205

**Code (dez)** (Codice decimale)
- Rappresentazione decimale del codice
- Esempio: 2816

**VAG code** (Codice VAG)
- Codice specifico del gruppo Volkswagen
- Esempio: P000800

**PVU/B/C code**
- Codice di riferimento tecnico specifico
- Esempio: P000800

#### 2.2 Tabella "List of source EVs" (Lista di EVs di Origine)

Una sezione tabulare che mostra:
- **Name** - Nome dell'elemento sorgente
- **Version** - Versione dell'elemento
- **Vehicle project** - Progetto veicolo a cui appartiene
- Esempio di voci:
  - EV_FCM36F1011039090G2 | 001004 | VW46X

#### 2.3 Sezione "Recently used objects" (Oggetti Recentemente Utilizzati)

Una tabella che traccia gli oggetti utilizzati di recente con colonne:
- **Name** - Identificativo dell'oggetto
- **Status** - Stato attuale (Risk release, In progress, ecc.)
- **Object type** - Tipo di oggetto (Fault location, Control module variant, Control module group, Vehicle project, Knowledge base)
- **Version** - Numero versione
- **Brand** - Marca di appartenenza
- **Last revision** - Data e ora dell'ultima modifica
- **Consistency** - Stato di coerenza dei dati
- **Content** - Ulteriori informazioni sul contenuto

---

### 3. Indicatori e Barre di Stato

#### 3.1 Barra di Stato Inferiore

La barra inferiore mostra:
- **Memoria utilizzata** - Esempio: "764M of 1094M" (memoria RAM in uso)
- **Contesto attuale** - Mostra il modulo o la vista attualmente attiva
- Esempio: "Editing View: XML template navigator"
- **Indicatore di progresso** - Se un'operazione è in corso

#### 3.2 Schede Tabulari

Diverse sezioni utilizzano schede per organizzare le informazioni:
- **Scheda 1** - Editorial objects (Oggetti Editoriali)
- **Scheda 2** - Editorial Objects (Variant) - (Varianti di Oggetti Editoriali)
- Permettono la visualizzazione di dati diversi nello stesso spazio

---

### 4. Strategie di Navigazione

#### 4.1 Espansione e Compressione dei Menu

Ogni sezione del menu laterale sinistro può essere:
- **Espansa** - Mostra le sottovoci della categoria
- **Compressa** - Nasconde le sottovoci (con icona "+")
- Clic sulla freccia/icona per togglare lo stato

#### 4.2 Selezione e Evidenziazione

Quando selezioni un elemento:
- L'elemento è evidenziato con sfondo colorato
- I dettagli vengono caricati nell'area centrale
- Le tabelle si aggiornano per mostrare i dati correlati

#### 4.3 Ricerca e Filtro

Il software supporta:
- Ricerca tramite il campo di ricerca (se disponibile)
- Filtri nelle tabelle
- Ordinamento per colonne (clic su intestazioni)

---

### 5. Colori e Iconografia

#### 5.1 Codice Colori

- **Blu** - Elementi selezionati/attivi
- **Grigio** - Elementi inattivi o disabilitati
- **Bianco** - Sfondo standard
- **Verde/Giallo/Rosso** - Indicatori di stato (success, warning, error)

#### 5.2 Icone Comuni

- 📁 **Cartella** - Indica una categoria/gruppo
- 📄 **Documento** - Indica un file o un elemento dati
- ⚙️ **Ingranaggio** - Impostazioni o configurazione
- ✓ **Spunta** - Completato/Verificato
- ⚠️ **Avvertenza** - Richiede attenzione
- 🔒 **Lucchetto** - Bloccato/Protetto

---

### 6. Workflow Tipico dell'Interfaccia

1. **Apertura dell'applicazione**
   - Si apre automaticamente con l'ultimo progetto utilizzato oppure con la schermata iniziale

2. **Selezione del modulo dal menu sinistro**
   - Clic su una voce principale per selezionarlo
   - Il contenuto si carica nell'area centrale

3. **Navigazione gerarchica**
   - Espandi le sottocategorie usando le frecce
   - Seleziona l'elemento specifico desiderato

4. **Visualizzazione dei dettagli**
   - I dettagli dell'elemento selezionato vengono mostrati nell'area centrale
   - Le tabelle correlate si aggiornano automaticamente

5. **Modifica (se necessario)**
   - Edita i campi disponibili
   - Aggiungi commenti e note
   - Traccia le versioni

6. **Salvataggio**
   - Usa Ctrl+S o il menu File > Save
   - Il software mantiene la cronologia delle versioni

7. **Esportazione o Pubblicazione**
   - Esporta i dati in formato XML o altri formati supportati
   - Pubblica il progetto se necessario

---

### 7. Aree Funzionali Specifiche

#### 7.1 Panel di Gestione Dati

Il panel destro (quando visibile) mostra:
- **Proprietà dell'elemento selezionato**
- **Metadati** (data di creazione, autore, ecc.)
- **Informazioni di stato**
- **Riferimenti incrociati** a elementi correlati

#### 7.2 Tabelle Dati

Le tabelle utilizzate in ODIS Creator hanno caratteristiche standard:
- **Ordinamento** - Clic sulla colonna per ordinare
- **Ridimensionamento colonne** - Trascina i bordi della colonna
- **Selezione multipla** - Ctrl+Click per selezionare più righe
- **Barra di scorrimento** - Per visualizzare più righe

#### 7.3 Campi di Input

I campi input supportano:
- **Testo libero** - Per inserire valori custom
- **Dropdown** - Per selezionare da un elenco predefinito
- **Numeri** - Con validazione formato
- **Date** - Con picker calendario (se applicabile)

---

### 8. Elementi Ricorrenti negli Screenshot

#### 8.1 Finestra Principale Ricorrente

Negli screenshot forniti, la finestra principale mostra sempre:
- System name: `0000002816_P000800_"B" Camshaft Position Bank 1`
- Display name: `"B" Camshaft Position Bank 1`
- Version: `1 | 0 | 0`
- Un set coerente di campi metadati

Questo evidenzia come la UI mantiene una struttura coerente indipendentemente dal modulo visitato.

#### 8.2 Menu Dinamico

Il menu laterale cambia in base alla selezione:
- Quando selezioni "Equipment Network", vedi le marche auto
- Quando selezioni "Control Module Tree", vedi moduli di controllo
- Quando selezioni "Supplemental documents", vedi tipi di documentazione

Questa dinamicità rende il software adattabile a diversi flussi di lavoro.

---

## 📌 Consigli per l'Utilizzo Iniziale

1. **Esplorare il menu** - Prendi familiarità con le diverse sezioni usando il menu sinistro
2. **Leggere i dettagli** - Ogni elemento ha informazioni utili nei campi di proprietà
3. **Consultare la guida** - Usa il menu Help quando hai dubbi
4. **Mantieni versioni** - Aggiungi sempre commenti alle versioni per tracciare i cambiamenti
5. **Organizza i dati** - Usa la struttura gerarchica per mantenere i dati organizzati
6. **Backup regolari** - Salva frequentemente e mantieni backup dei progetti importanti

---

## 🔧 Scorciatoie Tastiera Comuni

- **Ctrl+S** - Salva il progetto attuale
- **Ctrl+Z** - Annulla l'ultima azione
- **Ctrl+Y** - Ripeti l'azione annullata
- **Ctrl+F** - Apri il dialogo di ricerca
- **F1** - Apri la guida
- **Ctrl+Tab** - Passa tra schede aperte (se disponibile)

---

## ✅ Checklist Iniziale per Nuovi Utenti

- [ ] Ho aperto ODIS Creator e vedo la schermata principale
- [ ] Ho esplorato il menu laterale sinistro
- [ ] Ho cliccato su almeno tre moduli diversi
- [ ] Ho capito la differenza tra System name e Display name
- [ ] Ho visto come cambiano i dettagli quando cambio selezione
- [ ] Ho provato a scorrere una tabella di dati
- [ ] Ho letto la barra di stato inferiore
- [ ] Ho trovato il menu File per le operazioni di salvataggio
- [ ] Ho esplorato il menu Help per ulteriori informazioni
- [ ] Mi sento confortevole a navigare l'interfaccia

---

## 🧠 Deep dive: Knowledge base e Guided Function

La Knowledge base è l'area di ODIS Creator dove si definiscono gli oggetti concettuali del progetto: funzioni, documenti, diagnosi, procedure e strutture operative. Qui si costruiscono i blocchi informativi che poi vengono utilizzati dalle viste diagnostiche e dagli strumenti di pubblicazione.

### 1. Cos'è la Knowledge base

La Knowledge base rappresenta:
- un archivio gerarchico di oggetti
- un luogo in cui raccogliere regole, testo e riferimenti tecnici
- un punto centrale per collegare funzioni a moduli, vetture e marche

Nella UI, la Knowledge base è mostrata come un albero con nodi di livello superiore (es. `LB63x`, `LB71x`, `LB74x`, ecc.) e sotto-nodi specifici per sistemi, sottosistemi e componenti.

### 2. Struttura tipica dell'albero

Un oggetto della Knowledge base può contenere:
- un nome sistema (`System name`)
- un nome visualizzato (`Display name`)
- una categoria di documento o funzione
- attributi tecnici come il codice di marca e le regole di variante
- riferimenti ai contenuti e ai media collegati

Nell'albero si vedono oggetti come:
- `Powertrain`
- `J623 - Overview exhaust gas recirculation`
- altri oggetti diagnostici e di sistema

Questi nodi sono organizzati per funzione e per struttura del veicolo.

### 3. Come creare una nuova funzione nella Knowledge base

Il processo tipico è il seguente:

1. seleziona il nodo padre appropriato nella Knowledge base
   - ad esempio un ramo del motore, dell’impianto elettrico o del sistema di emissione
2. crea un nuovo oggetto figlio
   - usa il menu contestuale dell’albero o il pulsante "New"/"Create" se presente
3. compila i metadati principali
   - `System name`: identificativo tecnico univoco
   - `Display name`: nome leggibile per l’utente
   - `Version comment`: motivo della creazione o modifica
   - `Comment`: note di dettaglio e riferimenti interni
4. imposta campi specifici per la funzione
   - `General function`: indica che l’oggetto è una funzione generica
   - `Variant rule`: regole di variante per serie e versioni veicolo
   - `Brand assignment`: marchio a cui appartiene l’oggetto
5. salva e conferma la versione
   - utilizza il salvataggio esplicito o la scorciatoia
   - verifica che l’oggetto compaia nell’albero e nelle tabelle correlate

### 4. Che cos’è una Guided Function

Una `Guided Function` in ODIS Creator è una funzione progettata per guidare l’utente passo dopo passo in un percorso diagnostico o operativo. La UI mostra spesso una casella da spuntare `Guided Function` tra le proprietà dell’oggetto.

Quando si attiva `Guided Function`:
- l’oggetto viene trattato come un elemento con flusso guidato
- potrebbe essere esposto in modalità passo-passo nelle viste diagnostiche
- può includere istruzioni specifiche, controlli e risultati intermedi

### 5. Campi principali per una Guided Function

Su uno schermo tipo quello mostrato nello screenshot, i campi importanti sono:
- `System name`: nome tecnico dell’oggetto
- `Display name`: titolo della funzione
- `Version comment`: dichiarazione delle modifiche
- `Comment`: descrizione attuale, ad esempio `Root@Powertrain::id=2`
- `General function`: attiva il comportamento di funzione generale
- `Guided Function`: checkbox che dichiara la natura guidata dell’oggetto
- `Variant rule`: regole di vincolo tra varianti veicolo
- `Brand assignment`: marca di riferimento, utile quando la funzione è specifica a un produttore

### 6. Un esempio pratico

Nel screenshot si vede un oggetto `Powertrain` e uno relativo a `J623 - Overview exhaust gas recirculation`.

Per creare una nuova guided function simile potresti:
- collocarla sotto il ramo del sistema interessato (`Powertrain`, `Antrieb`, `Elektrik`)
- usare un nome chiaro come `J623 - Exhaust gas recirculation`
- impostare il `Display name` con una descrizione operativa
- spuntare `Guided Function` se il risultato deve essere un percorso guidato
- scegliere la categoria documentale più appropriata se l’oggetto è anche un documento tecnico

### 7. Suggerimenti pratici

- usa nomi coerenti e leggibili
- aggiungi sempre un commento di versione significativo
- mantieni la struttura ad albero ordinata per tema e per sistema
- verifica la consistenza con gli oggetti correlati in `Recently used objects`
- usa la Knowledge base come fonte principale per tutte le funzioni, anche se vengono poi richiamate da altre aree del software

### 8. Uso quotidiano della Knowledge base

In un workflow tipico:

1. identifichi il sistema o componente su cui vuoi lavorare
2. crei o selezioni il nodo corrispondente
3. definisci la funzione nel pannello di destra
4. salvi e aggiorni la versione
5. confermi che l’oggetto sia disponibile nelle viste diagnostiche o di pubblicazione

---

Questa sezione fornisce una prima guida di riferimento per muoversi nella Knowledge base e iniziare a definire una `Guided Function`. Se hai bisogno, posso completare la guida con esempi ancora più pratici e con una checklist per la creazione di un oggetto passo‑passo.
