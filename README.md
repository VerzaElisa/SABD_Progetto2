# SABD_Progetto2
Secondo progetto per il corso di Sistemi e Architetture per Big Data del corso di Ingegneria Informatica Magistrale dell'università di Roma - Tor Vergata
## Obbiettivo
L'obbiettivo del progetto é quello di riuscire a rispondere a 3 query su un dataset assegnato e trovabile al seguente link: http://www.ce.uniroma2.it/courses/sabd2223/project/out600_combined+header.csv<br>
Inoltre le specifiche del progetto asseriscono una serie di vincoli che devono essere rispettati:
- Le query devono essere processate con la tecnica dello stream processing
- Utilizzare Kafka come sistema a coda di messagi, su cui Flink possa trovare i dati
- Bisogna processare i dati utilizzando il framework Apache Flink
- Fare un analisi del throughput e della latenza end-to-end
- Elaborare la prima query anche con Apache Spark Streaming e confrontare i due framework
## Framework utilizzati
- Apache Flink: per l'elaborazione delle Query
- Apache Spark: per l'elaborazione solo della prima Query
- Apache NIFI: Framework per l'ingestion e per il pre-processing del dataset
- Apache Kafka: Sistema a coda di messaggi utilizzato per la comunicazione dei vari framework e script
- Apache zookeeper: necessario per il corretto avvio di Kafka
- Docker-compose: per contenerizzare e come framework di orchestrazione tra i vari container
## Dataset
il dataset é composto di dati finanziari fornito dall’azienda fintech Infront Financial Technology. In particolare il dataset riguarda lo scambio di strumenti finanziari su tre principali borse europee nel corso di una settimana. I dati si basano su eventi reali acquisiti da Infront Financial Technology per la settimana dall’8 al 14 novembre 2021 (cinque giorni lavorativi seguiti da sabato e domenica). Il dataset ridotto contiene circa 4 milioni di eventi (a fronte dei 289 milioni del dataset originario) che coprono 500 azioni (equities) e indici (indices) sulle borse europee: Parigi (FR), Amsterdam (NL) e Francoforte/Xetra (ETR). Gli eventi sono registrati cos`ı come sono stati acquisiti; alcuni eventi sembrano essere privi di payload.
## Requisiti di Sistema
Il sistema per essere avviato ha bisogno dell'installazione di Docker e Docker compose poichè il sistema è stato utilizzato in maniera contenerizzata.
## Avvio Sistema
Il sistema può essere avviato tramite lo script avvio_sistema.sh che si trova sulla directory principale del repository<br>
Per avviare il sistema basta eseguire il seguente comando:
```
sh avviosistema.sh
```
Questo permette l'avvio del sistema, in particolare,vengono avviati:
- 1 container per Zookeeper
- 1 container per Kafka
- 4 container per Flink (1 master 3 worker)
- 2 container per Spark (1 master 1 worker)
- 1 container per Nifi
Lo script si occupa di scaricare anche tutti i file necessari per la computazione, di creare autonomamente i topic su kafka, di instanziare e avviare i processori di Nifi e di avviare come ultima cosa il producer che permette la simulazione dell'invio delle tuple poco alla volta.<br>
Per avviare la computazione di Flink bisogna eseguire il comando:
'''
sh avvio_processamento -x <Nifi/Not>
'''
che permette di instanziare i tre job Flink per elaborare le query, il flag -x indica se l'elaborazione deve includere il preprocessamento o meno di default il preprocessamento é disabilitato<br>
## Consumer
Nella cartella Consumer sono inseriti script python per riportare i dati elaborati dalle 3 query su file csv <br>
Per avviare un consumer bisogna:
'''
cd Consumer
python3 Query*Consumer.py
'''
e sostituire * con il numero della query che si vuole avviare.

