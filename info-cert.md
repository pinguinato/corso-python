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
