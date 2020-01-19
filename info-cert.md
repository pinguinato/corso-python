# Info Certificazione Python

## Link 

https://edu.openedg.org/

https://edube.org/study/pe1

https://pythoninstitute.org/free-python-courses/

https://pythoninstitute.org/certification/pcep-certification-entry-level/

# Appunti Certificazione

## 0.1.1 Come operano i computer

Un programma permette di mettere in funzione un computer, senza programmi un computer
è come un piano senza musicista.

Un computer può eseguire solo semplici operazione, ma può ripeterlo spesso. Può svolgere comppiti
molto complessi, ma non è in grado di farlo da solo.

E' necessario istruire i **computer** attraverso i **programmi**, la chiave di tutto è un **linguaggio**.

## 0.1.2 Linguaggi naturali vs linguaggi di programmazione

Linguaggi ce ne sono tanti: linguaggio del corpo, linguaggio umano ecc ...
I computer usano i **machine language**.
I linguaggi per le macchine sono sviluppati dagli esseri umani per i computer. Le persone usano il linguaggio
per esprimersi e le parole evolvono nel tempo, questi sono i linguaggi naturali. Questi linguaggi possiedono 
- un alfabeto
- un lessico o dizionario
- una sintassi
- una semantica

Nei computer un completo set di comandi conosciuti viene definito **set di istruzioni** abbreviato come **IL**. 
IL sta alla base dei linguaggi per computer. IL è l'alfabeto di un computer. Però questo linguaggio è molto complesso
e abbiamo bisogno di un **linguaggio ad alto livello** che ci permette di avvicinarci al linguaggio umano e poter
parlare con un computer per fargli fare delle cose.

Un programma scritto in un linguaggio ad alto livello viene definito **source code**. Allo stesso 
modo il file che contiene questo codice viene detto **source file**.

## 0.1.3 Compilazione vs Interpretazione

I linguaggi per computer si compongono di:
- alfabeto
- lessico
- sintassi
- semantica

Per far si che un computer esegua il programma che scriviamo, dobbiamo tradurlo nel suo linguaggio macchina.

Questa traduzione, per fortuna, viene fatta dal computer stesso velocemente, attraverso due modi
differenti:

- Compilazione: il sorgente del programma viene tradotto **una volta**. Ogni volta che viene modificato il codice
sorgente, l'operazione di traduzione viene ripetuta. Chi si preoccupa della traduzione in **codice macchina**
è il **compilatore**. Il programma compilato poi viene preso e distribuito ovunque e non necessita del sorgente.
- Interpretazione: il programma viene tradotto ogni volta che va in esecuzione, chi fa questa traduzione è
l'**interprete**, il programma sorgente ncessita ogni volta dell'interprete per eseguirsi. Il codice viene distribuito così come è
perché tanto c'è sempre bisogno dell'interprete per eseguirlo.

Ci sono linguaggi che o seguono un approccio o un altro, mentre ci sono altri linguaggi che li seguono
entrambi.

### Cosa fa l'interprete (nei linguaggi sia compilati che interpretati come JAVA)

Scriviamo un programma, questo esiste come file all'interno del computer. E' un codice inserito solitamente in un file di testo.
Deve essere un **testo puro** senza formattazione varia. Viene invocato l'interprete che legge il file di testo.
L'interprete legge il file di testo sscorrendolo tutto quanto. L'interprete verifica le linee di testo
secondo i 4 aspetti che abbiamo citato prima:
- alfabeto
- lessico
- sintassi
- semantica

Ora, se il compilatore trova una eccezione, termina immediatamente l'esecuzione. L'interprete informa dove 
si trova l'errore che si è scatenato. Purtroppo non sempre i messaggi sono indicativi dell'errore corretto,
ma vengono lanciati solo quando si verifica la situazione eccezionale e non probabilmente dove è stato
commesso un errore di sviluppo. E' anche possibile che una certa porzione di codice venga eseguita comunque, fino a quando non 
viene rilevato il problema. Questo è un aspetto di questo modello.

### Quale è il modello migliore?

Non esiste una risposta ovvia, se ci fosse stata allora un modello avrebbe prevalso su di un altro.

**Python** è un linguaggio **interpretato**. Quindi si comporta esattamente come descritto sopra. Se devi
programmare in python hai bisogno di un interprete per eseguire i suoi programmi. Di solito i linguaggi
progettati per essere interpretati sono detti **linguaggi di scripting** e i programi sorgenti codificati
che li usano si chiamano **script**.

## 0.2.1 Che cosa è Python?

L'origine è Monthy Python. Il linguaggio è stato chiamato così in onore dello show televisivo.
Python è stato creato da Guido Von Rossum.

Obiettivi di Python (1999):
- semplice ed intuitivo
- open source
- comprensibile
- adatto per le attività quotidiane e brevi tempi di sviluppo

## 0.2.4 Perché Python?

### Vantaggi

- è facile da imparare in tempi brevi
- è facile da insegnare
- è facile da usare per scrivere nuovi software
- è facile da capire
- è facile da mantenere, installare e distribuire, è gratuito, aperto e multipiattaforma.

### Svantaggi

- non è veloce, non ha prestazioni eccezionali
- debug un pò complesso, però è più facile non commettere errori
- Python ha due concorrenti diretti: Perl e Ruby

Perl è più classico e vicino al C, Ruby è molto originale ed innovativo.

## 0.2.5 Perchè non Python?

Dove viene usato Python:

- servizi internet e motori di ricerca, cloud storage e social media.
- strumenti di sviuppo sono scritti in Python
- tester di sviluppo IT

Dove è assente:

- driver a basso livello
- motori grafici
- applicazioni per dispositivi mobili

## 0.3.1 Python 2 VS Python 3

**Python 2**: vecchia versione (termina aprile 2020), lo sviluppo è ad un vicolo cieco.

**Python 3**: nuova versione di Python, anzi la versione attuale del linguaggio.

Le versioni non sono compatibili! Gli script Python 2 non si possono eseguire su interprete Python 3  e viceversa.
Il programma va riscritto da zero!! E' troppo costoso migrare una vecchia applicazione Python 2, su una
piattaforma Python 3.

Python 3 oltre che ad essere migliore di Python 2 e proprio un altro linguaggio.

Per avviare nuovi progetti conviene usare Python 3, anche se ci sono ancora molte app in Python 2 e questo è il 
motivi oprincipale per cui è ancora abbastanza diffuso.

## 0.3.2 Python aka CPython

Python 2 e 3 hanno poi delle loro **derivate**.

- versioni di Python della Python Software Foudation (PSF)
- sono definiti Python canonici

Il presidente della PSF è Guido Von Rossum e ha usato il **linguaggio C** per scrivere la prima versione di Python.

Tutti i Python della PSF sono scritti in C.

L'implementazione PSF di Python viene definita **CPython**, il linguaggio C è anche il motivo per cui
quando si migra al C un Python è più facile.

## 0.3.3 Cython

Rimedia all'ineficcienza di Python, aumentadone le performance soprattutto nei calcoli matematici complessi, se da un certo lato
è molto meglio fare calcoli con Python, poi eseguirli è un problema di performance. Cython supplisce a questo problema.
Cython permette di scrivere i calcoli usando Python, ma poi traduce il tutto in codice C.

## 0.3.4 Jython

Jython permette di usare Python in ambienti Java. Al momento non esiste una versione conforme al Python 3, quella
attuale segue standard Python 2.

## 0.3.5 PyPy e RPython

PyPy è conforme Python 3, è uno strumento per coloro che sviluppano il linguaggio Python. RPython è
restricted Python.PyPy viene tradotto in C e non eseguito interpretativamente. Sviluppare una nuova funzionalità del codice
Python è più facile farla usando PyPy che CPython e questo è il motivo per cui viene usato dai creatori di Python.

## 0.4.1 Come ottenere Python e come usarlo

- **Linux**: dovrebbe già essere installato, perché è usato da componenti del sistema operativo. Se sei
utente Linux apri un terminale e digita:

        python3 
        
se c'è vedrai una cosa simile:

        Python 3.4.5 (impostazione predefinita, 12 gennaio 2017, 02:28:40)
        [Clang 3.7.1 compatibile GCC 4.2.1 (tag / RELEASE_371 / final)] su Linux
        Digita "aiuto", "copyright", "crediti" o "licenza" per ulteriori informazioni.
        >>>
        
Se Python 3 è assente, fai riferimento alla documentazione di Linux per scoprire come utilizzare il gestore pacchetti per scaricare e installare un nuovo pacchetto: quello di cui hai bisogno si chiama "python3" o il suo nome inizia con quello.

Tutti gli utenti non Linux possono scaricare una copia qui:

https://www.python.org/downloads/

- **Windows**: scarica dal sito il file installer e procedi seguendo le indicazioni di installazione
- **MAC**: dovrebbe esserci Python2 di default, per installare il 3 bisogna scaricare ed eseguire il file **.pkg**

Python contiene **IDLE**:
IDLE è l'acronimo: Integrated Development and Learning Environment.

Avviando IDLE, si avvia la Python Shell: la finestra che appare sullo schermo è la 
console Python (o solo console o shell Python o shell). Lo userai per eseguire semplici 
comandi Python e per vedere gli effetti delle esecuzioni dei tuoi programmi.

## 0.4.4 Il primo prgramma Python

Apri IDLE, poi clicca il menù File e poi la voce New, per lanciare l'editor e iniziare a scrivere il
primo programma.

Non confondere l'editor di IDLE con la Python Shell, svolgono 2 compiti differenti!!

Python necessita che i file di codice sorgente abbiano estensione **.py**.

Per eseguire il codice scritto nell'editor di IDLE, scegli la voce **run module**. Ora si apre
la python shell che esegue il codice.

IDLE contiene strumenti per analisi degli errori del codice che si digitano nell'editor.

## 0.4.11 Fixing del codice

La finestra di editor di IDLE non fornisce indicazioni utili sugli errori, ma lo fa la shell.

- **traceback**: percorso che fa il codice del programma
- **location error**: posizione dell'errore (riga)
- contenuto della riga errata
- nome dell'errore e breve spiegazione

## 0.5.1 Edube Sandbox

https://edube.org/sandbox?language=python

Strumento online per sviluppare con Python, non comporta l'installzione di Python sulla propria macchina.
L'interfaccia di Edube si compone di:
- finestra di editor
- finestra console
- barraa dei pulsanti azione (per eseguire il codice)

## 0.5.2