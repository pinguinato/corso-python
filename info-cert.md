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

## 0.5.2 Edube LABS

Serve per i laboratori.

# PARTE 1

## 1.1.1 Primo programma e funzione print()

        print("Hello World!")
        
**print** è una funzione di Python. Una funzione è una parte separata del codice che può:
- **causare degli effetti (un effetto)** (scrivere sul terminale, inviare un file ecc...)
- **valutare dei valori o più e darne un risultato (un risultato)**

Molte funzioni di Python sono in grado di fare insieme tutte e due le cose precedenti.

Da dove vengono le funzioni?
- dal Python stesso, dal linguaggio
- da moduli esterni o librerie di terze parti
- le possiamo scrivere noi

**Importante** 

Le funzioni devono sempre avere dei nomi significativi.

## 1.1.3 la funzione print()

Abbiamo capito che le funzioni possono avere:
- un effetto
- un risultato

Un altro importante componente di una funzione sono gli **argomenti**, di solito le funzioni
matematiche ricevono un solo argomento, le funzioni in Python riescono ad essere un pò più versatili e
sono in grado di accettare svariato numero di argomenti. Ci sono funzioni in Python che non 
accettano nessun argomento.
In Python per esprimere una funzione sono necessarie una coppia di parentesi subito dopo il nome della funzione.
Come si vede dalla funzione **print**.

        print(...)
        
Nell'esempio l'unico argomento fornito dalla funzione print è una **stringa**.

        print("Hello")
        
## 1.1.5 Invacazione di funzione

        function(argument)
        
Cosa fa Python dopo l'invocazione di una funzione?
- verifica che il nome sia legale
- verifica che i requistiti della funzione corrispondano al numero di argomenti passati
- Python lascia il nostro codice verifica la funzione da invocare e i suoi argomenti e li passa 
alla funzione
- la funzione esegue il codice e provoca l'effetto atteso
- Python ritorna al nostro codice

## 1.1.6 Ancora su print()

Tre domande:
- **Effetto della funzione print()?** invia su schermo una stringa di testo, converte il nostro argomento in 
una forma umana leggibile.
- **Quali argomenti/o si aspetta print()?** virtualmente tutti i tipi di dati Python. Stringhe, numeri,
caratteri ecc...
- **Quali risultati restituisce print()?** in effetti nessuno, non restituisce nessun risultato nè li valuta,
riporta solo testo su schermo.

## 1.1.7

Python richiede che non ci possano essere più di una istruzione per riga (perchè manca il separatore come il **;**).

Una riga può essere vuota (non contenere istruzioni), ma **non deve contenere** due o tre più istruzioni.

Es.

        print("bla bla") print("hello") # errore!!!
        
## 1.1.11 Modi di scrivere il testo su schermo - Escape characters \n

Modo semplice per fare un salto di riga:

        print('Roberto') 
        print()
        print("sadsa")

**Escape \n**

Usare il carattere \n per mandare il testo a capo:

        print('Robe\nrto') 
        print()
        print("sa\ndsa")

**Escape \\**

Se voglio usare lo \ nel testo:

        print("Roberto \\") # scrive Roberto \
        
Usare la funzione print con più argomenti, separandoli con la virgola:

        print("Roberto", " Gianotto")
        
I modi visti di passare argomenti alla funzione print() di Python si definiscono **posizionali**.

Il codice viene stampato nell'ordine in cui viene scritto nel file.

## 1.1.16 Cambiare il comportamento di print() uso di end=

Esempio:
    
        print("My name is", "Python", end=" ")
        print("Monty Python")
        
        >>> My name is Python Monty Python

Cosa fa il carattere **end=**?

Riflette il carattere " " alla fine degli argomenti posizionali, cioè le stringhe, sovrascrivendo
la print() che va a capo.

Invece così:

        print("My name is", "Python", end="")
        print("Monty Python")
        
        >>> My name is PythonMonty Python

Si perde uno spazio, quello che avrebbe dato la funzione print() usata di default.

## 1.1.20 Usare un separatore di stringa sep=

Esempio:

        print("My name is", "Python", sep="-")

## Laboratorio

        print("Programming","Essentials","in",sep="***")
        
        print("Python",end="...")
        
## 1.2.1 Literals

**Literals**: è un valore che è determinato dal letterale stesso.

        print(2)
        
        print("2")
        
## 1.2.3 Integer

I numeri gestiti dai calcolatori sono di 2 tipi:
- interi (integer)
- virgola mobile (float)

Per esprimere un numero negativo ci metto il **-** davanti. I numeri positivi non hanno bisogno di essere
preceduti dal simbolo **+**.

Ci sono altre 2 rappresentazioni:
- ottale
- esadecimale

entrambe supportate da Python.

## 1.2.8 Floats

Sono numeri che hanno una frazione decimale non vuota. Sono i numeri che hanno una parte
frazionaria dopo il punto decimale. I numeri **float** si esprimono con il carattere **.**.

        2.5

Se usiamo la virgola come carattere abbiamo un errore perché in Python ha un altro significato.

In Python posso omettere lo 0 quando scrivo i numeri con virgola.

Es:

        invece di  0.4 posso scrivere .4
        
        oppure 4.0 lo posso scrivere come 4.

**Importante**

4 è un numero **integer**
4.0 è un numero **float**

## 1.2.12 Notazione scientifica

Si usa con i numeri molto grandi:

    se devo scrivere un numero così 300000000 lo posso scrivere 3E8
    
Es.

    Costante di Plank: 6.62607E-34
    
## 1.2.15 Letterali Stringhe

Necessitano delle **quotes** che sono gli apici.

Stampare una stringa con le quotes, si può:
- mettendo uno slash prima della virgoletta **\\"**
- usare gli apici singoli

Per scrivere il carattere apostrofo

        print('I\'m Monthy Python')
        
        print("I'm Monthy Python")
        
Per scrivere una stringa **vuota**

- ""
- ''

Esempio:

        print("I'm")
        print('learning')
        print("\"Python\"")

## 1.3.1 Operatori

Python può essere usato come una calcolatrice, la sua shell permette la manipolazione dei dati.

Un **operatore** è un simbolo del linguaggio di programmazione che serve ad operare su di un valore.

I dati e gli operatori quando vengono usati insieme formano le **espressioni**.
    
### 1.3.2 Operatori Aritmetici

        + - * / // % **
        
### 1.3.3 Esponente (**)

Es. 2**3 è come 2 elevato alla terza.

        print(2**3)

        >>> print(2**3)
        8
        >>> print(2 ** 3)
        8
        >>> print(2. ** 3)
        8.0
        >>> print(2. ** 3.)
        8.0

**Importante**        
Quando entrambi gli argomenti sono interi il risultato è un **intero**.
Quando almeno uno è un float allora il risultato è un **float**.        
       
### 1.3.5 Moltiplicazione (*)

Es.

        >>> print(2 * 3)
        6
        >>> print(2 * 3.)
        6.0
        >>> print(2. * 3)
        6.0
        >>> print(2. * 3.)
        6.0
        
**Nota**
Valgono le stesse regole per gli argomenti espressi sopra.

### 1.3.7 Divisione (/)

Es.

        >>> print(6/3)
        2.0
        >>> print(6/3.)
        2.0
        >>> print(6./3)
        2.0
        >>> print(6./3.)
        2.0
        
6 è un **dividendo** e 3 è un **divisore**.

**Importante** 
Il risultato prodotto dall'operatore della divisione è sempre un **float**.

### 1.3.9 Divisione Intera (//)

Il risultato nella divisione intera è conforme alle regole di integer/float viste sopra.

Es.

        >>> print(6//3)
        2
        >>> print(6//3.)
        2.0
        >>>  print(6.//3)
        2.0
        >>> print(6.//3.)
        2.0
        
**Attenzione**

Il risultato di una divisione intera è sempre arrotondato all'intero più vicino. Il 4 nel 6 ci sta
una volta soltanto.

Es.

        >>> print(6//4)
        1
        >>> print(6.//4)
        1.0
        
**Attenzione**

Es. 
        
        >>> print(-6//4)
        -2
        >>> print(6. // -4)
        -2.0
        
In questo caso il risultato giusto sarebbe -1.5, però siccome -1.5 è vicino a -2 allora la divisione
intera riporta -2.

### 1.3.15 Operatore Modulo (%)

Es.

        >>> print(14%4)
        2 
        
è l'operazione di divisione che ritorna come risultato il resto. 14 modulo 4 vuol dire che
il 4*3 = 12 e 14 - 12 = 2

Es. 

        >>> print(12%4.5)
        3.0
        
Vengono mantenute le regole espresse sopra per interi/float.

### 1.3.19 La divisione per 0

- Non funziona la divisione per 0
- Non funziona la divisione intera per 0
- Non funzione il modulo per 0

### 1.3.20 Addizione(+)

Es.

        >>> print(-4+4)
        0
        >>> print(-4. +8)
        4.0
        
### 1.3.22 Sottrazione (-)

Es.

        >>> print(-4 -4)
        -8
        >>> print(4. - 8)
        -4.0
        >>> print(-1.1)
        -1.1
        
Il segno meno cambia il segno al numero, c'è un modo per preservare il segno è anteporre 
l'operatore **unario**.

Es.

        >>> print(+2)
        2

### 1.3.24 Precedenza degli operatori

Es.

        2 + 3 * 5
        
è ovvio che la moltiplicazione precede l'addizione. Python definisce la priorità di tutti gli operatori 
rispetto a priorità alte o basse, ovviamente gli operatori a priorità alta vengono prima di quelli 
a priorità bassa.

### 1.3.25 Bindging degli operatori

Il binding degli operatori determina l'ordine delle computazioni degli operatori. In Python la 
maggior parte degli operatori esegue binding da sinistra verso destra (**left-sided binding**).

Es.

        >>> print(9%6%3)
        0
        >>> print(9%6%2)
        1
        
**Attenzione**

L'operatore esponente usa il **right-side binding**

Es.

        >>> print(2**2**3)
        256
        
viene fatta prima 2^3 = 8 e poi 2^8 = 256

### 1.3.29 Lista della priorità

1) Unario + e -
2) ** esponente
3) moltiplicazione, divisione e modulo
4) Binario + e -

### 1.3.30 Operatori che hanno stessa priorità

Es.

        >>> print(2*3%5)
        1
        
Possiamo usare le parentesi per imporre un ordine dei calcoli.

Es.

        >>> print(5*((25%13) + 100) / (2*13) //2)
        10.0
        
## 1.4.1 Le variabili

Dentro ci possiamo mettere quello che vogliamo.

Hanno un **nome** e un **valore**.

Regole per nomi delle variabili in Python:
- un nome di una varibile si compone di lettere maiuscole/minuscole/numeri/underscore
- underscore è una lettera
- una variabile deve iniziare con una lettera
- maiuscolo e minuscolo vengono trattati in maniera differente
- non possiamo usare come nomi delle variabili le parole riservate del linguaggio

Sintassi:

        nomevariabile = valore
        
Es.

        >>> var = 1
        >>> print(var)
        1

Es.

        >>> var = 1
        >>> account_balance = 1000.0
        >>> ClientName = 'John Doe'
        >>> print(var,account_balance, ClientName)
        1 1000.0 John Doe        

Se uso delle varibli che non esistono ottengo un errore!!

L'operatore **=** viene detto **operatore di assegnamento**.

Es.

        >>> var = 1
        >>> print(var)
        1
        >>> var = var+1
        >>> print(var)
        2
        
## 1.4.10 Commenti

Quando Python incontra un commento lo ignora.

Per inserire commenti anteposse il segno **#** al testo.

Es.

        # commento in Python
        
## 1.4.13 Operatori Shorcut

        var = var op exp ==> var op=exp

- var = var +1 diventa var += 1
- var = var *2 diventa var *= 2
- var = var ** 2 diventa var **=2

ecc...

## 1.5.1 Come parlare ad un computer?

### La funzione input()

Questa funzione legge dati di input dell'utente.

Es.

        >>> var = input("Inserire qualcosa")
        Inserire qualcosa10
        >>> print(var)
        10
        
### 1.5.4 la funzione str()

Es. ERRORE

        >>> var = 1
        >>> print ("il valore di var è = " + var)
        Traceback (most recent call last):
            File "<pyshell#58>", line 1, in <module>
            print ("il valore di var è = " + var)
            TypeError: can only concatenate str (not "int") to str

Soluzione: la funzione **str()**, permette di stampare un numeero come stringa!

         >>> print ("il valore di var è = " + str(var))
         il valore di var è = 1
         
         #input a float value for variable a here
        a = 10.0
        #input a float value for variable b here
        b = 15.5
        #output the results of addition, subtraction, multiplication and division
        print("Addizione = " + str(a + b))
        print("Sottrazione = " + str(a -b))
        print("Moltiplicazione = " + str(a * b))
        print("Divisione = " + str(a / b))
        print("That's all, folks!")
         
### 1.5.6 Funzioni int() e float()

Si possono combinare con la funzione **input()** per convertire in intero(int()) o float(float()),
l'input du numeri.

Es.

        >>> var = float(input("Inseirire un numenro con virgola: "))
	    Inseirire un numenro con virgola: 10.5
        >>> print(var)   
        10.5

### 1.5.11 Concatenazione di stringhe

Si usa l'operatore **+**.

### 1.5.13 Replication Operator

Si usa l'operatore della moltiplicazione.

Es.

        print("2" * 5)
        
Disegnare una rettangolo:

        print("+" + 10 * '-' + '+')
        print(("|" + ' ' * 10 + '|\n') * 5, end='')
        print("+" + 10 * '-' + '+')

# PARTE 2

## 2.1.1 Domande e Risposte

I computer hanno solo 2 risposte: vero e falso.

Per rispondere alle domande Python usa degli operatori molto poarticolari.

## 2.1.2 Verifica se due valori sono uguali

Python usa l'operatore **==**, è un operatore binario a left-sided binding.

## Operatori >, >=, <, <=, !=

## Ordine degli operatori

| Operatore  | Nome |
|------------|------|
|  +-  | unari      |
|  **  | esponente  |
|  */% | molt. div. mod.  |
|  +-  | binari|
|  <<=>>=||
|  != ==||

## 2.1.13 Statement IF

        if condizione:
            espressione
            
## 2.1.17 Statement IF ... ELSE

        if condizione:
            espressione
        else:
            espressione

## 2.1.21 Statement IF ... ELIF ... ELSE

       if theWeatherIsGood:
          goForAWalk()
       elif TicketsAvailable:
          goToTheTheatre()
       elif TableAvailable:
          goForLunch()
       else:
          playChessAtHome()
          
- non possiamo usare else senza prima usare un if
- else è sempre l'ultimo statement
- else è opzionale e può essere ommesso
- se c'è un ramo else nella cascata di statement solo uno dei ramis viene eseguito
- se non c'è else è possibile che non venga eseguito nessun ramo                               

**Nota**

Se if o else contengono una sola istruzione li puoi scrivere in linea.
Es:

        if number1 > number2: max = number1
        else: max = number2
        
*Pseudocodice*: è un linguaggio con cui definiamo gli algoritmi, è conciso, leggibile.

## 2.2.1 Ciclo While

        while condition:
            expression

Se si vogliono usare più istruzioni nello stesso while, il codice va identato!

        while condition:
            instruction_1
            instruction_2
            ...
            instruction_n
            
Le istruzioni dentro il ciclo while vengono definite **loop body**.

**Importante**

- Se la condizione è **False** il body non viene eseguito nemmeno una volta.
- Se la condizione è **True** il body si esegue all'infinito.

## 2.2.4 Looping your code

        while True:
            print("I'm stuck inside a loop")
            
Esempio:

        max = -999999999
        number = int(input("Enter the value or -1 to stop while: "))
        while number != -1 :
            if number > max :
                max = number
            number = int(input("Enter the value or -1 to stop while: "))
        print("The largest number is ", max)    

Esempio (algoritmo pari e dispari)

        Evens = 0 # quanti pari
        Odds = 0 # quanti dispari
        Number = int(input("Enter the value or 0 to stop: "))
        while Number != 0:
            if Number % 2 == 1: # dispari
                Odds += 1
            else:
                Evens += 1
            Number = int(input("Enter the value or 0 to stop: "))
        print("\nI numeri pari sono: ", Evens)
        print("\nI numeri dispari sono: ", Odds)
        
Esempio (numero magico)

        secret_number = 8
        print("Welcome to my game, muggle!\nEnter an integer number and guess what number I've picked for you!\nI'll give you a hint: it's an integer number from 0 to 10.")
        my_number = int(input("Enter a number: "))
        while my_number != secret_number:
            my_number = int(input("No, that's not the number I've picked for you. Try again! Enter a number: "))
        print("Well done! That's the number I've chosen for you! You are free now.")
        
**Importante**

Condizioni equivalenti che si comportano allo stesso modo(algoritmo dei pari e dispari):

           while Number != 0:
           
           while Number:
           
           if Number % 2 == 1:
           
           if Number % 2:        
           
## 2.2.9 Fermarsi nel While

            counter = 5
            while counter != 0:
                print("My name is ...")
                counter -= 1
                
Quando counter arriva a 0 il programma esce dal while.

Potevo anche scrivere nella condizione di while:

            while counter:
            
# 2.2.12 Il ciclo For

Per certi compiti risulta essere più comodo del while, soprattutto quando dobbiamo
ripetere tante volte una specifica istruzione.

Es.
        
        for i in range(100):
            istruzione
            
- la parola chiave for apre il llop for
- la variaible **i** viene detta variabile di controllo e conta i giri del ciclo
- la parola chiave **in** introduce il range dei possibili valori di **i**
- la funzione **range()** genera tutti i possibili valori di i.

Es.

        for i in range(10):
            print("Hello ", i)
            
Stampa Hello da 0 a 9.

## 2.2.15

**Importante**

La funzione range() può avere più parametri:

        for i in range(2,8):
            print("Hello ", i)
            
Stampa Hello da 2 a 7, 8 escluso!
- range() accetta **solo interi come argomenti**.
- range() può accettare anche **3 argomenti** dove il terzo argomento è l'incremento
del range.

Es:

        for i in range(2,8,3):
            print("Hello ", i)
            
Stampa Hello di 2 e Hello di 5.

Esercizio:
        
        for i in range(1,11):
            print(i, "Mississippi")
            
## 2.2.22 Break e Continue

Puoi anche farne a meno, sono chiamati **zucchero sintattico**.

- **break**: esce dal loop immediatamente, termina le operazioni del loop, il programma
riprende dalla più prossima operazione dopo il loop
- **continue**: si comporta come se il programma avesse raggiunto la fine del corpo, il turno
successivo viene avviato e l'espressione della condizione viene testata immediatamente.

Sono entrambi parolo chiavi del linguaggio Python.

Es.

        while True:
            secret = input("You're stuck in an infinite loop! Enter a secret word to leave the loop:")
            if secret == "chupacabra":
                print("You've successfully left the loop")
                break
            else:
                secret = input("You're stuck in an infinite loop! Enter a secret word to leave the loop:")

## 2.2.24 Loop e Else

Entrambi i loop **while** e **for** possono essere arricchiti da una interessante
opzione **else**.

Il ramo finale **else** dei loops viene eseguito sempre almeno una volta, indipendentemente
che il loop sia entrato o no nel suo corpo.

Es.

        i = 1
        while i < 5:
            print(i)
            i = i + 1
        else:
            print("else: ", i)
            
        Viene stampato:
        1
        2
        3
        4
        else: 5
        
Es.

        i = 5
        while i < 5:
            print(i)
            i = i + 1
        else:
            print("else:",i)
            
        Risultato:
        else:5
        
Es. 

        for i in range(5):
            print(i)
        else:
            print("else:",i)
            
        Risultato:
        0
        1
        2
        3
        4
        else:4
        
Es.

        i = 111
        for i in range(2,1):
            print(i)
        else:
            print("else:",i)
            
        Risultato:
        else:111 # attenzione abbiamo inizializzato i prima del ciclo!! Il for non parte nemmeno
        
## 2.3.1 Logica del computer (gli operatori logici)

Questi operatori seguono le **tavole di verità**

## 2.3.2 And

Es. 

        Counter > 0 and value == 100
        
Validità di and:

        è True solo se entrambi sono veri, altrimenti è sempre False
        
## 2.3.4 Or

Validità di or:

        è True se almeno uno dei due lo è o entrambi lo sono, se entrambi False allora
        è False
        
## 2.3.6 Not

Validità di not:

        not nega l'espressione che segue, se True diventa False e viceversa
        
Es.

        not (var > 0)
        
        not var == 0
        
Es. 

        i = 1
        j = not not i
        
        i vale 1, mentre j vale True, il not tasforma j in un valore booleano!!

## 2.3.7 De Morgan

La negazione di una congiunzione è la disgiunzione delle negazioni.

La negazione di una disgiunzione è la congiunzione delle negazioni.

In Python:

        not (p and q) == (not p) or (not q)
        
        not (p or q) == (not p) and (not q)
        
**Importante**

Gli operatori logici prendono i loro argomenti nel loro insieme 
indipendentemente da quanti bit contengono. Gli operatori sono consapevoli 
solo del valore: zero (quando tutti i bit sono resettati) significa Falso; 
non zero (quando è impostato almeno un bit) significa True. 
Il risultato delle loro operazioni è uno di questi valori: Falso o Vero. 
Ciò significa che questo frammento assegnerà 
il valore True alla variabile j se i non è zero; altrimenti, sarà falso.

Es.

        i = 1
        
        j = not not i
        
## 2.3.9 Bitwise Operatori

Operatori in grado di manipolare i singoli bit di dati.

- Xor si indica con ^
- & ampersand
- | bar
- tilde (bitwise negation)

Gli argomenti di questi operatori devono essere interi!!!

## 2.3.21 Shifting Operator

- operazione sempre relativa ai singoli bit, si chiama spostamento
- si indica con il simbolo >> oppure <<
- si applica solo ai valori interi

Es.

        >>> var = 17
        >>> var_right = var >> 1
        >>> var_left = var << 2
        >>> print(var, var_right, var_left)
        17 8 68

- Lo spostamento a destra di 1 BIT equivale alla **divisione intera per 2**
- Lo spostamento a sinistra di 2 BIT equivale alla **moltiplicazione per 4**
- quindi: 17 // 2 = 8 e 17 * 4 = 68
        
## 2.3.22 Tabella riassuntiva precedenza degli operatori

| Operatore  | Nome |
|------------|------|
|  ++,--,!,tilde,+-  | unari      |
|  **  | esponente  |
|  */% | molt. div. mod.  | 
|  +-  | binari|
| <<, >> ||
|  <,<=,>,>=||
|  != ==||
| =, +=, -=, *=, >>=, <<=||

# 2.4 Le Liste

Es.

        numbers = [10,5,7,2,1]
        
Cambio valore:

        numbers[0] = 111
        
        >>> [111,5,7,2,1]
        
Copia valore:

        numbers[0] = number[4]
        
Scrivere il valore su schermo:

        print(numbers[0])
        
Scrivere una lista su schermo:

        print(numbers)
        
Scrivere la lunghezza di una lista (il numero degli elementi):

        print(len(numbers)
        
        >>> 5
        
Cancellare elementi da una lista:

        del numbers[1]
        print(len(numbers))
        print(numbers)
        
        >>> 4
        >>> [111, 7, 2, 1]
        
Errore se si accede ad elementi inesistenti:

        numbers[4] = 1
        
        Errore!!!
        
Sono consentiti indici negativi su una lista:

        print(numbers[-1])
        
        >>> 1
        
        print(numbers[-2])
        
        >>> 2
        
## 2.4.12 Metodi vs Funzioni

**Metodo**: è un tipo di funzione, sembra una funzione, ma differisce per il modo in cui viene 
invocato. Un metodo è in grado di cambiare stato dell'entità selezionata.

Es.

        result = data.method(args)

**Funzione**: non appartiene a nessun dato, ottiene dei dati in input e fornisce un risultato. La funzione
accetta un argomento, fa qualcosa e restituisce sempre un risultato.

Es. 

        result = function(args)
        
## 2.4.14 Aggiungere elementi ad una lista

Usiamo un metodo:

        numbers.append(4)
        
        >>> [111,7,2,1,4]

Mette in fondo alla lista un nuovo elemento.

## 2.4.15 Inserire un elemento in un punto specifico

Usiamo il metodo **insert(dove,cosa)**:

        numbers(0,222)
        
        print(numbers)
        
        >>> [222,111,7,2,1,4]
        
Aggiungere elementi con un ciclo:

        list = []
        for i in range(5):
            list.append(i + 1)
        print(list)
        
        >>> [1, 2, 3, 4, 5]
        
Aggiungere elementi al contrario:

        list = []
        for i in range(5):
            list.insert(0, i + 1)
        print(list)
        
        >>> [5, 4, 3, 2, 1]
        
## 2.4.22 Variante del ciclo FOR

Es.

        list = [10,1,8,3,5]
        sum = 0
        for i in range(len(list)):
            sum += list[i]
        print(sum)
        
        >>> 27

## 2.4.26 Un modo efficiente per ffettuare uno SWAP

Es.

        variabile1 = 1
        variabile2 = 2
        variabile1, variabile2 = variabile2 , variabile1
        
Es.

        x = 1
        y =2
        print(x)
        print(y)
        x,y = y,x
        print(x)
        print(y)
        >>> 1
        >>> 2
        >>> 2
        >>> 1
        
Es. (liste):

        list = [10,1,8,3,5]
        list[0],list[4] = list[4],list[0]
        list[1],list[3] = list[3],list[1]
        print(list)
        
        >>> [5,3,8,1,10]

Es. (liste)

        list = [10,1,8,3,5]
        l = len(list)
        for i in range(l // 2):
            list[i], list[l-i-1] = list[l-i-1],list[i]
        print(list)
        
        >>> [5, 3, 8, 1, 10]
        
## 2.5.1 Sorting di liste

## Bubble Sort per le liste

Es.

        # bubble sort per le liste

        list = []
        swapped = True
        num = int(input("How many element do you want to sort?: "))

        for i in range(num):
            val = float(input("Enter next element: "))
            list.append(val)
        while swapped:
            swapped = False
            for i in range(len(list)-1):
                if list[i] > list[i+1]:
                    swapped = True
                    list[i],list[i+1] = list[i+1],list[i]
        print("Sorted: ")
        print(list)

## 2.5.14 Metodo sort()

Possiamo ordinare le liste con il metodo **sort()**:

Es.

        list = [8,10,6,2,4]
        list.sort()
        print(list)        
        
# 3.1.1 Scrivere le proprie funzioni

Usiamo le funzioni per semplificarci la vita ed evitare di ripetere il codice più volte.
Ad esempio se vediamo che il codice inizia a ripetersi in più posti conviene scrivere una funzione.
Oppure se un frammento di codice diventa complesso da leggere conviene usare una funzione.
Dobbiamo decomporre i problemi per arrivare al prodotto finale. Soprattutto quando si lavora in team.

Da dove provengono le funzioni:

- da Python (quelle proprie del linguaggio tipo print(), int(), float() ecc...)
- dai moduli preinstallati in Python
- dal proprie codice

## 3.1.6 La tua prima funzione

Esempio:

        print("Enter next value: ")
        a = int(input())
        print("Enter next value: ")
        b = int(input())
        print("Enter next value: ")
        c = int(input())
        
il codice si ripete più volte, possiamo scrivere una funzione che semplifica il codice, in modo
che se dobbiamo intervenire lo andiamo a cambiare in un solo punto del codice una volta
soltanto.

Sintassi di una funzione:

        def nome_funzione():
            body_funzione
            
Le funzioni iniziano sempre con la parola chiave **def**, poi segue il nome di funzione seguita
da una coppia di parentesi dove mettiamo la nostra lista di **parametri**. La linea deve terminare
con i due punti. Andiamo a capo e iniziamo il **body** della funzione stessa.

Esempio:

        def message():
            print("Enter next value: ")
            
La richiamo nel mio codice in questo modo:

        message()
        a = int(input())
        message()
        b = int(input())
        .....
        
Quando si invoca una funzione, Python ricorda il luogo in cui è avvenuta e salta nella
funzione invocata. Viene eseguito il corpo della funzione, quando la funzione arriva alla fine 
Python ritorna al corpo del codice dove era rimasto.

**Importante**

- Non puoi invocare una funzione che non è nota al momento dell'invocazione!! Python 
legge il codice dall'alto verso il basso, non guarderà una funzione definita più avanti.

Esempio:

        print("We start here")
        message()
        print("End here")
        
        def message():
            print("Enter next value: ")
            
Questa situazione produce un errore.

- Non possiamo avere una funzione e una variabile che portano lo stesso nome!!

Esempio:

        def message():
            print("Enter next value: ")
            
        message = 1
        
- Però possiamo mescolare il nostro codice con tutte le funzioni nel nostro file sorgente

Esempio:

            print("We start here")
            
            def message():
                print("Enter next value: ")
            
            message()
            
            print("End here")
            
## 3.2.1 Funzioni parametrizzate

Come le funzioni comunicano con il loro ambiente? 

Attraverso l'uso dei parametri. Un parametro è una variabile.

Il parametro:
- esistono soltanto all'interno di funzioni in cui sono stati definiti e l'unico posto in cui si possono
definire è una coppia di parentesi nell'istruzione **def**.
-  l'assegnazione di un valore al parametro viene eseguita al momento dell'invocazione della funzione,
specificando l'argomento corrispondente.

**Importante**

- Parametri: vivino all'interno di una funzione
- Argomenti: vivino al di fuori delle funzioni e sono portatori di valori passati
ai parametri corrispondenti

Esempio:

        def message(no):
            print("Enter value number ", no)
            
**Attenzione**: non abbiamo assegnato alcun valore al parametro perché arriverà dall'
ambiente della funzione, se si specficano parametri nella funzione e non si invocano poi quando
si richiama la funzione, otteniamo un errore!!

Es:
            
          def message(no):
            print("Enter value number ", no)
          
          message() # questo produce errore!! Manca il parametro!!
          
Una funzione può ospitare quanti parametri vogliamo.

## 3.2.9 Passaggio di parametri posizionali

Tecnica che assegna il primo, secondo e terzo parametro secondo l'ordine di definizione
nella funzione stessa. Gli argomenti vengono definiti **argomenti posizionali**.

Es:

        def introduction(givenname, surname):
            print("Hello, my is ", givenname, surname, ".")
            
        introduction("Pippo", "Pallino")
        
        >>> Hello, my name is Pippo Pallino.
        
## 3.2.12 Passaggio dell'argomento della parola chiave

Modo alternativo di passare i parametri ad una funzione:

Es:

        def introduction(givenname, surname):
            print("Hello, my is ", givenname, surname, ".")
          
        introduction(givenname="Pippo", surname="Pallino")
        
**Attenzione**

Non possiamo usare un nome di un parametro che non esiste nella funzione!!

**REGOLA**

Devi mettere sempre gli argomenti **posizionali** prima di quelli di parola **chiave**.

Es:

        def sum(a,b,c):
            print(a,"+",b,"+",c,"=",a+b+c)
            
        sum(1,2,3)
        
        >>> 1 + 2 + 3 = 6
        
è un tipico esempio di passaggio posiazionale di parametri.

Es: variante per parola chiave

        sum(c=1,a=2,b=3)
        
        >>> 2 + 3 + 1 = 6
        
Es di errore:
        
        sum(3, c=1, b=2)
        
        >>> errore TypeError
        
Es che invece funziona:

        sum(3, 4, c=3)
        
        >>> 3 + 4 + 3 = 10
        
## 3.2.20 Funzioni con valori di parametri di default
        
Es (**valore di default**):

                
       def introduction(givenname, surname="Smith"):
            print("Hello, my is ", givenname, surname, ".")
        

       introduction("Robert") # Non produce alcun errore
       
       >>> Hello, my name is Roberto Smith.
       
Es:
        
        def introduction(givenname="John", surname="Smith"):
            print("Hello, my is ", givenname, surname, ".")
      
        introduction(surname="Foo")
        
        >>> Hello, my name is John Foo,
        
## 3.3.1 Effetti e risultati (valori di ritorno di una funzione)

            return
            
Parola chiave di Python, permette di restituire un valore nella funzione.

Ha una doppia funzionalità:

1) **se usata da sola all'interno della funzione ne causa l'immediata terminazione
e un ritorno immediato al punto di invocazione**

**Importante**

Se una funzione non è destinata a restituire valori, return viene usata implicitamente
alla fine della stessa. Allo stesso modo si può usare in un punto della funzione 
per terminarne l'esecuzione.

2) **usata per ritornare un'espressione finale e valutarne il risultato**

Il risultato dell'espressione ritornata viene trasportato al punto di invocazione della funzione e
volendo può essere salvato all'interno di una variabile.

## 3.3.8 Il valore NONE (nessun valore)

In realtà è l'assenza di valore, non va usato per calcolare espressioni perché
genera errore a runtime TypeError. **None** è una parola chiave. Esistono solo 2 situazioni 
in cui ha senso usarlo:

- quando lo si confronta con una variaibile per verificarne il suo valore interno
- quando lo si assegna ad una varibile e lo si restituisce come risultato

## 3.3.9 Importante

Se una funzione non restituisce alcun valore, utilizzando l'espressione return si intende
in realtà **return none**.

Es.

        def strange(n):
            if(n % 2 == 0):
                return True
                
Questa funzione se n=2 stampa True, se n=1 stampa None.

## 3.3.11 Passare un array/lista ad una funzione?

Es.

        def sumoflist(l):
            sum = 0
            for el in l:
                sum += el
            return sum
            
**Importante**

        print(sumoflist([5,4,3])
        
Ci restituisce 12 come risultato finale. Ma se passo:

        print(sumoflist(5))
        
Mi viene restituito un errore!! TypeError "Int object is not iterable".

##3.3.12 Può un elenco essere il risultato di una funzione?

Si perché qualsiasi entità può essere il risultato di una funzione in Python.

Es.
        
        def strngeList(n):
            list = [ ]
            for i in range(0,n):
                list.insert(0,i)
            return list
        
        print strngeList(5)
        
        >>> [4,3,2,1,0]
        
## 3.4 Funzioni e Scope

**Scope**: l'mabito di un nome (di una varibiale ead esempio) è la parte dove questa
e riconoscibile. Ad esempio l'ambito di un parametro di una funzione è la funzione stessa.

Es.

        def scope():
            x = 123
            
        scope()
        print(x)
        
        >>> errore NameError "x is not defined"
        
## 3.4.3 Varibile che esiste al di fuori delle funzioni

**Caso particolare**

Es. 

        def function():
            print("Conosci quella var?", variabile)
            
        variabile = 1
        function()
        print(variabile)
        
        >>> Conosci quella var? 1
        >>> 1

**Attenzione**

Però la variabile definita all'interno della funzione non è la stessa definita
all'esterno della funzione!!
     
Modifichiamo il codice così e ce ne accorgeremo:

Es.

        def function():
            variabile = 2
            print("Conosci quella var?", variabile)
            
        variabile = 1
        function()
        print(variabile)
        
        >>> Conosci quella var? 2
        >>> 1        

**REGOLA**

Una variabile esistente al di fuori di una funzione ha un ambito 
all'interno dei corpi delle funzioni, 
escluse quelle che definiscono una variabile con lo stesso nome.
Significa anche che **l'ambito di una variabile esistente 
all'esterno di una funzione è supportato solo quando si 
ottiene il suo valore (lettura)**. L'assegnazione di 
un valore forza la creazione della variabile propria della funzione.
 
Quindi **l'ambito interno ad una funzione va a sovrascrivere l'ambito esterno se 
questa viene riassegnata internamente**.

## 3.4.5 La praola chiave global

Ma quindi una funzione non è in grado di definire una variabile al di fuori di essa?

Non è vero, possiamo farlo estendendo lo scope di una variabile anche dentro le funzioni 
utilizzando una parola del linguaggio:

        global noma_var
        
Permette ad una variabile di estendere il proprio scope anche dentro le funzioni. Quindi 
posso assegnare valori a questa variabile anche da dentro le funzioni.

Quindi se una variaibile viene definita global allora Python bypassa il comportamento 
incontrato prima.

Es.

        def function():
            global variabile = 2
            print("Conosci quella var?", variabile)
            
        variabile = 1
        function()
        print(variabile)
        
        >>> Conosci quella var? 2
        >>> 2
        
Ecco fatto, abbiamo aggiunto global al nome della variabile dentro la funzione, e vediamo 
così che questa rimane la stessa variabile e non viene alterata dalla presenza di una altra
variabile "esterna" alla funzione, è sempre la stessa.

## 3.4.7 Come le funzioni interagiscono con gli argomenti

Es.

        def function(n):
            print("Adesso ho: ", n)
            n += 1
            print("Adesso ho: ", n)
            
        variabile = 1
        function(variabile)
        print(variabile)
        
        >>> Adesso ho: 1
        >>> Adesso ho: 2
        >>> 1
        
**Importante**

La modifica del parametro di una funzione, non si propaga al di fuori della funzione stessa.
Questo vuol dire che una funzione riceve il valore di un argomento, non l'argomento stesso! Questo
**vale per gli scalari**.

## 3.4.8 Se ho un elenco?

Es. 

        def function(list):
            print(list)
            list = [0,1]
            
        L = [2,3]
        function(L)
        print(L)
        
        >>> [2,3]
        >>> [2,3]
        
Viene stampato prima che sia modificato, quindi il risultato non varia! Se l'avessi stampata
dopo nell'ordine della funzione, avrebbe modificato il risultato.

**Attenzione**

Es.

        def function(list):
            print(list)
            del list[0]
            
        L = [2,3]
        function(L)
        print(L)
        
        >>> [2,3]
        >>> [3]
        
Il meccanismo visto prima sopra non vale con **del**. Questo perché:

- Non modifichiamo il valore dell'elenco dei parametri perché non ha nessuna alterazione
sul risultato finale
- ma se modifichiamo l'elenco identificato da questo(list), ha effetto sul risultato finale!!

**REGOLA**

Se l'argomento è un elenco, la modifica del valore del parametro corrispondente non influisce
sull'elenco, ma se si modifica un elenco identificato dal parametro (quindi l'elenco e non il parametro), 
l'elenco rifletterà la modifica!!

## 3.5 (esercizi - vedi cartella /esercizi)

### Esercizio 1 (indice di massa corporea)

        def BMI(weight, height):
            return weight / height**2

        print(BMI(80.8, 1.83))

### Esercizio 2 (modifica funzione BMI)

        def BMI2(weight, height):
            if height < 1.0 or height > 2.5 or weight < 20 or weight > 200:
                return None
            return weight / height**2

        print(BMI2(80.8,1.83))

### esercizio 3

Utilizzando delle funzioni helpers per le cifre Anglosassoni:

        def ftintom(ft, inch=0.0):
            return ft * 0.3048 + inch * 0.0254


        def lbtokg(lb):
            return lb * 0.45359237

        def bmi(weight, height):
            if height < 1.0 or height > 2.5 or weight < 20 or weight > 200:
                return None
            return weight / height**2


        print(bmi(height=ftintom(5,7),weight=lbtokg(176)))
        
### Fibonacci (Ricorsione 1)

        def Fib(n):
            if n < 1:
                return None
            if n < 3:
                return 1
            return Fib(n -1) + Fib(n - 2)

        print("Serie Fibonacci del numero 6:\n")
        print(Fib(6))
        
### Fattoriale (Ricorsione 2)

        def factorial(n):
            if n < 0:
                return None
            if n < 2:
                return 1
            return n * factorial(n - 1)


        print("Fattoriale di 5:\n");
        print(factorial(5))

## 3.6 Tuple e Dizionari

Un tipo **sequenza** in Python è un tipo dato in grado di memorizzare 
più di un valore, oppure anche nessuno e questi valori possono essere sfogliati in 
sequenza, da qui deriva il nome.

Il ciclo **for** è stato progettato per scorrer le sequenze e fino ad ora abbiamo 
affrontato una sola sequenza le **liste**.

**Dati Mutabili**

E' una proprietà di quei dati che in Python ci danno la possibilità di poterli
alterare/modificare a piacimento durante l'esecuzione del programma.
I dati mutabili possono essere modificati liberamente e chiamiamo questo tipo di 
operazione **in situ**.

        list.append(1)
        
**Dati Immutabili**

I dati immutabili non possono essere modificati in questo modo. 
Immagina che un elenco possa essere solo assegnato e letto. 
Non potresti né aggiungere un elemento ad esso né rimuovere alcun 
elemento da esso. Ciò significa che l'aggiunta di un elemento alla 
fine dell'elenco richiederebbe la ricreazione dell'elenco da zero. 
Dovresti creare un elenco completamente nuovo, composto 
da tutti gli elementi dell'elenco già esistente, più il nuovo elemento.

Un esempio di questo tipo di dati sono le **tuple**, loro non possono essere
modificate in situ.

## 3.6.2 Tuple

La prima differenza rispetto alle liste è nel modo in cui si possono creare:

Modi in cui posso creare una tupla:

        tupla = (1,2,3,4)
        >>> (1,2,3,4)
                
        tupla = 1,2,3,4
        >>> (1,2,3,4)
        
        tupla = 1.,.5,.25
        >>> (1.0,0.5,0.25)
        
Si può creare anche una **tupla vuota**:

        tupla_vuota = ()
        
Si può creare una tupla ad **1 solo elemento**:

        t = (1,)
        
        >>> (1)
        
        t = 1,
        
        >>> (1)
        
Le tuple si possono leggere allo stesso modo in cui si leggono le liste:

        t = (1,10,100,1000)
        
        print(t[0])
        
        >>> 1
        
        print(t[-1])
        
        >>> 1000
        
        print(t[1:])
        
        >>> (10,100,1000)
        
        print(t[-2])
        
        >>> (10,100)
        
        for el in t:
            print(el)
            
        >>> 1
        >>> 10
        >>> 100
        >>> 1000

**Importante**

Non si può modificare il contenuto di una tupla, non è una lista e si ottiene un errore
a runtime!

Es.
        
        t.append(10)
        
        del t[1]

        t[0] = -1

Tutte queste istruzioni causeranno un **runtime error**.

## 3.6.7 Join di tuple con +

L'operatore **+** permette di concatenare tuple:

Es. 

        t1 = (10,100)
        t2 = (100,1000)
        print(t1 + t2)
        >>> (10,100,100,1000)
        
## 3.6.9 Come usare le tuple

- **len()** questa funzione accetta le tuple e ne ritorna il numero di elementi contenuti
in essa
- **+** può concatenare tuple (tuple join)
- l'operatore di moltiplicazione moltiplica le tuple 

Es. 

        print(t1 * 3)
        
        >>> (10,100,10,100,10,100)
        
- **in** e **not in** funzionano come sulle liste.

Es. 

        print(10 in t1)
        >>> True
        print(100000 not in t2)
        >>> True
        
## 3.6.11 I Dizionari
        
Il dizionario è un'altra struttura dati di Python, non è un tipo sequenza, è **mutabile**.

        <k,v> k = chiave v = valore
        
Nel modo Python la parola che cerchi è chiamata **chiave**, la parola che ottieni è 
chiamata **valore**, è quindi una coppia <chiave,valore>.

Ogni **chiave** deve essere unica e non si può avere delle chiavi ripetute.

Un dizionario non è un elenco, perché un elenco contiene un insieme di valori 
numerati, mentre un dizionario contiene **coppie di valori**.

La funzione **len()** è valida anche per i dizionari e restituisce il numeri di 
coppie chiave/valore presenti.

Un dizionario **vuoto** è costituito da una coppia di parentesi graffe: { }

Es. di dizionario:

        dict = {'cat':'chat','dog':'chien'}
        
        phones = {'boss': 333444555, 'mom': 44455666}
        
        empty = {}
        
I dizionari, non essendo elenchi non conservano l'ordine dei loro dati.

Per ottenere un valore dal dizionario dobbiamo fornire un **valore chiave valido**.

Es. 

        print(phones['boss'])
        
Se la chiave è una stringa è necessario specificarla come tale. Se usiamo una chiave
inesistente provochiamo un **errore a Runtime**.

Cercare in un dizionario:

Es.

        dict = {'cat':'chat','dog':'chien'}
        
        words = ['cat', 'lion', 'horse']
        
        for word in words:
            if word in dict:
                print("Success")
            else:
                print("Nope")
                
**Nota**

Posso sfogliare i dizionari come fossero elenchi o tuple?

Si e no. No perché il dizionario non è un tipo sequenza e il for è inutile con esso.
Si perché posso adattare un dizionario ad un ciclo for. Usando ad esempio **keys()**:

Es. 

        dict = {'cat':'chat','dog':'chien'}
        
        for key in dict.keys():
            print(key, "--->", dict[key])

**keys()** restituisce con il for l'elenco composto da **tutte le chiavi** del dizionario.

Avere un elenco di chiavi ci permette di accedere in modo sempice al dizionario.

Per **ordinare** un dizionario:

Es.

        for key in sorted(dict.keys()):
            ....

**sorted()** permette di ordinare il dizionario!!

Possiamo scorrere un dizionario mostrandolo come un **elenco di tuple** e peer farlo
usiamo il metodo **items()**:

Es.

        for el in dict.items():
            ....
            
        >>> (cat, chat)
        >>> (dog, chien)
        
Oppure mostrarne solo i valori delle chivi usando **values()**:

Es.

        for val in dict.values():
            print(val)
            
        >>> chat
        >>> chien
        >>> ....

**Importante**

Siccome i dizionari sono mutabili posso modificarli:

Es.
         
         dict = {'cat':'chat','dog':'chien'}
         
         dict['cat'] = 'minou'
         
         print(dict)
         
         >>> {'dog':'chien','cat':'minou'}
         
## 3.6.19 Aggiungere una nuova coppia chiave-valore al dizionario

Es.

        dict['lion'] = 'lion'
        
        print(dict)
        
        >>> {'lion':'lion','dog':'chien','cat':'minou'}
        
## 3.6.20 Rimuovere elementi dal dizionario

**del** rimuove l'intera coppia <k,v> dal dizionario.

Es.

        del dict['cat']
        
        print(dict)
        
        >>> {'lion':'lion','dog':'chien'}
        

         
