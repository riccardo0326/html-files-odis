# **ODIS Creator – Manuale Operativo Base**

# **1. Introduzione**

## **1.1 Scopo del documento**

Questo manuale descrive l’utilizzo operativo di **ODIS Creator** come strumento di authoring

diagnostico, con riferimento ai flussi tipici dei brand del Gruppo (es. Lamborghini).

Il documento fornisce:

una **visione strutturata** dell’architettura ODIS Creator

- le **regole fondamentali** da rispettare

- il **lifecycle degli oggetti**

- le relazioni tra **GFF, DTC, EV, BV, Usage e Release**

- Le procedure operative dettagliate sono documentate separatamente nei tutorial dedicati.

## **1.2 Ambito e destinatari**

Il manuale è destinato a:

author diagnostici

- responsabili di copertura

- figure di handover tecnico

- Ambito:

DEV / pre-LIVE

- preparazione al rilascio

- analisi coverage e difetti

- **2. Strumenti e ambienti**

## **2.1 ODIS Creator**

Strumento di authoring per:

oggetti diagnostici

- funzioni (GF / GFF)

- test baseline

- usage calculation

- **2.2 System42**

Utilizzato per:

verifica ODX / PDX

- presenza ZDC

- versionamento diagnostico

- Procedura operativa:

**Tutorial – Verificare se uno ZDC è presente**

## **2.3 Order Management**

Utilizzato per:

complete / risk release

- hotfix

- export usage

- Procedura operativa:

**Tutorial – Mettere una funzione / oggetto in Risk Release**

# OC BASE

lunedì 4 maggio 2026

16:18

basics Page 1

---

## **2.4 HP ALM**

Sistema di tracking per:

requirements

- test coverage

- stato funzionale

- Procedura operativa:

**Tutorial – HP ALM: gestione e stato dei Requirements**

# **3. Architettura concettuale ODIS Creator**

## **3.1 Oggetti diagnostici**

L’oggetto diagnostico è l’unità base del sistema ed è associato a:

Diagnostic Address (DA)

- ECU

- Component Code

- Su un oggetto diagnostico si costruiscono:

funzioni

- GFF

- collegamenti a DTC

- Creazione operativa:

**Tutorial – Creare un nuovo Diagnostic Object in Knowledge Base**

## **3.2 Funzioni (GF / GFF)**

**GF**: funzione guidata generica

- **GFF**: funzione reattiva a uno o più DTC

- Regola fondamentale:

Per ogni oggetto diagnostico deve esistere **una sola funzione principale**, perché in ODIS

Service l’operatore vede il *display name*.

## **3.3 BV ed EV**

**BV (Basic Variant)**: struttura diagnostica di base del progetto

- **EV (Electronic Variant)**: contenuto diagnostico specifico per ECU

- BV ed EV sono elementi **strutturali**, non eseguibili.

Identificazione e significato icone:

**Tutorial – Simboli e icone per elementi e stati**

# **4. Stati degli oggetti e lifecycle**

Un oggetto in ODIS Creator può trovarsi negli stati:

In progress

- Completed

- Released (Risk released)

- Sono previsti tre passaggi fondamentali:

**Complete**

- **Risk release**

- **Finished and released** (diretto)

- Procedura dettagliata:

**Tutorial – Cambi di stato degli oggetti**

# **5. Navigazione e gestione strutturale**

basics Page 2

---

## **5.1 Copy, Reuse e Link**

In ODIS Creator:

**Copy** crea una copia fisica

- **Reuse as subnode** crea un link (soft-copy)

- Il reuse mantiene una sola fonte di verità.

Approfondimento e regole operative:

**Tutorial – Copy, Cut, Paste e Reuse**

## **5.2 Multiselezione**

La multiselezione è **più limitata della selezione singola** e richiede attenzione.

Regole principali:

CTRL per elementi separati

- SHIFT per elementi adiacenti

- la ramificazione incide sul comportamento

- Procedura corretta:

**Tutorial – Multiselezione in ODIS Creator**

# **6. GFF e DTC**

## **6.1 Relazione GFF ↔ DTC**

Le GFF reagiscono alla presenza di DTC tramite:

suspicion rules

- BV context

- usage calculation

- Non è ammesso usare DTC non realmente presenti sull’ECU.

## **6.2 Adattamento GFF esistente**

La modifica delle suspicion rules **non deve partire da zero**.

Regola chiave:

La modifica delle suspicion rules deve avvenire **solo dopo analisi dei DTC reali** per ogni

oggetto diagnostico.

Procedura dettagliata:

**Tutorial – GFF Adapt (non partire da zero)**

## **6.3 Verifica GFF su singola ECU**

Per capire cosa incide sulla copertura di una ECU è necessario:

partire da Self_diagnostic_capable_systems

- identificare l’oggetto diagnostico reale

- verificare Subsystems_marginal_conditions

- Procedura dettagliata:

**Tutorial – Check GFF in 1 ECU**

# **7. Usage e Coverage**

## **7.1 Usage Calculation**

La usage calculation:

collega GFF, DTC, EV e BV

- determina le percentuali di copertura

- Deve essere rifatta **dopo ogni modifica rilevante**.

## **7.2 Copertura GFF**

basics Page 3

---

La copertura GFF richiede:

creazione gruppo

- reuse KBN

- reuse EV

- Finished + Risk release

- Procedura dettagliata:

**Tutorial – Copertura GFF**

## **7.3 Copertura DTC**

La copertura DTC viene verificata tramite:

usage calculation

- export

- analisi Excel

- Procedura dettagliata:

**Tutorial – Estrazione DTC già coperti per ogni centralina**

# **8. Test Baseline (TBL)**

La Test Baseline contiene **tutto ciò che è stato modificato**, indipendentemente dallo stato degli

oggetti.

Rischio:

Una TBL può risultare funzionante anche se le funzioni non sono in Risk Release.

Procedura dettagliata:

**Tutorial – Creare una Test Baseline**

# **9. Hotfix**

L’hotfix è una consegna puntuale e **non cumulativa**.

Regola fondamentale:

L’hotfix va sempre creato nel **periodo n-1** rispetto al rilascio.

Procedura dettagliata:

**Tutorial – Creare e rilasciare un Hotfix (regola n-1)**

# **10. Security (SFD)**

Il lock/unlock SFD deve:

usare **subroutine standard**

- essere parametrizzato per ECU

- Le subroutine **non vanno duplicate**.

Procedura dettagliata:

**Tutorial – SFD Lock / Unlock**

# **11. Battery & Power Handling**

Alcune funzioni richiedono:

riavvio ECU

- stacco batteria

- continuità della funzione diagnostica

- Serve impostare **Without 12V power supply**.

Procedura dettagliata:

**Tutorial – Battery related functions**

# **12. Requirements (HP ALM)**

La gestione dei requirement include:

basics Page 4

---

status

- test coverage

- vehicle associato

- Il lifecycle del requirement deve restare coerente con:

sviluppo

- hotfix

- rilascio

- Procedura dettagliata:

**Tutorial – HP ALM: gestione e stato dei Requirements**

# **13. Best practice generali**

Salvare frequentemente

- Verificare sempre **USED / USED BY**

- Non rilasciare con X rosse presenti

- Non forzare usage o shortcut

- Commentare sempre le versioni

- Riferimento visivo:

**Tutorial – Simboli e icone per elementi e stati**

# **14. Conclusione**

Questo manuale fornisce il **quadro concettuale e le regole operative** di ODIS Creator.

Le procedure dettagliate sono intenzionalmente demandate ai tutorial dedicati, per mantenere:

chiarezza

- manutenzione semplice

- separazione tra *principi* e *azioni*

- **15. Appendice: esempi di codice**

## 15.1 Code a pause (loop)

## 15.2 Code a Restart-Reset

basics Page 5
