# Corso di Python (v 3.6)

L'indentazione in Python è obbligatoria e non rispettarla comporta
un reato federale!

## Funzioni del linguaggio importanti

- **input()** serve per gestire l'input dal terminale

- **print()** serve per stampare a video

- **int()** converte a int

- **str()** converte a stringa per poter concatenare

- **type()** mi dice il tipo che passo come parametro

## Operatori aritmetici

- +, -, *, / e modulo %
- potenza es. 7 ** 2 = 49

## Operatori di confronto

- ==
- !=
-  <, >=, <, <=

## Operatori booleani (logica booleana)

- and
- or
- not

2 == 2 and 1 > 2 dà come risultato **false**

not 3 == 3 dà come risultato **false**

## Controllo del flusso

La condizione espressa deve risultare True per essere eseguita altrimenti viene ignorata.

- if, elif, else

es: 

    if eta >= 18:
        consizione
        
- while

In questo ciclo tutto viene eseguito finchè rimane nello stato true.

es:

        contatore = 0
        while contatore <= 10:  
            print(contatore)
            contatore = contatore + 1
            
- break e continue

es:

    contatore = 0
    while True:
        print(contatore)
        contatore += 1
        if contatore > 5:
            print('Sto uscendo dal loop!')
            break

    contatore = 0
    while contatore < 10:
        contatore += 1
        if contatore == 6:
            print('saltato')
            continue
            print(contatore)
            
- for

Fintanto che la condizione di controllo resta true il ciclo esegue le istruzioni.

es:

    contatore = 0

    while contatore <= 10:
        print(contatore)
        contatore = contatore + 1

    # for

    for contatore in range(11):
        print(contatore)
        
Funzione range(): 

ci possiamo passare fino a 3 parametri

    range(start,stop,step)
    
es:

    for contatore in range(3,11,2):
        print(contatore)
        
output = 3,5,7,9

## LABORATORIO 1 - CALCOLATRICE IN PYTHON 3.6

    # Calcolatrice in python
    # autore: Gianotto Roberto

    while True:

        # esempio di print multiriga
        print('''
        Benvenuto al programma della calcolatrice in Python
        Creato da: Gianotto Roberto
        Di seguito un elenco delle varie funzioni disponibili:
        
        - Per effettuare una addizione, seleziona 1
        - Per effettuare una sottrazione, seleziona 2
        - Per effettuare una moltiplicazione, seleziona 3
        - Per effettuare una divisione, seleziona 4
        - Per effettuare un calcolo esponenziale, seleziona 5
        - Per uscire dal programma puoi digitare ESC
        ''')
    
        scelta = input('Inserisci il numero corrispondente all\'azione desiderata ---> ')
    
        if scelta == '1':
            print('\nHai scelto: Addizione')
            a = float(input('Inserisci il primo numero -> '))
            b = float(input('Inserisci il secondo numero -> '))
            print('Il risultato della somma e\' : ' + str(a + b) + '\n')
        elif scelta == '2':
            print('\nHai scelto: Sottrazione')
            a = float(input('Inserisci il primo numero -> '))
            b = float(input('Inserisci il secondo numero -> '))
            print('Il risultato della sottrazione e\' : ' + str(a - b) + '\n')
        elif scelta == '3':
            print('\nHai scelto: Moltiplicazione')
            a = float(input('Inserisci il primo numero -> '))
            b = float(input('Inserisci il secondo numero -> '))
            print('Il risultato della moltiplicazione e\' : ' + str(a * b) + '\n')
        elif scelta == '4':
            print('\nHai scelto: Divisione')
            a = float(input('Inserisci il primo numero -> '))
            b = float(input('Inserisci il secondo numero -> '))
            print('Il risultato della divisione e\' : ' + str(a / b) + '\n')
        elif scelta == '5':
            print('\nHai scelto: Esponenziale')
            a = float(input('Inserisci il primo numero -> '))
            b = float(input('Inserisci l\'esponente -> '))
            print('Il risultato della somma e\' : ' + str(a ** b) + '\n')
        elif scelta == "ESC":
            print('\nL\'applicazione verra\' chiusa')
            print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n')
            break
    
        loop = input('\nDesideri continuare ad usare l\'applicazione ? S/N ')
    
        if loop == "S" or loop == "s":
            print("\nSto tornando al menu principale...\n")
            print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n')
            continue
        else:
            print("\nGrazie ed arrivederci...\n")
            print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n')
            break

## Moduli della standard library

Ogni modulo di questa libraria è un programma e contiene un insieme di funzioni
per fare operazioni tra le più comuni.

Consultabile qui: https://docs.python.org/3/library/

Prima di usare tutte le funzioni della standard library, questi vanno **importati**.

Si importano con il comando **import**

es:

    #importa il modulo random e le sue funzionalità
    import random 
    
    for numero in range(10):
        valore = random.randint(1,50)
        print(valore)
        
Risultato:

questo codice stampa una serie di 10 numeri casuali compresi tra 1...50   

Esiste poi un'altra tipologia di import che permette di importare solo una funzione:

es:
    
    #importa una sola funzione
    from math import sqrt
    
    # importa tutte le funzioni della libraria math
    from math import *
    
N.B. si possono importare moduli esterni usando **PIP**

## Funzioni

Servono per riutilizzo del codice, il codice dentro una funzione deve essere indentato!

Sintassi:

        def nomefunzione(parametri)
        
es:

        def print3volteCiao():
            print("Ciao")
            print("Ciao")
            print("Ciao")
      
Per eseguire la funzione la devo richiamare:

        print3volteCiao()
        
Esempio con parametri:

        # definizione
        def sommatrice(a,b):
            print('Questa funzione somma')
            print('Somma due numeri passati come parametri')
            risultato = a + b
            print('Il risultato = ' + str(risultato))
        
        # richiamo funzione    
        sommatrice(15,5)
        
Esempio che ritorna in forma autonoma il risultato:

        def sommatrice(a,b):
            risultato = a + b
            return(risultato)
            
Altro esempio:

        def laptop_nuovo(ram,cpu, antivirus = False):
            print('Il nuovo laptop avrà le seguenti caratteristiche:')
            print('ram: ' + ram)
            print('cpu: ' + cpu)
            if antivirus == True:
                print('Hai comprato anche un antivirus')
                
N.B. tutte le funzioni hanno un **return** e se non visibile il risultato sarà **none**

## Variabili Globali e Locali

Le varibili possono avere 2 ambiti diversi:

- ambito locale (local scopes) --> viene creato ogni volta che una funzione viene chiamata e distrutto dopo un return

- ambito globale (global scopes) --> avviato da Python all'avvio del programma e distrutto alla sua chiusura, resta in vita dall'avvio alla chiusura ed è possibile accedere da ovunque nel programma.
 
 Per modificare una variabile globale da una funziona bisogna dichiarare il **global**
 
 Es (modifica global):
 
        x = 15
        
        def esempio():
            global x
            x =+ 2
            return x
        
        print(esempio())
        

 Es (modifica local):
 
        def mia_funz()
            spam = 24
            return (spam)
            
        eggs = mia_funz() + 6
        
        print(eggs)
        
In programmi complessi le variabili globali sono pesanti, sono molto consigliate le variabili locali.

## Gestione degli errori

Gli errori causano crash nel programma, vanno gestiti con le Eccezioni.

Si usano tre parole chiavi

- try: viene eseguito tutto se non si verificano errori

- except: si esegue quando si verifica un errore

- finally: si esegue un default

        def divisione(a,b):
            try:
                risultato = a / b
                print("Il risultato della divisione = " + str(risultato))
            except ZeroDivisionError:
                print("Non posso dividere per 0")

        divisione(10,0)
        
        def moltiplicatore():
            try:
                a = int(input('Inserisci il valore di a: '))
                b = int(input('Inserisci il valore di b: '))
                risultato = a * b
                print(risultato)
            except ValueError:
                print('Hey amico! solo caratteri numerici, grazie!')
            finally:
                print('Grazie per aver utilizzato questa applicazione!')
                
    
## Liste e Tuple

- **Lista**: tipo di dato che contiene al suo interno un insieme di dati uguale/diverso ordinati sulla base di un indice della lista, una lista
si definisce con un insieme di parentesi quadre []. Ad ogni lemento è associato un numero che ne
rappresenta la posizione per accedere in maniera rapida e precisa. L'inizio della lista ha sempre
 indice 0. Le liste sono **mutabili**.
 
Esempio di lista:
 
        elenco = [2, 5, "bacon", 3.14, "eggs"]

Accesso ad una lista:
        
        elenco[2]
        Risultato: 'bacon' 
        
Accesso con indice negativo:

        elenco[-2]
        3.14

Esempio:

        primi = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]
        
        # stampa completa della lista
        for primo in primi:
            print(primo)

Metodo **list()** per creare sottoliste si supporto:

        lista_numerica = list(range(99,300))

Eliminazione di un elemento da una lista, uso del metodo **del**:

        del lista_multipla[-2]
        
- **Tuple**: queste anch'esse sono insieme di dati, ma **immutabili**, si definiscono con una 
coppia di parentesi tonde ().

Esempio di tupla:

        tuple = (2,4,9,15,23)
        
        # cercando di eliminare un elemento si ha errore
        del tuple[0]
        
L'accesso ad elementi di una tupla o l'iterazione su di essi è molto più veloce.

## Liste e Stringhe

- La funzione **len()** restituisce la lunghezza dell'argomento passato ed è comune 
sia a stringhe che alle liste.

Esempio:

      spam = "La pratica"
      
      len(spam)
      
      risultato: 11

- Le funzioni **in** e **not in** verificano, sia su liste che stringhe se un carattere/numero
è presente all'interno di esse.

Esempio: 

    a = [1,2,3,4]
    b = "qwerty"

    1 in a
    True

    6 in a
    False

    "q" in b
    True

    "z" in b
    False
    
- Possiamo convertire una stringa in lista con il metodo **list()**

# Corso Python (Udemy)

# Paradigma Obejct Oriented

# La Python Virtual Machine

**Linguaggio compilato**: un compilatore traduce le istruzioni di un sorgente in un file eseguibile di codice binario. La Compilazione
viene eseguita una volta per ogni architettura.

**Linguaggio interpretato**: c'è un interprete che esegue direttamente il codice sorgente, istruzione per istruzione, ogni volta
che il programma viene passato all'interprete ogni volta lo traduce. Lo stesso sorgente può essere eseguito però su piattaforme differenti, e non
ha bisogno di essere ricompilato ogni volta.

**Linguaggio compilato in forma intermedia (bytecode)**: viene posto il bytecode in esecuzione in una VM, una macchina ideale.

Python è di fatto una VM, ciò che manda in esecuzione il nostro programma viene definito Python Virtual Machine.
Viene generato un bytecode che viene mandato in esecuzione sulla VM.

- sorgente (source.py)
- byte codeo (source.pyc)
- runtime (source.pyc dentro la VM Python)

# Programma Python

Insieme di file srogenti che contengono istruzioni, dove c'è un programma principale chiamato **script** 
e poi ci sono gli altri secondari detti **moduli** che sono delle librerie usate dal programma principale e che
contengono le librerie.

# Oggetti in Python

Tutto è un oggetto in Python. Anche se i programmi sono serie di istruzioni, la forma che Python
assegna alle entità di un programma è quella di **oggetto**.
Gli oggetti in Python sono strutture di dati con 3 caratteristiche:
- identità (id) -- id numerico univoco e immutabile, che lo distingue da tutti gli altri, dato a runtime
- tipo (type) -- una categoria che determina la natura di un oggetto (stringa, intero...)
- valore (value) -- è un dato o insieme di dati mantenuto all'interno di un oggetto

**Mutabile** cambia valore durante il ciclo di vita

**Immutabile** non cambia valore dutante il ciclo di vita

Mutabile ed immutabile vengono definiti dal tipo di oggetto.

# Literal

Fornire in Forma Letterale, che permette a Python di distinguere gli oggetti.

- 20 (intero)
- 'stringa' (stringa di testo)
- [1,2,3] (array, lista)

# Variabili

Si definiscono attravero una istruzione di assegnamento:

        a = 20
        
Nomi validi in Python:
- contiene lettere, numeri o caratteri unicode
- non può iniziare con un numero
- non può essere una parola riservata

In python una variabile non è un oggetto, ma un nome che punta ad un oggetto.

Può riferirsi ad oggetti che puntano a tipi diversi:

        a = 20
        
        a = 'Python'
        
Se assegnamo una varaibile ad un altra variabile viene considivso l'id

        a = 20
        
        b = a
        
Oggetto puntato e condiviso da a e b --> **reference count** è il contatore di riferimenti che tiene traccia delle reference degli oggetti
ce l'hanno tutti gli oggetti Python. Python libera il garbage collector quando il reference count va a 0. Python gestisce automaticamente 
la memoria dei propri oggetti grazie a questo meccanismo.

# Callable Object

- Oggetti **chiamabili**: sono codice eseguibile e non dati, contengono delle istruzioni al loro interno che noi possiamo eseguire esprimendo il loro nome (invocazione), hanno anche dei parametri
le funzioni sono l'esempio più significativo di oggetto chiamabile.
- Oggetti **non chiamabili**: sono dati che contengono valori o gruppi di valori (tipo le liste, variabili ecc...)

# Attributi

Gli oggetti in Python hanno:
- una identità (id)
- un valore
- **una serie di attributi** (che possono essere anche chiamabili (metodi))

## Dot Notation

        NomeOggetto.NomeAttributo
        
        NomeOggetto.NomeAttributo(Parametri)

        x.y --> ritorna il valore dell'attributo
        
        x.y() --> callable, esegue il codice del metodo x()
        
# Basic Data Type

Tipi di dato predefiniti più semplici che il linguaggio mette a disposizione (tipi numerici, booleani e stringhe).

## None

è un oggetto ed è l'unica istanza della classe NoneType, indica l'assenza di valore ed è un basic data type!
Quando una funzione ritorna un None, ritorna un non valore, ma comunque ritorna sempre qualcosa.

## Tipi Numerici

- integer
- floating point
- boolean

Tutti i tipi numeri sono **immutabili**. Il numero 3 è sempre 3, ma ciò non vuol dire che non possiamo cambiare 
le varibiali che puntano a questi oggetti. E' il valore dell'oggetto che non cambia!

Tipo integer: **int**

Dalla versione 3.6 è stato introdotto anche l'underscore per rendere più leggibili numeri molto grandi.

Basi di riferimento che possiamo usare:
- binario
- ottale
- esadecimale

Tipi booleani: **bool**

Sono sottotipi degli interi (ma solo in Python), ha solo 2 oggetti, uno true e l'altro false.
Ci consentono la rappresentazioni di oggetti a 2 stati.

Tipi Floating Point: **float**

La classe che li contiene si chiama **Float**.

La presenza del punto di separazione decimale dice a Python che il numero è floating point.

**Nota**

Python fornisce anche come basic data il supporto ai numeri immaginari.

Per verificare il tipo usare **type(variaible)**

### Esercitazione

        >>> x = 100
        >>> print(x)
        100
        >>> type(x)
        <class 'int'>
        >>> y = 0b1100100
        >>> type(y)
        <class 'int'>
        >>> f = 975.0
        >>> type(f)
        <class 'float'>
        >>> f = 9.75e2
        >>> print(f)
        975.0
        >>> type(f)
        <class 'float'>

## Stringhe

Sono un tipo di sequenza (sequenza di caratteri), una sequenza è una struttura che ha un ordine.

Il tipo = **str**

Ogni carattere che appartiene ad una stringa deve appartenere al set Unicode.

Sono oggetti **immutabili** come i numeri.

Le stringhe si definiscono dentro una coppia di apici singoli oppure doppi (come PHP).

La stringa vuota è comunque valida anche se non ha al suo interno nessun carattere. Si può scrivere una 
stringa multiline usando il carattere backslash. Come alternativa possiamo usare triple di apici, indicando
a Python che è una stringa multiline.

Le **sequenze di escape** consentono di inserire caratteri stmapabili e non sullo schermo (tipo il rotnorno a capo ecc...).

## f-string (interpolazione di stringhe dalla 3.6)

Altri modi di formattazione del testo:

- %-formatting (deprecata)
- str.format()
- f-string (dalla 3.6)

f-string è da preferire visto che è nuova.

Esempio:

        >>> titolo = "Isola misteriosa"
        >>> autore = "Giulio Verne"
        >>> f"Titolo: {titolo}, Autore: {autore}"
        'Titolo: Isola misteriosa, Autore: Giulio Verne'
        
Il valore delle due variabili viene inserito al posto giusto nella stringa, ciò viene detto interpolazione di stringhe.
Si ritrova in molti linguaggi di programmazione. L'interpolazione permette di usare una qualunque
espressione dentro le paretesi graffe, quindi possiamo metterci anche delle funzioni!

## Espressioni ed operatori

Permettono di creare espressioni complesse, un operatore è un simbolo che rappresenta una operazione. Gli operandi sono gli 
elementi su cui può intervenire l'operatore.

Esempio:

        x = 10 + 5
        
In python abbiamo:

- operatori aritmetici (+, -, *, /, //, %, **, - unario)
- operatori assegnamento (=, +=, -=, /=, //=, %=, **=, *=)
- operatori di confronto (>, <, ==, !=, >=, <=) ritornano sempre un valore boolean
- operatori logici (and, or, not), a questi operatori sono associate le tavole di verità
- operatori su sequenze (indexing, slicing, concatenazione con operatore +, lunghezza **len(stringa)**, massimo **max(stringa)**, e minimo **min(stringa)** )

### Indexing

        >>> s = 'ciao'
        >>> s[0]
        'c'

### Slicing (porzione di una stringa, sottostringa)

Da start a stop-1. Gli offset sono separati dai 2 punti. Gli slice ad indici negativi partono dal fondo.

        >>> s = 'python programming'
        >>> s[:]
        'python programming'
        >>> s[:9]
        'python pr'
        >>> s[9:]
        'ogramming'
        >>> s[0:9]
        'python pr'
        >>> s[9:0]
            ''
        >>> s[-9]
            'o'
        >>> s[-11]
        'p'
        >>> s[-12]
        ' '
        >>> s[-1]
        'g'
        >>> s[-3]
        'i'
        >>> s[-2] --> 2 caratteri prima della fine
        'n'
        >>> s[1:12:3]
        'yopg'
        >>> s[1:12:-3]
        ''
        >>> s[1:12:]
        'ython progr'

### Precendeza degli operatori

Distingue con le parentesi.

Esercizio valori booleani:

        >>> x = 100
        >>> y = 200
        >>> x and True
        True
        >>> x = 0
        >>> x and True
        0
        >>> x = 100
        >>> y = 200
        >>> not (x or y)
        False
        >>> (x < y) or (x > 2000)
        True
        >>> (x == 20) and (y == 200)
        False

# Importante (test dei valori di verità)

Valgono sempre FALSE:

- None
- False
- zero di qualunque tipo (0, 0.0)
- una sequenza vuota ('', (), [])
- un qualunque dizionario/oggeto vuoto {}

Tutto il resto è considerato TRUE.

# Conversioni di tipo

- **integer conversion**: usiamo la funzione **int()**. Se le stringhe contengono un numero vengono convertite ad intero altrimenti 
generano un errore
- **float conversion**: usiamo la funzione **float()**.
- **string conversion**: usiamo la funzione **str()**.
- **boolean conversion**: usiamo la funzione **bool()**.

# Strutture di dati

- Liste
- Tuple
- Dizionari
- Set

Sequenza: è un insieme ordinato di elementi, dove questi elementi sono indicizzati numericamente tramite la loro posizione,
un indice che parte da zero. Python possiede 2 tipologie di sequenze: liste e tuple.

Liste e tuple hanno elementi di tipo qualunque, però le liste sono mutabili(i suoi elementi possono cambiare nel corso di vita
della lista) e le tuple invece no(gli oggetti della tupla una volta che sono inseriti sono fissi e non possono cambiare).

## Le Liste

Sequenza di oggetti mutabile, anche diversi tra loro. Si usa la classe **list**.

        mylist = [] è una lista vuota
        mylist = [1,2,3] è una lista con elementi dentro
        mylist = list() è una lista vuota che sfrutta il costruttore della classe, ma ritorna sempre [] come primo esempio
        
        mylist = [10,20,30]
        mylist[1] ritorna 20
        mylist[-1] ritorna 30, ci si sposta al contrario nello scorrere la lista

Le liste possono contenere altre liste:

        mylist = [[1,2],[1,3],[1,4]]
        mylist[1][1] ritorna 3
        
Modifica di un elemento di lista:

        mylist = [10,20,30]
        mylist[1] = 50
        si ottiene [10,50,30]
        
Slice di una lista(come sulle stringhe perché sono delle sequenze):

        mylist = [10,20,30]
        mylist[:2]
        ottieni [10,20]
        
Lunghezza di una lista:

        usiamo la funzione len()
        mylist = [10,20,30]
        len(mylist)
        ritorna 3

Inserimento in una lista di un elemento:
        
        mylist = [10,20,30]
        mylist.insert(2,50)
        otteniamo [10,20,50,30]
        ricordare in particolare la dot notation che usiamo in Python per richiamare funzioni/attributi
        
Appendere in coda alla lista un nuovo elemento:

        usiamo il metodo append()
        mylist = [10,20,30]
        mylist.append(50)
        aggiunge in coda alla lista il nuovo elemento, otteniamo
        otteniamo [10,20,30,50]
        
Eliminare un elemento dalla lista(operatore **del**):

        usiamo l'operatore del
        mylist = [10,20,30]
        del mylist[1]
        otteniamo: [10,30]
        
Verifica se un elemento appartiene alla lista(operatore **in**):

        mylist = [10,20,30]
        20 in mylist
        otteniamo true
        
**IMPORTANTISSIMO**

Due nomi, una lista:

        mylist = [10,20,30]
        mylist2 = mylist
        mylist2[1]  = 60 una modifica di una lista che punta assieme ad un altra stessa lista
        in realtà si riflette ad entrambe le liste quindi:
        mylist sarà [10,60,30] e così pure
        mylist2 sarà [10,60,30]

Soluzione: possiamo evitare questa situazione servendoci del metodo **copy()** che va a sdoppiare a tutti gli effetti le liste
andando a copiare lemento per elemento della lista e lavorando così su due liste separate da lì in avanti:

        mylist = [10,20,30]
        mylist2 = mylist.copy()
        mylist2[1] = 60
        allora avrò la seguente situazione: 
        [10,20,30] per mylist
        [10,60,30] per mylist2
        
Esercizio sulle liste:

        >>> myList = [1,2,3,4,5]
        >>> print(myList)
        [1, 2, 3, 4, 5]
        >>> myList
        [1, 2, 3, 4, 5]
        >>> myList[:2]
        [1, 2]
        >>> myList[1:3]
        [2, 3]
        >>> myList[2:4]
        [3, 4]
        >>> myList.insert(1,6)
        >>> myList
        [1, 6, 2, 3, 4, 5]
        >>> myList.append(10)
        >>> myList
        [1, 6, 2, 3, 4, 5, 10]
        >>> del myList[3]
        >>> myList
        [1, 6, 2, 4, 5, 10]
        
## Le Tuple

Una tupla è una sequenza immutabile, ciò vuol dire che gli elementi di una tupla, una volta inseriti, dopo non possono 
più essere modificati. Tutte le tuple sono istanze della classe **tuple**

Istanziare una tupla:

        medaglie = () istanzia tupla vuota
        medaglie = tuple() istanzia tupla vuota
        
        medaglie = 'oro', 'argento', 'bronzo'
        medaglie = ('oro', 'argento', 'bronzo')
        
        >>> medaglie
        stampa ('oro', 'argento', 'bronzo')
        
**Unpacking** di una tupla:

        medaglie = ('oro', 'argento', 'bronzo')
        o,a,b = medaglie
        >>> o
        'oro'
        >>> a
        'argento'
        >>> b
        'bronzo'
        
Le tuple sono più efficienti delle liste, perché Python sa che non si può alterare nessuna Tupla. Quindi è consigliabile,
quando si può, usare delle tuple al posto delle liste.

Esercitazione sulle tuple:

        >>> t1 = (1,2)
        >>> t1
        (1, 2)
        >>> t2 = (3,4)
        >>> t2
        (3, 4)
        >>> myList = [t1, t2]
        >>> myList
        [(1, 2), (3, 4)] ho creato una lista di tuple!!
        >>> myList.append((5,6))
        >>> myList
        [(1, 2), (3, 4), (5, 6)]
        
## Dizionari

Simile ad una lista ma l'ordine degli elementi non è definto perché non sono sequenze. Un elemento di u dizionario
si compone di 2 oggetti <chiave, valore>. Le chiavi, una volta associate, non possono cambiare valore, sono immutabili.
Non ci sono limitazioni per i valori. I Dizionari però sono mutabili. In questo è come le liste.
Quindi è un oggetto mutabile. Una istanza della classe **dict**.

Esempio:

        myDict = {} //formato literal
        myDict = dict() // con costruttore
        myDict = { "primo": 10, "secondo":20, "terzo":30}
        
Aggiungere un elemento:

        myDict["quarto"] = 40 // lachiave si usa per accedere e cambiare il valore

Se la chiave non esiste, per Python significa aggiungere una chiave.

Eliminare un elemento:

        del myDict["secondo"] // il secondo elemento e la sua chiave vengono cancellati
        
        myDict.clear() // attributo che hanno tutti i dizionari, elimina tutti gli elementi del dizionario
        
        myDict = {} // anche così svuoto in un colpo solo il dizionario
        
Verifica di un elemento:

        "terzo" in myDict // si usa la chiave per la verifica --> Python ritorna True
        
Copia:

        myDict = myDict2 // si riferiscono a myDict, come le liste
        
        myDict2 = myDict.copy() // sdoppiamo il dizionario, come le liste
        
Esercitazione:

        >>> d1 = {10:"a",20:"b"}
        >>> d1
        {10: 'a', 20: 'b'}
        >>> type(d1)
        <class 'dict'>
        >>> d2 = {30:"c"}
        >>> type(d2)
        <class 'dict'>
        >>> d2
        {30: 'c'}
        >>> l1 = d1.items()
        >>> l1
        dict_items([(10, 'a'), (20, 'b')])
        >>> type(l1)
        <class 'dict_items'>
        >>> l2 = d2.items()
        >>> l2
        dict_items([(30, 'c')])
        >>> type(l2)
        <class 'dict_items'>
        >>> d3 = dict(l1)
        >>> d3
        {10: 'a', 20: 'b'}
        >>> d3.update(dict(l2))
        >>> d3
        {10: 'a', 20: 'b', 30: 'c'}

## Set

Un insieme è come una specie di dizionario da cui però si eliminano tutti i valori mantenendo soltanto le chiavi. Gli elemnti 
sono tutti univoci. Si usano le operazioni tipiche dell'insiemistica matematica.
La classe che li identifica è **set**.

Esempio:

        mySet = set()
        mySet = set([10,20,30,40])
        mySet = {10,20,30,40} // forma literal, non crea l'insieme vuoto
        mySet = {} // questo on è un insieme vuoto, ma un dizionario vuoto attenzione!!!
        
Un insieme è un oggetto mutabile. Si possono aggiungere e togliere elementi.

Aggiungere:

        mySet.add(50)
        
Creare insiemi immutabili, chiamati **frozenset**:

        mySet = frozenset([10,20,30])
        mySet.add(40) // Python va in errore!!!
        
Verifica di un elemento:

        30 in mySet // restituisce True
        
Intersezione di insiemi:

        mySet = {10,20,30,40}
        mySet2 = {30,40,50,60}
        mySet & mySet2  // ottengo {30,40}

Unione di insiemi: 

        mySet | mySet2 // {10,20,30,40,50,60}
        
Differenza insiemistica:

        mySet - mySet2 // {10,20}
        
Xor, or esclusivo:

        mySet ^ mySet2 // {10,20,50,60}

# Strutture di codice in Python

## Linee di codice e blocchi di codice

Un programma è composta da linee logiche, dove ogni liena logica è composta da una o più linee fisiche.

**inea logica**: quella che vede e riassembla Python.

**Linea fisica**: quella che scriviamo noi nel programma.

Esempio: 2 linee fisiche di codice

        s = 'Python'
        print(s) # commento
        
I commenti però non fanno parte delle linee fisiche. Per Python l'esempio viene tradotto in altrettante 2 linee logiche.

Altro esempio:

        s = 'Python \
            Programming \
            Language'
        print(s)

Qui abbiamo 4 linee fisiche, ma solo 2 linee logiche che interpreta Python!!
Quindi linee logiche possono essere composte da una o più linee fisiche.
Il carattere Back Slash segnala a Python il multi line.

## Blocco di codice

Insieme di linee di codice. Vengono nidificati, creati uno dentro l'altro in forma gerarchica. Python non usa 
delle coppie di parentesi per delimitare i suoi blocchi di codice. Python usa l'**indentazione**!!

## Gli Statement

Una linea fisica di codice è composta da uno statement (istruzione da eseguire).
In Python possiamo scrivere codice sulla stessa riga separando con il punto e virgola, ma questa modalità è fortemente
sconsigliata conviene mantenere sempre gli statement e le linee di codice su linee separate.

### Statement Semplice

Uno statement che non contiene altri statement, rappresenta una sola linea logica di codice.

### Statement Composti

Uno statement che ne contiene altri più semplici, quindi vengono scomposti da Python in una serie di linee logiche.
Ad esempio un test condizionale.

## Lo statement IF

Serve per esecuzioni condizionali del codice. Eseguire test di verità.

Sintassi:

            if espressione:
                suite
            elif espressione:
                suite
            else:
                suite

Forma semplice:

            if x < 10:
                print("<10")

Forma più complessa:

            if x < 10:
                print("<10")
            else:
                print(">10")

Forma completa (a statement composto):

            if x < 10:
                print("<10")
            elif x < 20:
                print(">10 e <20")
            elif x < 30:
                print(">20 e <30")
            else:
                print(">30")
                
## Ciclo While

Statement composto

Sintassi:

        while espressione:
            suite
        else:
            suite

La clausola **else** spesso non è presente.

Esempio (forma comune):

            x = 0;
            while x < 3:
                print(x)
                x += 1
                
Esempio (loop infinito):

            while True:
                x = input("Inserire una stringa")
                if x == 'stop':
                    break
                print(x)
                
Esempio (loop infinito con continue)

            while True:
                x = input("Inserire una stringa")
                if x == 'stop':
                    break
                if x < "b":
                    continue
                print(x)
        
## Statement For

Statement composto, usato per iterare gli elementi delle sequenze, e gli oggetti, purchè questi siano **iterabili**.

Sintassi:
    
            for target in iterator:
                suite
            else:
                suite

Il ciclo termina quando finisce l'iterator. La clausola **else** è facoltativa e poco usato, però si può usare.

Esempio (lista):

            myList = [1,2,3,4]
            for i in myList:
                print(i)
                
Esempio (stringa, anche loro sono delle sequenze, un caratteere per volta):

            myString = 'python'
            for i in myString:
                print(i)
                
Esempio (dizionario)

            myDict = {'a':1,'b':2,'c':3}
            for i in myDict:
                print(i)

Esempio (dizionario stampa i valori e non le chiavi):

            myDict = {'a':1,'b':2,'c':3}
            for i in myDict.values():
                print(i)
                
Esempio (dizionario, stampa le coppie intere):

            myDict = {'a':1,'b':2,'c':3}
            for i in myDict.items():
                print(i)
                
**Nota**

Break e continue si comportano uguali come nel ciclo while.

## La funzione RANGE

Funzione che restituisce un oggetto iterabile, che contiene una sequenza di numeri progressiva.

Sintassi:

        range(start,stop,step)
        
Funziona simile ad uno slice.

Esempio:

            for i in range(10,16,2):
                print(i)
                
- start non è obbligatorio, ma se non espresso si parte da 0.
- stop è obbligatorio metterlo.
- step non è obbligatorio e indica il passo.

### Esercitazione

        lista = list()
        >>> for i in range(10,30,1):
        ...     if i % 2 == 0:
        ...             if i < 25:
        ...                     lista.append(i)
        ...
        >>> print(lista)
        [10, 12, 14, 16, 18, 20, 22, 24]
        
        lista = list()
        >>> for i in range(10,30):
        ...     if (i % 2 == 0) and (i < 25):
        ...                     lista.append(i)
        >>> print(lista)
        [10, 12, 14, 16, 18, 20, 22, 24]
        
## List Comprehension

Produce una lista.

A partire da una lista ne produce un'altra in una sola istruzione, facendo una elaborazione sui dati della lista in origine.

Sintassi:

            [espressione for item in iterable if condition]
            
è contenuta in una coppia di parentesi quadre. Iterable è la lista di origine su cui è eseguita l'iterazione, item è il target.
For e in fanno un loop. Quindi è un ciclo for in che scorre la lista mettendolo in un item. Inoltre viene verificata la condition.
Expression elabora item, per produrre il valore che entra nella lista risultante.

Esempio:
            
            >>> numbers = [1,2,3,4,5,6,7,8,9]
            >>> newList = [n*n for n in numbers if n% 2 == 1]
            >>> newList
            [1, 9, 25, 49, 81]
            
            >>> listaDiNumeri = [10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
            >>> nuovaListaNumeri = [n for n in listaDiNumeri if (n%2==0) and (n<25)]
            >>> nuovaListaNumeri
            [10, 12, 14, 16, 18, 20, 22, 24]
            
## Dict Comprehension

Variante delle list comprehension. L'oggetto finale prodotto è un dizionario.

Sintassi:
        
            {key_exp: val_exp for item in iterable if condition}
            
Parentesi graffe perché son dizionari. L'espressione applicata ad item se la condizione è vera, in questo caso, deve essere scomposta in parte key e parte value.

Esempio:

            a = 'python'
            b = {k: ord(k) for k in a}
            b
            {'p': 112, 'y': 121, ....}
            
Ad ogni iterazione produciamo una key e un value, il value è prodotto da una chiamata alla funzione ord() di Python, che 
ritorna il codice Unicode del carattere. La chiave è il carattere e il valore è quello numerico del carattere.

## Set Comprehension

Terzo tipo di comprehension. Meccanismo utilizzabile per ottenere un nuovo insieme partendo da una lista, oggetto iterabile ecc...

Sintassi:

            {expression for item in iterable if condition}
            
Esempio:

        >>> a = 'doppione'
        >>> c = {k for k in a}
        >>> c
        {'e', 'p', 'd', 'o', 'i', 'n'}
        
L'insieme non consente di avere valori dupicati!!

# Funzioni in Python

Insieme di istruzioni a cui diamo un nome da poter poi richiamare nei programmi. In Python le funzioni sono oggetti.
Oggetti perticolari detti **callable**, cioè chiamabili. Due cose si fanno con una funzione:
- definirla
- chiamarla più volte

## Definire una funzione

        def nome_funzione(lista_parametri):
            suite # insieme di statement della funzione

Parametri: elenco opzionale di nomi racchiusi nelle parentesi tonde e che verranno asseganti ai valori forniti al momento della
chiamata della funzione. Quando sono passati si chiamano poi **argomenti**.
La suite viene eseguita quando la funzione viene chiamata.

## Parametri di una funzione Python

### Parametri Posizionali

        def myFunc(a,b,c):
            print(a,b,c)  
            
### Parametri Keyword

Nel momento della chiamata specifico il nome del parametro e posso usare anche un ordine diverso dei parametri.

Esempio:

                  def myFunc(a,b,c):
                    print(a,b,c)
                    
                  myFunc(c=10,a=20,...)
                  
**Importante**

I posizionali devono precedere sempre i keyword.

### Parametri Opzionali

            identifier = expression
            
Esempio:

            def myFunc(a,b,c=3,d=4):
                print(a,b,c,d)
                
            myFunc(10,20) // Python stampa 10 20 3 4
            
            myFunc(10,20,30,40) // Python stampa 10 20 30 40

### Parametri *args

Vengono esposti sotto forma di una **tupla**.

            def myFunc(*args):
                print(args) // questa funzione riceve un numero variabile di argomenti sotto forma di tupla

            myFunc(1,2,3,4)
            (1,2,3,4) // il risultato è una tupla

**Nota**

Se la funzione possiede dei parametri posizionali, **args** deve essere l'ultimo! Quindi i posizionali, anche qui 
devono venire prima. I parametri args saranno stampati come tupla, gli altri no.

### Parametri **kwargs (keyword args)

Vengono scomposti e ricomposti all'interno di un **dizionario**.

            def myFunc(**kwargs):
                print(kwargs)
        
            
            myFunc(a=1,b=2)
            
            {'a':1,'b':2}
            
# Lo statement RETURN

Tutte le funzioni in Python ritonano sempre un valore in maniera implicita o esplicita.

Return ritorna un valore da un funzione. Può esistere nella suite della funzione e può essere seguito da una espressione.

        def sum(a,b):
            return a + b
            
Se non indico nessuna espressione dopo return, Python ritorna automaticamente un oggetto predefinito che è **None**. Ciò rappresenta
l'assenza di un valore. Non torno un valore in particolare.

        def sum(a,b):
            c = a + b
            
Anche in questo caso, Python ritorna un valore che è sempre **None**. Qui non c'è nemmeno return.

# Chiamare una funzione

Chiamare una funzione in Python:

        function_name(arguments)
        
La presenza delle parentesi tonde denota che è una funzione!! Senza parentesi avrebbe un significato differente!

Gli argomenti sono passati sempre **per riferimento**.

## Tipi immutabili passati alle funzioni (esempio)

            def myFunc(x):
                x = 10
                print(x)
                
            y = 20
            myFunc(y)
            // stampa 10
            print(y)
            // stampa 20, y non cambia, perché y è immutabile!!

## Tipi mutabili passati alle funzioni (esempio dizionario)

            def myFunc(x):
                x['func'] = 10
                
            d = {'a':5}
            myFunc(d)
            print(d)
            // ottengo {'a':5,'func':10}
            
Il dizionario è mutabile e quindi viene alterato il suo contenuto. 

# Funzioni come oggetti

Esempio:

        def sum(x,y):
            print(x + y)
            
        sum(10, 5) # chiamata alla funzione, quando chiamo la funzione con i parametri
        sum # funzione come oggetto           
        type(sum) # ritorna tipo function
        
Le funzioni sono oggetti della classe **function**.

Esempi di uso di funzioni come oggetti:

- funzioni nidificate(definizione di un oggetto all'interno di un altro):

        def outer(x,y):
            def sum(a,b):
                return a + b
                
        print(sum(x,y))
        
        outer(10,5) # ritorna 15
        
- funzione come valore di ritorno:

        def outer(x,y):
            def inner(a,b):
                print(a+b)
            return inner # ritorno la funzione usando solo il suo nome, perché è un oggetto!!
            
La funzione **outer** ritorna un oggetto del tipo function.

- funzioni come parametro:

        def sum(a,b):
            print(a + b)
            
        def myFunc(f,x,y):
            f(x,y)
            
        >>> myFunc(sum, 10, 5) # la funzione myFunc usa il riferimento a sum, fornendogli i parametri.
        
   # Namespace e Scope
   
   **Namaspace**: mappatura che collega nomi ad oggetti. Mantiene distinti i nomi degli oggetti in zone diverse dei programmi.
   
   Una volta che un programma Python va in esecuzione ci sono tanti namespace.
   
   **Scope**: il contesto è un'area di codice precisa, che determina a runtime quale namespace va usato per
   risolvere i nomi degli oggetti.
   
   ## Gerarchia Namespace
   
   - **Local** (livello interno ad una funziona, local namespace, primo livello dei nomi, rimosso quando la funzione ritorna e allocato quando la funzione entra in gioco)
   - **Enclosed** (nomi non definiti in una funzione, ma in una funzione che racchiude quella funzione, vedi funzioni annidate)
   - **Global** (il livello globale consente a Python di accedere a tutti i nomi definiti nel sorgente main Python)
   - **Built-in** (namespace predefinto, a livello più alto, fornito dall'ambiente di runtime di Python, contiene le funzioni predefinte del linguaggio)
   
   ### Local Scope
   
        def sum(x,y):
            print(x + y)
            
   ### Enclosed Scope
   
        def outer(a):
            y = 10
            def inner():
                print(x+y)
            inner()
            
   ### Global Scope
   
         x = 100
         
         def myFunc(y):
            print(x + y)
            
   ### Built In Scope
   
         print('python')
   
# Local e Non Local (alterare il livello dei namespace)

**Variable Hiding**: se una funzione definisce una variabile locale che è definita già ad un livello globale, allora la 
variabile locale **nasconde** la variabile globale!!

Esempio:

        x = 100
        def myFunc():
            x = 20
            print(x)
        >>> myFunc()
            20
        >>> print(x)
            100
            
Per alterare il comportamento standard di Python mettere lo statement **global** seguito dal nome della
variabile globale, quindi non viene creata una variabile locale, ma si usa quella globale.

        x = 100
        def myFunc():
            global x = 20
            print(x)
        >>> myFunc()
            100
        >>> print(x)
            100
            
Per alterare un comportamento enclosed, bisogna usare **nonlocal**, alterando il comportamento di 
una funzione nidificata.

# Function Decorator

**Decoratore**: è una funzione che prende in input un'altra funzione, la decora, la arricchisce di istruzioni, del proprio codice e
poi la ritorna. Serve per alterare il comportamento di una funzione che esiste, senza che noi dobbiamo andare a
modificare il codice di questa funzione.

Esempio (decorare senza decoratore):

        def myFunc():
            print("Hello World!")
            
        >>> myFunc()
        Hello World!

Definire una funzione dentro la definizione di un'altra funzione:

        def myDecorator(f):
            def decorator():
                print("ho decorato")
                f()
                return decorator

        def myFunc():
            print("la funzione myFunc")

Vogliamo prendere in input una funzione, ma in realtà ritornarne un'altra che è **decorator**.

Questa funzione è un decoratore, cioè una funzione che ha aggiunto del codice. Che ha decorato.

        >>> myFunc(myDecorator(myFunc))
        >>> myFunc()
        ho decorato
        la funzione myFunc

Ho quindi decorato la funzione myFunc con il contenuto di un'altra funzione.

Possiamo ottenere lo stesso risultato con una **annotations**.

        def myDecorator(f):
            def decorator():
                print("ho decorato")
                f()
                return decorator

        @myDecorator
        def myFunc():
            print("la funzione myFunc")

Stiamo indicando a Python, che stiamo decorando myFunc(); è una forma più compatta e leggibile.

# Funzioni Lambda

Altro modo di definire delle funzioni, senza usare **def**.

Lambda ritorna delle funzioni anonime, quelle che negli altri linguaggi vengono definite **funzioni anonime**.

        lambda arg1, arg2, .... : expression (argomenti)

Esempio:

        def myFunc(a,b):
            return a**b

        >>> myFunc(2,3)
        8

con Lambda:

        f = lambda a, b: a**b
        >>> f(2,3)
        8

# Object Orientation (Programmazione ad oggetti con Python)

Tutto in Python è un oggetto. Un linguaggio object based, ma non vuol dire che sia per forza object oriented. Un linguaggio object oriented permette di lavorare al 100% con gli oggetti, poter creare le nostre classi e usarle per creare le nostre istanze. Organizzare
le nostre classi in gerarchie, con l'ereditarietà. Questo fa di Python un linguaggio **object oriented** e **object based**.

## Classi ed istanze

2 tipi di oggetti:

- **oggetti classe**: forniscono il comportamento di default, la definizione di attributi e metodi, che servono a produrre le proprie istanze.

- **oggetti istanze**: sono individuali, prodotti dalla definizione degli oggetti classe.

## Lo statement Class

Lettera maiuscola per definire le classi (convenzione).

Statement composto che ha la clausola **class**

        class classname(base-classes): # header
            statements                 # suite
            
Esempio (minimale):
        
        class MyClass:
            pass
            
        >>> type(MyClass)
        <class 'type'> # anche una classe è un oggetto, tutte le volte che creo una classe
                        # creo una istanza della classe type.
                        
### Istanza di una classe

        >>> myObj = MyClass()
        
Crea una istanza della classe MyClass.

## Attributi di una classe

- attributi di classe
- attributi di istanza

### Attrbuti di Classe

Condivisi da tutte le istanze della classe:

        class MyClass:
            myAttr = 10
            
        >>> MyClass.myAttr # per accedere
        10
        
Altro esempio:

        m1 = MyClass()
        m2 = MyClass()
        
        >>> m1.myAttr
        10
        >>> m2.myAttr
        10 
        
**Nota** 

Nel moemento in cui una istanza va a modificare l'attributo di una classe, in realtà modifica solo il suo
e non tocca quello degli altri!

Esempio:

        m1.myAttr = 90
        >>> m2.myAttr
        10
        >>> MyClass.myAttr
        10
        
**Importante**

è sempre possibile anche se sconsigliato aggiungere attributi di una classe anche dopo aver definito 
la classe!

Esempio:

        class MyClass:
            myAttr = 10
            
        my.myAttr2 = 100
        
### Attributi di classe (metodi di istanza)

Anche i metodi definiti nel corpo della classe sono condivisi da tutte le istanze della classe.

I metodi hanno un primo parametro inserito che si chiama **self**, che rappresenta l'istanza specifica
che invoca il metodo.

        class MyClass:
            def myMethod(self):
                print(id(self))
                
        >>> m1 = MyClass()
        >>> m1.myMethod()
        123456789
        
        >>> m2 = MyClass()
        >>> m2.myMethod()
        23432123

**Importante**
        
myMethod è condiviso da tutte le istanze e infatti quando lo richiamiamo sulle istanze restituisce 
valori diversi. Manca il parametro **self** che non compare, eppure era scritto nel metodo. Questo
perché quando usiamo la dot notation per chiamare un metodo di una classe su una istanza, viene passato
direttamente l'argomento implicito del metodo che è proprio **self**. Non ci dobbiamo ricordare di passare
self, lo fa Python per noi, come il **this** per Java.

Passare parametri diversi da self:

        class MyClass:
            def myMethod(self, message):
                print(message)
                
        >>> m1.myMethod('Python')
        Python
        
## Attributi di istanza

        class MyClass:
            def setMessage(self, message):
                self.message = message
            def printMessage(self):
                print(self.message)
                
In questo caso **message** diventa un attributo di istanza e non di classe! Quindi quando lo richiamo 
su di una istanza lo esprimo così:

        >>> m1 = MyClass()
        >>> m2 = MyClass()
        >>> m1.setMessage('test message')
        >>> m2.setMessage('primo')
        >>> m1.printMessage()
        test message
        >>> m2.printMessage()
        primo

**Attenzione**

Se definisco il codice così:

        >>> m3 = MyClass()
        >>> m3.printMessage()
        ERRORE!!!!
        
Ottengo un errore perché non ho ancora definito il metodo **printMessage()** per quella istanza, per rimediare
a questo che è un problema **strutturale** Python introduce il metodo **__init__**, il costruttore.

# Il metodo init

Init è un metodo di istanza, che permette di costruire le istanze di una classe.

Viene chiamato sempre appena una istanza di una classe viene creata. Costruisce le istanze di una
classe e prende come parametro sempre **self**.

Init viene richiamato sempre da Python a runtime.

Riscriviamo la classe MyClass, introducendo il metodo init.

        class MyClass:
            def __init__(self, message):
                self.message = message
            def printMessage(self):
                print(self.message)
            
        >>> m1 = MyClass()
        
        Se scrivo questo ottengo un errore perché Python si aspetta il message, perché lo definito
        nel suo costruttore della classe MyClass.
        
Soluzione:

        >>> m1 = MyClass('primo')
        >>> m1.printMessage()
        primo
        
# Metodi di classe

Metodi non pensati per essere usati sulle singole istanze, ma direttamente sull'oggetto classe.

        class MyClass():
            def counter = 0
            def __init__(self):
                MyClass.counter += 1
                
            @classmethod
            def istanze(cls):
                print(cls.counter)
                
Counter è un attributo di classe. Init usa l'attributo di classe. Inoltre il decoratore **@classmethod** 
indica a Python che istanze() è un metodo di classe, pensato per essere invocato sulla classe stessa.
**Cls** per convenzione indica l'oggetto classe, non le istanze come self.

Esempio:

            >>> m1 = MyClass()
            >>> m2 = MyClass()
            >>> m3 = MyClass()
            >>> MyClass.istanze()
            3
            
## Metodi Statici

Si definiscono usando un altro tipo di decoratore: **@staticmethod**

Esempio:

        class MyClass():
            @staticmethod
            def somma(a,b):
                return a + b


        >>> s = MyClass.somma(10,5)
        >>> print(s)
        15

**Importante**

Il metodo statico fornisce un servizio minimale, che non contiene nè cls, nè self, non ci sono parametri
 particolari, ha il solo scopo di essere inserito nella classe e essere invocato in quel punto. I metodi 
 statici non vengono usati molto frequentemente.
 
 # Ereditarietà (Inheritance)
 
 Python lo consente, sia dalle classi alle istanze, che dalle classi alle classi.
 
 Le sottoclassi ereditano gli attributi dalle proprie superclassi, possono ridefinirli (override) e aggiungerne di nuovi.
 
        class BClass:
            pass
            
        class AClass(BClass):
            pass
            
 Passiamo la classe da ereditare tra le parentesi!! AClass è sottoclasse di BClass. Se una classe eredita 
 da più di una classe allora:
 
        class AClass(BClass, DClass, CClass):
            ...
            
## Funzione isinstance()

Funzione di utilità, che serve a gestire informazione di utilità su una classe, consente di verificare 
se un oggetto è istanza di una classe. Come instanceof di Java.

        >>> m1 = AClass() 
        >>> isinstance(m1, AClass)
        True
        >>> isinstance(m1, BClass)
        True
        >>> isinstance(m1, DClass)
        True
        ...
        
Una classe quando eredita eredita anche tutte le istanze, una istanza ereditata è anche di quella 
classe!

# Override

Modo in cui ridefiniamo un attributo all'interno di una sottoclasse. Ridefiniamo un attributo di una superclasse, 
dentro una sottoclasse.

Esempio:

        class BClass:
            def setMessage(self, message):
                self.message = message
            def printMessage(self):
                print(self.message)
                
        def AClass(BClass):
            def printMessage(self):
                print("A Class " + slef.message)
                
Abbiamo ridefinito il comportamento del metodo **printMessage()**

**Importante**

Se inserisco un costruttore in una sottoclasse bypasso il costruttore delle superclassi, un modo per mantenerli è 
usare la clausola **super**.

# La funzione SUPER

Funzione predefinita del sistema, che ci permette di:

Richiedere in modo esplicito in una sottoclasse, l'esecuzione del costruttore della superclasse.

Esempio:

        class BClass:
            def __init__(self, message):
                self.message = message
            def printMessage(self):
                print(self.message)
                
        class AClass:
            def __init__(self, message, valore):
                super().__init__(message)
                self.valore = valore
                
Super chiamata in __init__ ottiene come valore di ritorno, quello della superclasse. Stiamo eseguendo
di fatto il costruttore di BClass. Dopo proseguiamo con il costruttore di AClass e aggiungiamo un 
secondo attributo specifico solo di AClass.

        >>> m1 = AClass('python', 20)
        >>> m1.valore
        20
        >>> m1.printMessage()
        python
        
Super lo possiamo usare anche per ereditare e overridare metodi delle sopraclassi nelle rispettive sottoclassi.

# Properties

## Information Hiding

Tipico dei linguaggi ad Oggetti. **Nascondere l'informazione**, rendere privati gli attributi che 
presentano dati cui non si può accedere dall'esterno, ma si può solo accedere tramite metodi 
getter/setter. E' buona norma nascondere questi attributi, per cambiarne poi la forma. I metodi
per l'accesso agli attributi restano coerenti.

Python non ha un vero e proprio supporto agli attrinuti privati, ma lo può fare attraverso le **Properties**.

### Definizione di una Property

Esempio:

        class MyClass():
            def __init__(self, my_attr):
                self.priv_attr = my_attr
            def get_attr(self):
                return self.priv_attr
            def set_attr(self, attr):
                self.priv_attr = attr
                
            attr = property(get_attr, set_attr)
            
            >>> obj = MyClass('Python')
            >>> obj.attr
            Python
            >>> obj.attr = 'Prova'
            >>> obj.attr
            Prova
            
Nessuno però ci impedisce di accedere direttamente ai metodi nascosti, Python non li nasconde del tutto:

            >>> obj.set_attr('python')
            >>> obj.get_attr()
            prova
            
C'è una soluzione al problema, scrivendo l'attributo da nascodere con 2 underscore! In questo modo nascondo un attributo. Lo 
rendo inaccessibile all'esterno della classe.

            class MyClass():
                
                def __init__(self, my_attr):
                    self.__priv_attr = my_attr
                
                def get_attr(self):
                    return self.__priv_attr
            
                def set_attr(self, attr):
                    self.__priv_attr = attr
                
                attr = property(get_attr, set_attr)
                
            >>> obj = MyClass('Python')
            
            >>> obj.__priv_attr
            
            Errore AttributeError!!!
            
Python dice che l'attributo non esiste, in realtà non è vero. Python non rende privato il nostro 
attributo, ne ha storpiato il nome (**Name Mangling**), l'attributo resta accessibile, passando da qui

            >>> obj._MyClass__priv_attr
            Python
 
In questo modo Python realizza l'information hiding.

# Property Decorators

Con i decoratori, si ottiene lo stesso risultato esposto sopra:

            @property (decorator del metodo getter)
            
            @name.setter (decorator del metodo setter)
            
Esempio:

            class MyClass():
                
                def __init__(self, my_attr):
                    self.__priv_attr = my_attr
                
                @property
                def attr(self):
                    return self.__priv_attr
            
                @attr.setter
                def attr(self, attr):
                    self.__priv_attr = attr
              
Definiamo 2 metodi che si chiamano nello stesso modo, ma sono diversi nella composizione dei parametri.

Se usiamo questi 2 decorators, noi stiamo dichiarando a Python, che stiamo introducendo una proprietà e 
gli diciamo quale è il metodo setter e quello getter. L'utilizzo è identico a quello soproa esposto:

                 >>> obj = MyClass('python')   
                 >>> obj.attr
                 python
                 
# Esercitazione Object Oriented

La classe Conto Corrente.

## Prima versione del progetto

        class ContoCorrente:
            # inizializzatore
            def __init__(self, nome, conto, importo):
                self.nome = nome
                self.conto = conto
                self.saldo = importo
            # prelievo
            def preleva(self, importo):
                self.saldo -= importo
                print("\nHai prelevato dal conto: " + str(importo))
            # deposito
            def deposita(self, importo):
                self.saldo += importo
                print("\nHai depositato sul conto: " + str(importo))
            # stampa
            def descrizione(self):
                print("\nIntestatario del conto: " + str(self.nome))
                print("Conto Corrente: " + str(self.conto))
                print("Saldo Conto: " + str(self.saldo))

## Seconda versione del progetto (nascondiamo attributo saldo all'esterno)

Usando i property decorators.

        class ContoCorrente:
        # inizializzatore
            def __init__(self, nome, conto, importo):
                self.nome = nome
                self.conto = conto
                self.__priv_saldo = importo

            # getter
            @property
            def saldo(self):
                print("sono dentro getter")
                    return self.__priv_saldo

            # setter
            @saldo.setter
            def saldo(self, importo):
                print("sono dentro setter")
                self.preleva(self.__priv_saldo)
                self.deposita(importo)

            # prelievo
            def preleva(self, importo):
                self.__priv_saldo -= importo
                print("\nHai prelevato dal conto: " + str(importo))

            # deposito
            def deposita(self, importo):
                self.__priv_saldo += importo
                print("\nHai depositato sul conto: " + str(importo))

            # stampa
            def descrizione(self):
                print("\nIntestatario del conto: " + str(self.nome))
                print("Conto Corrente: " + str(self.conto))
                print("Saldo Conto: " + str(self.__priv_saldo))

        # testing

        c1 = ContoCorrente('Roberto', '123456', 1000)
        c1.descrizione()
        c1.saldo = 1000000
        print(c1.saldo)
        
## Terza Versione del progetto (la superclasse Conto)

Modifiche sostanziali alla classe ContoCorrente:

        class Conto:
            def __init__(self, nome, conto):
                self.nome = nome
                self.conto = conto

        class ContoCorrente(Conto):
            # inizializzatore
            def __init__(self, nome, conto, importo):
                # dalla superclasse
                super().__init__(nome, conto)
                self.__priv_saldo = importo
                
Il resto del codice non cambia rispetto alla seconda versione.
                
# Quarta versione del progetto (la classe Gestione di conti correnti)

        class GestoreContiCorrenti():
            @staticmethod
            def bonifico(sorgente, destinazione, importo):
                print("\nEffettua un bonifico di € " + str(importo))
                sorgente.preleva(importo)
                destinazione.deposita(importo)

# Eccezioni in Python

Le eccezioni comunicano e gestiscono gli errori e le anomalie che si verificano nell'esecuzione dei programmi. 
Le eccezioni sono oggetti in Python. Possiamo crearne di nostre personali.

        def myFunc(a,b):
            return a // b
            
Se passo 0 a questa funzione si genera un errore, si dice che si solleva una eccezione! Python in terrompe l'esecuzione del programma anche perché nessuno gli ha 
detto come gestire questa eccezione.
Praticamente se l'eccezione non viene gestita Python risale sempre più verso l'alto nella pila dello stack fino a quando viene interrotto il programma.

Le eccezioni sono oggetti. Tutte le eccezioni sono istanze di classi che sono sottoclassi di **BaseException**. Nel nostro esempio
abbiamo una eccezione **ZeroDivisionError** che è sottoclasse di **ArithmeticError** che a sua volta è una sottoclasse di **Exception** che a sua volta
è sottoclasse di **BaseException**. BaseException non deriva da nessuno e quindi implicitamente deriva di **object**.

## Lo Statement try/except

        try:
            suite
        except:
            suite
            
è uno statement composto. Se si verifica una eccezione il flusso del programma si sposta all'interno della clausola **except**.

Scriviamo un blocco di codice che vogliamo sorvegliare all'interno della clausola **try**, se viene sollevata l'eccezione, il programma
non risale verso l'alto, non si interrompe e gestisce l'eccezione nel blocco **except**.

Esempio:

        def myFunc(a,b):
            return a // b
            
        try:
            c = myFunc(4,0)
        except:
            print("Errore")
            
Il corpo della clausola **except** viene chiamato in Python **Exception Handler**.

Esempio:

        try:
            suite
        except:
            suite
        except:
            suite
            
Più precisione:

        try:
            c = myFunc(4,0)
        except ZeroDivisionError:
            print("Errore")
        except IndexError:
            print("Errore")
            
Alternativa:

        try:
            c = myFunc(4,0)
        except (ZeroDivisionError, ValueError): // se si verifica almeno una delle due eccezioni
            print("Errore")

## Lo statement try/except/as

**as** permette di assegnare un valore all'eccezione in modo da richiamarlo dentro la suite di except.

        try:
            suite
        except expression as target:
            suite
            
Perché? In questo modo posso richiamare il nome dell'eccezione quando la invoco.

        try:
            c = myFunc(4,0)
        except ZeroDivisionError as e:
            print(e.args)
            
## Le clausole finally ed else

**finally** assicura di esguire sempre le azioni dentro la sua suite, sia che venga sollevata o meno una eccezione. Anche se ci 
fosse except Python esegue comunque la finally.

Esempio:

        try:
            c = myFunc(4,0)
        except ZeroDivisionError as e:
            print(e.args)
        finally:
            print("Finally")
            
**else** si deve inserire solo dopo tutte le clausole except, quindi al fondo. Viene eseguita soltanto se non vengono 
sollevate nessuna delle eccezioni associate al try.

        try:
            suite
        except:
            suite
        else:
            suite        

**IMPORTANTE**

Finally ed else non sono mutuamente esclusive, si possono usare insieme, solo che finally deve essere messa dopo else!

## Gli statement Raise ed Assert

**Raise**: si usa per sollevare esplicitmanete una eccezione. Di solito è Python che solleva le eccezioni. Anche noi possiamo creare e sollevare eccezioni
nei nostri programmmi.

        raise exception # exception può essere una Classe di eccezione o una isanza di eccezione
        
Esempio:

        for i in range(50):
            print(i)
            raise IndexError # sollevo la classe di Eccezione
            
Così Python esce dal programma mostrandoci la classe di Eccezione e risalendo lo stack.

        for i in range(50):
            print(i)
            raise IndexError("Errore nel loop") # così ho creato una istanza di eccezione
            
Così Python mostra un messaggio di errore.

Se uso solo **raise** senza niente va bene se voglio risollevare una eccezione che avevo già trattato in precedenza:

Esempio:

        try:
            c = f(4,0)
        except ZeroDivisionError:
            print("Errore!")
            raise

All'interno di except viene intercettata l'eccezione, non conclude, ma bensì risolleva l'eccezione ZeroDivisionError, quindi raise risolleva l'eccezione.

**Assert**: valuta una espressione per vedere se la valutazione dell'espressione è vera o false.
Se falsa, viene sollevata una eccezione AssertionError.

        assert expression, argument
        
Esempio:

        x = 10
        
        assert x == 5, "Valori diversi" # AssertionError con argomento "Valori diversi"
        
# Moduli e Package

è il livello più alto possibile dell'organizzazione del codice in Python. I moduli sono i veri e propri programmi in Python.

## Moduli

Unità più alta a livello di organizzazione di un programma in Python, un modulo contiene la definizione di codice e di dati, funzioni, classi...

Sono predisposti in modo da poter essere usati altrove. Un modulo genera una **spazio di nomi**. I moduli sono a livello Global.

Due moduli diversi anche se contengono nomi di classi uguali vengono considerati attributi diversi perché appartengono a moduli diversi.

Di solito in Python c'è uno **script** principale e poi i **moduli** che fannno da libreria:

        script1.py
        module2.py
        module3.py ecc...
        
I moduli in generale sono considerati come **librerie di oggetti e classi**. Possono essere riutilizzati
tramite **importazione** nello script principale.

        import module2
        import module3
        
        obj = module2.myFunc(x) # per usare una funzione di module2 dentro lo script principale!!
        
        module2.myFunc(x) # per usare una funzione di module2 importata
        
## Importazione di un modulo

        import modulo1
        
Nome del file privo del suffisso **py**.

Fasi dell'importazione di un moduo in Python:

- individuazione del modulo
- compilazione bytecode del modulo
- esecuzione del modulo

### Modalità di ricerca di un modulo

Priorità nella ricerca:

Python guarda la directory corrente se contiene il modulo da importare, se non lo trova li dentro va a vedere le directory
di una variabile di ambiente **PYTHONPATH**, se non è settata allora si prosegue la ricerca nella libreria standard di Python, che
contiene molti moduli e infine come ultima possibilità si ricerca nella directory **site-packages**, che contiene framework o moduli
di terze parti.

### Traduzione in Bytecode

I moduli, ma non gli script che devono essere importati producono, la prima volta un bytecode, viene fatto per risparmiare
tempo dopo. Vale solo per i moduli importati. E' il nome del modulo originario più estensione **pyc**.

        modulo.py
        
        modulo.cpython-36.pyc
        
Sono archiviati dentro la **__pycache__**

## Lo statement IMPORT

Come si usa:

        import modulo1

se chiediamo a Python cosa sia il modulo importato, Python ci dice che modulo è un oggetto e una 
istanza della classe **module**.

Quindi tutti gli oggetti definiti dentro il modulo che importiamo saranno attributi dell'oggetto module. Si può accedere
soltanto a questi.

Dentro script.py:

        import module1
        
        module1.myFunc(10) # uso la funzione del modulo importato!!!
        
Dentro module1.py:

        def myFunc(x):
            print(x)
            
Si possono indicare più moduli con una sola import:

        import module1, module2, ....
        
        import module1
        import module2
        ....
        
Definire un **alias** per accorciare il nome del modulo:

        import module1 as m
        
        m.myFunc(x) 
        
## Lo statement FROM

Si vogliono importare solo alcuni attributi da un modulo:

Es.

        from modulo1 import myFunc()
        
        >>> myFundc(20)
        20
        
Quindi usiamo la parola chiave **from** seguita dal nome del modulo, poi la parola chiave
**import** seguita dal nome dell'attributo che vogliamo importare. Importa solo ciò che io richiedo e 
inoltre possiamo accedere direttamente all'attributo con il suo nome senza anteporre la **dot notations**, Python
lo risolve attraverso lo statement from.

Esiste inoltre la possibilità di importare con la clausola **star**, cioè usando
l'operatore asterisco non per importare l'intero modulo, ma tutti gli attributi del modulo singolarmente:

Es.

        from modulo1 import *
        
        >>>myFunc(20)
        20
        
Vengono importati tutti gli attributi e poi usati con il loro nome, **questa pratica è
fortemente sconsigliata** anche se possbili in Python!!

Possiamo usare ancora insieme a from e import anche lo statement **as**:

Es.

        from modulo1 import myFunc() as f1
        from modulo2 import myFunc() as f3
        from modulo3 import myFunc() as f4
        
        >>>f1(20)
        20
        
Può servire per eseguire la **disambiguazione** degli attributi! Una sorta di ridenomina, sfruttando
le funzionalità dell'alias as. Attributi con lo stesso nome all'interno dello stesso modulo
non vanno in conflitto di nomi, ma se vengono importati tutti insieme fuori dallo stesso 
modulo si possono distinguere così.

## L'attributo __name__ attributo predefinito dei moduli Python (eseguire modulo come script)

A volte può essere utile eseguire un modulo di libreria direttamente dalla linea di comando.

Tutti i moduli in Python possiedono un attributo chiamato:

        __name__
        
        modulo1.__name__
        
Come funziona?

A runtime Python di default assegna il nome del modulo all'attributo name, quindi
il valore di name è **il nome del modulo**: nel nostro caso modulo1.

Però se il modulo viene eseguito in uno script il suo nome specifico non è il suo nome,
bensì:

        __main__
        
perché diventa lo **script principale**.

Come trasformiamo un modulo che può essere importato anche in uno script?

Possiamo fare un controllo condizionale di questo tipo:

        def myFunc(x):
            print(x)
            
        if __name__ == '__main__':
            myFunc(150)

## I Package

Un modulo è un file che contiene del codice Python. Python consente di strutturare questi moduli.
Una directory che contiene un insieme di moduli è un **package**. Questo può contenere una struttura gerarchica, quindi
possono essere inseriti all'interno di alberi di directory, che ne loro complesso diventano un package.


Come si usano?

Es.

        Immaginiamo di inserire modulo1 e modulo2 all'interno di una cartella dir_c
        
        dir_c è a sua volta una sottocartella di dir_b
        
        Se inseriamo dentro queste due cartelle un file __init__.py, Python considera
        queste due cartelle un package
        
        La presenza di questo file in entrambe le cartelle è obbligatoria se vogliamo
        rendere questa struttura gerarchica un package.
        
        A sua volta questa struttura deve essere contenuta dentro una directory
        che chiamiamo dir_a presente nel module serach path.
  
        dir_a è la radice (non fa parte del package e non ha il file __init__.py)
        però Python è in grado di risolvere per capire dove importare il nostro package
        
        Come si importa un package?
        
        Si importano come i moduli, ma si separano con il punto terminando con il nome del
        modulo del package che si vuole importare
        
        Es.
        
                import dir_b.dir_c.modulo1
                
                from dir_b.dir_c import modulo1
                
# Advanced Python
        
## Multiple Inheritance

Python supporta il concetto di ereditarietà, estendiamo ancora il concetto attraverso
 l'ereditarietà multipla, cioè derivare una sottoclasse da più superclassi.
 
Ripasso **ereditarietà singola**:

Es. 

        class BClass:
            pass
            
        class AClass(BClass):
            pass
            
AClass deriva da BClass, AClass deriva da BClass, in questo caso parliamo di ereditarietà 
singola.

Es.

        class SuperClasse:
            a = 10

        class SottoClasse(SuperClasse):
            print("Sono la SottoClasse e stampo a che ho ereditato da SuperClasse => ", SuperClasse.a)

        prova = SottoClasse()
        print("Sono la SottoClasse, ho creato una istanza prova e richiamo a  ==> ", prova.a)

Python ci permette anche l'**ereditarietà multipla** in questo modo:

Es.

        class BClass:
            b = 10
            
        class CClass:
            c = 20
            
        class AClass(BClass,CClass):
            pass
            
Le classi da cui ereditare vanno passate tutte quante nella firma iniziale della classe, che è la 
sottoclasse.

Se definiamo una istanza di AClass, possiamo accedere ai due attributi presenti nelle
 due superclassi BClass e CClass:
 
Es.

        a = AClass()
        print(a.b) # 10
        print(a.c) # 20
        
Es. 

        class BClass:
            def funcBClass(self):
                print("Sono un metodo di BClass")


        class CClass:
            def funcCClass(self):
                print("Son un metodo di CClass")


        class AClass(BClass, CClass):
            pass


        istanzaAClass = AClass()
        istanzaAClass.funcBClass()
        istanzaAClass.funcCClass()
        
**Importante**

Che cosa succede se entrambi le superclassi definiscono lo stesso attributo, la stessa funzione?
Quale delle implementazioni verrà scelta? Potrebbe generare un errore?

Es.

        class BClass:
            def funcBClass(self):
                print("Sono un metodo di BClass")
            def xFunc(self):
                print("Sono xFunc di BClass")

        class CClass:
            def funcCClass(self):
                print("Son un metodo di CClass")
            def xFunc(self):
                print("Sono xFunc di CClass")

        class AClass(BClass, CClass):
            pass


        istanzaAClass = AClass()
        istanzaAClass.funcBClass()
        istanzaAClass.funcCClass()
        istanzaAClass.xFunc() 
        
## Method Resolution Order

è la risposta alla problematica esposta sopra. Viene abbreviato con un sigla 
**MRO** ed è la regola che usa Python per eseguire situazioni di ereditarietà multipla di 
classi che hanno nomi di metodi o attrbuti identici.

Come funziona MRO?

- prima di tutto l'attributo viene ricercato nella sottoclasse stessa, perché potrebbe 
essere ridefinito li dentro, se viene trovato li dentro viene direttamente utilizzato.
- se l'attributo non viene trovato nella sottoclasse allora il meccanismo di MRO risale di un 
livello nella gerarchia delle Superclassi e va a cerca l'attributo nell'ordine in cui ho definito 
le sopraclassi nella firma della sottoclasse, nel nostro caso (BClass, CClass) ecco perché viene 
selezionato il metodo di xFunc() di BClass e non quello di CClass. La ricerca quindi si interrompe una 
volta trovato l'attributo di riferimento. Se non l'avesse trovato in BClass, lo avrebbe cercato in CClass.
Voendo poteva salire a livelli di gerarchie superiori seguendo sempre un ragionamento da sinistra verso destra.

Es. definizione a più livelli di ereditarietà, meccanismo MRO


        class DClass:
            def xFunc(self):
                print("Sono metodo xFunc definito dentro DClass")


        class BClass(DClass):
            pass


        class CClass:
            pass


        class AClass(CClass, BClass):
            pass


        a = AClass()
        a.xFunc()

Se nemmeno in DClass ci fosse la definizione di xFunc, allora riceviamo da Python 
una eccezione **Attribute Error**, però attenzione potrebbe essere contenuto nella 
superclasse Object, la più generale di tutte!! Ricordiamoci che Python quando dichiariamo 
una nuova classe in realtà fa questo ragionamento:

Es.

        class MiaClasse:
            pass
            
ma è come se fosse in realtà:

        class MiaClasse(object):
            pass
            
## La classe object e type

Sono classi **sorelle**. Sono situate entrambe in cima alla gerarchia delle classi Python.

In Python tutto è oggetto anche le classi.

**object** è classe base in Python e tutti gli oggetti in Python sono istanze di object.
Quindi se faccio:

        class MyClass:
            pass
          
        myInstace = MyClass()
        
            
- **MyClass**, che è una classe, è anche una **istanza di object** (is a)!!
- **myInstance** è una istanza di MyClass, questo è sicuro, però siccome tutti gli oggetti 
sono istanze di object, allora anche myInstance è un oggetto di object!! Come del resto tutti
gli oggetti in Python.

Adesso spendiamo due parole per la classe **type**: è una classe che contiene come istanze 
solo come istanze **solo degli oggetti che sono a loro volta delle classi**!!!
Quindi le nostre classi, i dizionari, tutti i type, sono istanze di type!!
- **MyClass** è quindi una istanza della classe type
- **myInstance** non è una istanza della classe type, myInstance non è una classe!

### Rapporto che sussiste tra object e type

- object è una classe, ma anche un oggetto e questo vuol dire che **object è una istanza di object**, 
una istanza di se stessa.
- object è anche una classe e quindi **è anche istanza della classe type**

- type è una classe e anche un oggetto, quindi è una istanza di object
- in quanto type è una classe è anche una istanza di se stessa, quindi è una istanza di type!!

### Esercitazione

        >>> class MyClass:
	            pass
        >>> myObj = MyClass()
        >>> isinstance(myObj,MyClass)
        True
        >>> isinstance(MyClass,object)
        True
        >>> isinstance(myObj,object)
        True
        >>> isinstance(MyClass,type)
        True
        >>> isinstance(myObj,type)
        False
        >>> isinstance(object,object)
        True
        >>> isinstance(type,type)
        True
        >>> isinstance(type,object)
        True
        >>> isinstance(object,type)
        True
        
## Il costruttore __new__

**Init**

è un metodo usato durante la fase di costruzione di un oggetto. L'abbiamo chiamato 
costruttore di un oggetto, ma in realtà lo inizializza soltanto, non è un costruttore di una 
istanza, nè è soltanto l'inizializzatore, come dice il suo nome stesso. Il vero costruttore 
si chiama **new** in Python, è new che fabbrica l'istanza di una classe.
Init la inizializza una volta che però è già stata costruita.

Prima viene invocato **new** e poi dopo **init**

Es.

        __new__(cls [...])
        
new è un metodo statico, ma non è necessario decorarlo con **static**.

Andiamo con ordine:

Es.
        
        class MyClass():
            def __new__(cls):
                print("istanza creata")
            def __init__(self):
                print("istanza inizializzata")
                
        mc = MyClass()
        
Il metodo **new** viene chiamato, mentre **init** no.
Vedremo:

        >>> istanza creata
        
Questo perché **dobbiamo creare una istanza e ritornarla**.

        class MyClass():
            def __new__(cls):
                istanza = super.__new__(cls) 
                print("istanza creata")
                return istanza
            ...
            
Qui risaliamo fino alla classe object, con super e lasciamo a object il compito di creare l'instanza.
A questo punto, siccome ritorniamo l'istanza creata, il flusso del programma prosegue e 
verrà stampata anche "istanza inizializzata", che prima veniva ignorata.

Es.

        class MyClass:
            def __new__(cls, message):
                istanza = super(MyClass, cls).__new__(cls)
                print("++++ Creata istanza e ritorno ++++")
                return istanza

            def __init__(self, message):
                self.message = message
                print("++++ Sono in INIT ++++")
                print(self.message)


        mc = MyClass("Python")

        class MyClassSenzaMessage:
            def __new__(cls):
                istanza = super(MyClassSenzaMessage, cls).__new__(cls)
                return istanza

            def __init__(self):
                print("Init senza message")


        mcsm = MyClassSenzaMessage()
        

## Iterabili e iteratori

Piccola digressione su cosa erano i **Contenitori** in Python:

supponiamo una **lista** (che è un contenitore)

        >>> ls = [1,2,3,4,5,6,7]
        >>> e = 3 in ls
        >>> e
        True
        
Un contenitore è anche un **oggetto iterabile**. Non tutti gli iterabili però 
sono contenitori, un file ad esempio non lo è.

### Iterabile

Quando è un oggetto (iterabile) in grado di ritornare un altro oggetto (l'iteratore) che 
consente di eseguire una **iterazione sugli oggetti dell'oggetto di partenza**.

Per fare questo si chiama un metodo **__iter__**, che ritorna gli oggetti, 
dentro l'oggetto.

        __iter()__
        
### Iteratore

è un oggetto che produce il prossimo elemento di un iterabile, attraverso il 
metodo **next()**


        __next()__
        
**Ricorda**

Un solo oggetto può essere sia iterabile che iteratore. In questo caso un iteratore di se stesso.

Es.

        la lista
        
        >>> myList = ["primo", "secondo", "terzo"]
        >>> it1 = iter(myList)
        >>> type(myList)
        <class 'list'>
        >>> type(it1)
        <class 'list_iterator'>
        >>> next(it1)
        'primo'
        >>> next(it1)
        'secondo'
        >>> next(it1)
        'terzo'
        >>> next(it1)
        Traceback (most recent call last):
        File "<pyshell#10>", line 1, in <module>
            next(it1)
        StopIteration
        >>> for e in myList:
	        print(e)

        primo
        secondo
        terzo

Quando eseguo un for l'eccezione StopIteration
 è gestita da Python stesso.
 
### Creazione di un iteratore (un oggetto iterabile)

Es.

        # un iteratore ha sempre metodo iter e metodo next

        class MyIterator:
            def __iter__(self):
                self.myattr = 2
                return self

            def __next__(self):
                if self.myattr < 300:
                    n = self.myattr
                    self.myattr *= 2
                    return n
                else:
                    raise StopIteration


        iteratore = MyIterator()
        testIter = iter(iteratore)

        # usando print se ne metto ancora una ottengo l'eccezione StopIteration
        print(next(testIter))
        print(next(testIter))
        print(next(testIter))
        print(next(testIter))
        print(next(testIter))
        print(next(testIter))
        print(next(testIter))
        print(next(testIter))

        # con il for l'eccezione è controllata e non si presenta
        for i in testIter:
            print(i)
            
## Generator Functions

Normale funzione python, ma con una particolarità: se all'interno della funzione compare
la parola chiave **yield** (cedere) allora l'intera funzione viene trasformata automaticamente
in un iteratore e l'iterazione avviene nel punto in cui compare yield. Se viene poi invocata nuovamente 
riparte dall'istruzione successiva alla yield.

Es.
           
        def get_doppio_gen():
           e = 2
            while (e < 300):
                yield e # e contiene valore dell'iterazione
                e *= 2
                
        gen = get_doppio_gen()
        print(gen)
        print(next(gen))  # 2
        print(next(gen))  # 4
        
Quando produciamo una funzione generatore Python dietro le quinte produce un oggetto analogo
ad un iteratore. Questo vuol dire che quando chiamo **next(gen)** vuol dire in realtà che sto facendo 
una chiamata al metodo speciale next esattamente come nel caso di un normale iteratore: posso verificarlo 
in questo modo:

        print(gen.__next__()) # produrrà lo stesso identico risultato di print(next(gen))

Esempio completo:

        def get_doppio_gen():
            e = 2
            while (e < 300):
                yield e
                e *= 2


        testgen = get_doppio_gen()
        print(testgen)
        print(next(testgen))
        print(next(testgen))
        print(next(testgen))
        print(next(testgen))
        print(next(testgen))
        print(next(testgen))
        print(next(testgen))
        print(next(testgen))

        testgen2 = get_doppio_gen()
        print(testgen2)
        print(testgen2.__next__())
        print(testgen2.__next__())
        print(testgen2.__next__())
        print(testgen2.__next__())
        print(testgen2.__next__())
        print(testgen2.__next__())
        print(testgen2.__next__())  
        print(testgen2.__next__())

### return nelle Generator Functions

All'interno di una funzione generatore possiamo usare anche l'espressione **return** per
interrompere l'iterazione, per fermarla. Se lo facciamo viene sollevata una StopIteration.
Proviamo a riscrivere la funzione nel nuovo modo usando return:


        def get_doppio_gen2():
            e = 2
            while (True):
                yield e
                e *= 2
                if (e >= 300):
                    return


        testgen3 = get_doppio_gen2()
        for el in testgen3:
            print(el)

## Generator Expression

è equivalente ad una List Comprehension

Es. (list comprehension)


        numbers = [1,2,3,4,5,6,7,8,9,10,11,12]
        newlist = [n * n for n in numbers if n % 2 == 1]
        print(newlist)
        
        >>> [1, 9, 25, 49, 81, 121]
        
## Dizionari (aggiunte python 3.7)

Python fino alla versione 3.6 non garantiva l'ordinamento delle chiavi, dalla versione 3.7
lo garantiscono.

Esempio:
        
        >>> myDict = { "primo": 10, "secondo": 20, "terzo": 30}
        
        >>> myDict["quarto"] = 40
        
        >>> print(myDict)
        
        {'primo': 10, 'secondo': 20, 'terzo': 30, 'quarto': 40} 

La vera novità di Python 3.7 sta nel fatto che invocando il metodo **keys()** vengono 
restituite le chiavi in ordine del dizionario, l'ordinamento viene preservato. 

Esempio:

        >>> myDict.keys()
        
        dict_keys(['primo', 'secondo', 'terzo', 'quarto'])
        
## Le type annotations (python 3.7)

In realtà sono le **Data Classes** la vera novità di Python 3.7, ma per comprendere le data classes, 
prima dobbiamo fare un passo indietro e parlare delle **Type Annotations** e della loro storia
attraverso documenti della community chiamati **PEP**.

Le type annotations esistono già in versioni precedenti alla 3.7

### PEP (python enhancement proposal)

Documento sottoposto alla comunità di python, dove qualcuno sottopone nuove caratteristiche del 
linguaggio da approvare previa decisione della community.

La PEP 3107 riguarda l'adozione delle annotazioni, risale alla versione 3.0 del python.

**Annotazione:** in Python è una qualsiasi espressione valida del linguaggio che segue
il crattere due punti.

Esempio:

        def foo(a: expression, b: expression = 5):
        
        def sum() -> expression:
        
        def myFunc(x: "parametro x") -> "ritorno":
            return x
            
        print(myFunc.__annotations__)
        
        {'x': 'parametro x, return': 'ritorno'}
        
La PEP 484 (Python 3.5 2014) Type Hints

Usa la sintassi delle annotazione per suggerire i data types.

Esempio:

        def myFunc(x, s = "python"):
            print(x)
            return s
            
        res = myFinc(10)
        
        print(res)
        
        >>> 10
        >>> python
        
Modifichiamo la funzione con delle **Type Annotations**:

        def myFunc(x: int, s: str = "python"):
            print(x)
            return s
            
Oppure specificando il tipo di valore di ritorno con l'operatore freccia:

        def myFunc(x: int, s: str = "python") -> str:
            print(x)
            return s
            
        print(myFunc.__annotations__)
        
La funzione print ci ritorna il dizionario con i valori della funzione.

La PEP 526 (python 3,6, 2016)

Estende le annotazioni di tipo dalle funzioni alle variabili.

Esempio:

        a: int = 10
        print(a)
        print(__annotations__)
        
        {'a': <class 'int'>}
        
L'annotazione di tipo può essere usata anche all'interno delle classi. Per annotare levariabili di istanza/classe.

Esempio:

        class MyClass:
            nome: str
            cognome: str
            
            def __init__(self, nome, cognome):
                self.nome = nome
                self.cognome = cognome

        mc = MyClass(nome = "Roberto", cognome = "Gianotto")
        print(mc)
        print(mc.nome)
        print(mc.cognome)
        
        <__main__.MyClass object at 0x02F507D0>
        Roberto
        Gianotto
        

## Le Data Classes

Abbiamo visto come già a partire dalla versione 3.6 python può gestire le annotazioni di tipo. Dalla versione
3.7 gestisce anche le **Data Classes**. Il principio ruota attorno ad un class decorator, che si chiama
data class definito all'interno del modulo data classes, che fornisce modulo e funzioni per definire le data classes.

Quindi se vogliamo usare le data classes la prima cosa da fare è importare il decoratore!!

Da come si vede nell'esempio si usa anche l'annotazione di tipo nella classe di esempio.

        from dataclasses import dataclass
        
        @dataclass
        class MyClass:
            nome: str
            cognome: str
            
Praticamente inserendo questo codice viene automaticamente generato un metodo init fatto così:

        def __init__(self, nome: str, cognome: str) -> None:
            self.nome = nome
            self.cognome = cognome

Un pò come succede per le annotations di Java (tipo Lombok). Inoltre però viene aggiunta,
sempre in automatico una implementazione dei seguenti metodi:

        __repr__
        __eq__ # (==)
        __ne__ @ (!=)
        
Quindi le **data classese** mi servono per implementare in automatico metodi senza doverli definire!!

Esempio:
        
        from dataclasses import dataclass

        @dataclass
        class MyClass:
            nome: str
            cognome: str

        mc = MyClass(nome = "Roberto", cognome = "Gianotto")
        print(mc)
        print(mc.nome)
        print(mc.cognome)
        
        >>>MyClass(nome='Roberto', cognome='Gianotto')
        >>>Roberto
        >>>Gianotto    
        
**Importante**

Il decoratore dataclass ammmette parametri che permettono molta personalizzazione.
Esempio:

       @dataclass(init=True, repr=True, order=True, frozen=False)
       ...
       
- init=True: chiediamo al decoratore di generare il costruttore in automatico, se lo 
mettiamo a False, non possiamo più generare istanze.

- repr=True: consente di avere una rappresentazione in output dei campi dell'istanza, 
come espresso qui: MyClass(nome='Roberto', cognome='Gianotto'), se lo metto a False, la rappresentazione
è di più difficile lettura: <__main__.MyClass object at 0x02F507D0>

- order=True: il valore di default è False, se messo a True vengono genrati dei metodi in automatico, 
che definiscono una gerarchia di ordine delle istanze sulla base di valori attuali.

- frozen=False: se impostato a False possiamo modificare i valori delle varibili di istanza
a nostro piacimento, però se impostiamo a True, l'intera classe si "congela" e non possiamo
alterare il valore dei campi!! Si ottiene un FrozenInstanceError.

## Assignment Expressions (da Python 3.8)

Espressioni con assegnamento: introducono un nuovo operatore del linguaggio, l'operatore 
**walrus** (tricheco) :=

Uno statement è un comando che forniamo all'interprete Python per ottenere un valore e viene
valutata a runtime (le più semplici sono i literal e gli operatori). Le invocazioni di metodi anche sono 
espressioni, perché producono dei valori di ritorno.

Ci sono dei casi in cui non possiamo assegnare dei valori di ritorno ad una variabile.

Esempio:

        def somma(a,b):
            return a + b
            
        x = somma(5,3)
        
        print(x)
        
        if x = somma(5,3) > 6: # ERRORE!!! Non potevo farlo fino alla versione 3.8
            print("x maggiore di 6")
            
Esempio 3.8:

        if x := somma(5,3) > 6:
            print("x maggiore di 6")
            
## Parametri Positional Only (da Python 3.8)

Parametri e argomenti di una funzione in Python.

Esempio:

Passaggio posizionale

        def somma(a, b, c):
            return a + b + c
        
        # passaggio di parametri per posizione, 3 argomenti posizionali    
        x = somma(10,4,2)
        print(x)
        >>> 16
        
Passaggio "Keyword", liberi di essere passati nell'ordine desiderato.
        
        # passaggio di parametri "keyword" argument, per chiave
        y = somma(a=10, b=4, c=2)
        print(y) 
        >>>16

Ci sono dei casi però dove chi definisce una funziona possa decidera di ammettere solo il passaggio
keyword o solo il passaggio posizionale. A partire dalla versione 3.8 questo è possbile con i parametri
"positional only". Questa specifica è stata introdotta nella PEP 570.

Esempio:

        def somma(a,/,b,c): # il carattere / dice che a riceve solo argomenti posizionali
            return a+b+c
            
Questo vuol dire che non va più bene scrivere questo:

        y = somma(a=10, b=4, c=2)
        
Ma devo mettere:

        y = somma(10, c=4, b=2)
        
**Importante**

**PEP 572** - Assignnment Expression
        
# Python e RabbitMQ

Python viene usato per il web e il machine learning, però può venir usato per applicazioni
scalabili, in grado di supportare un numero massivo di utenze. Si possono realizzare quindi 
applicazioni server scalabili servendosi di **RabbitMQ** che è un **message brokers** per architetture 
distribuite.

**Primo esempio di architettura distribuita (il client server)**

La comunicazione avviena tramite un server, che eroga un servizio e una secnoda, il client che richiede
 l'esecuzione del servizio richiesto, esempio classico sono le web aplpication( es. il browser e il web application server).
 
Il client fa una **request** e il server l'elabora e successivamente produce una **resposnse**, ritornando le inforamzioni 
richieste al client.

**Architetture vicino ai message brokers**

Producer e Consumer. Applicazioni che producono informazioni e applicazioni che hanno interesse a ricevere le notifiche
di queste informazioni prodotte.

Il **Producer** notifica l'informazione attraverso un **messaggio**. Una volta prodotto il messaggio, dopo il verificarsi di determinati eventi 
il **Consumer** puà recepire il messaggio. Al momento della pubblicazione del messaggio non necessariamente, il consumer deve essere attivo, ma non 
per questo il messaggio viene perduto!! I consumer possono essere molti, non soltanto uno, un certo numero di consumer, magari pure molto diversi tra loro e tutti 
presenti in linea al momento in cui il messaggio si rende disponibile. Inoltre i consumer non si conoscono in modo da essere sempre 
totalmente disaccoppiati. Il terzo strato applicativo che **disaccoppia** produttorri e consumatori e il **message brokers**. Non contengono
 il producer o il consumer, ma sono applicazioni che lavorano da intemediari tra i producer e i consumer, in modo che i consumer forniscano loro il messaggio e il message brokers 
 lo instradano ai consumer. Nello schema:
 
                                     --> Consumer
        Producer --> Message Brokers --> Consumer
                                     --> Consumer
                                     
Nel momento in cui un consumer si rende disponibile a leggere il messaggil il message borkers glielo consegna.

Sul mercato esistono vari tipi di message brokers, uno dei più diffusi è **RabbitMQ** è open source e usabile in diversi 
linguaggi di programmazioni, uno di questi è proprio Python.

## Installazione di RabbitMQ

https://www.rabbitmq.com/download.html

### Docker

        docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3-management

https://registry.hub.docker.com/_/rabbitmq/


   
# Python e MongoDB

## JSON

**JSON**: javascript object notation, basato su un sottosistema del linguaggio javascript è un formato di interscambio leggero dei dati

http://www.json.org

**Strutture di base del JSON**

- oggetti (strutture, dizionari, collezioni di associazioni tra nomi, chiavi e valori)
- array (sono liste ordinate di valori)

        {"stringa/chiave": "stringa"|number|object|array|true|false|null }

Ogni coppia chiave/valore è separata della successiva attraverso il carattere virgola.

Esempio (con oggetto annidato):

        {
            "nome": "Mario",
            "cognome": "Rossi",
            "età": 30,
            "computer": {
                "comp1": "Asus",
                "comp2": "Apple"
            }
        }

Esempio (array):

        {
            "nome": "Mario",
            "cognome": "Rossi",
            "età": 30,
            "computer": ["Asus", "Apple"]
        }

## BSON

Estensione di JSON. Bson è una forma di serializzazione di documenti JSON espressa non in formato testuale, ma binario.

http://bsonspec.org

Tipi di dati:

- date
- timestamp
- int
- double
- long
- binary data
- boolean
- ObjectId (12 byte, struttura predefinita) -> specifico per mongo DB

In mongoDB questo formato serve per:
- archiviare informazioni
- trasmettere informazioni (interscambio dati)

MongoDB usa BSON.

## Documenti e Collezioni (document e collection)

MongoDB è orientato ai documenti.

In un db relazionale i dati sono organizzati in tabelle con dei record che contengono i valori.

Un record in un db relazionale è un documento in un db di mongo db.

Un insieme di **documenti** sono mantenuti in una **collezione**. Collezione si può paragonare ad una tabella.

Un documento in una collection ci consente di archiviare dei dati espressi in JSON/BSON. Un recordo in mongo db è meno rigido rispetto al modello relazionale. Il modello relazionale dei dati è molto rigido.

Es. (di documento)

        {
            "_id": "987896scd5678",
            "nome": "Mario",
            "cognome": "Rossi",
            "eta": 30
        },
        ....

Più documento con lo stesso schema fanno la collection.
**_id** esiste in ogni documento Mongo DB.
I documenti in mongo non hanno una struttura predefinita, sono semplicemente degli oggetti Json che vengono archiviati.

Ogni singolo documento di una collezione di Mongo può avere una struttrua differente dagli altri documenti della collezione.

Possiamo archiviare i dati in una forma molto flessibile (array di oggetti).

## Installazione di Mongo DB

- Mongo DB e Pymongo: http.//mongodb.com

I **documenti** in Mongo vengono archiviati all'interno delle **collezioni**. Un insieme di collezioni viene archiviata dentro un **databasae** Mongo e un database viene archiviato in **Cluster**.

- Donwload del **Community Server**, la versione gratuita di Mongo DB.
- Compass è un tool visuale per accedere ai db di Mongo
- Pymongo è invece la libreria che permette a Python di accedere ad un db Mongo
- è ncessario lanciare il processo **mongod** che fa la start in ascolto di Mongo DB. Di default il motore di Mongo è in ascolto in **localhost:27017**

### Esercitazione Mongo DB

Il software di mongo db si scarica da qui: https://www.mongodb.com/try/download/community

Per scrivere il programma ho dovuto installare **pymongo**: da un terminale qualsiasi basta digitare

        pip install pymongo

Se non lo si fa non funzionano gli import negli script di Python.

Comandi per la shell:

        mongo

        mongo --shell

        mongo --version

        show dbs

        use dbname

        show collections

        use collectrion_name

Per visualizzare i documenti nelle collection conviene usare il tool grafico **Compass**.

#### Esercizio 1

        import pymongo
        from pymongo import MongoClient
        
        # eseguo la connessione con Mongo DB
        
        client = MongoClient('localhost', 27017)
        
        # creo un database
        
        db = client.testdb
        
        # creo la collection persone
        
        persone_collection = db.persone
        
        # creo una serie di indici
        
        persone_collection.create_index([("nome", pymongo.ASCENDING)])
        persone_collection.create_index([("cognome", pymongo.ASCENDING)])
        persone_collection.create_index([("computer", pymongo.ASCENDING)])
        
        # creo un documento
        
        p1 = {"nome": "Mario", "cognome": "Rossi", "eta": 30, "computer": ["asus", "msi", "acer"]}
        
        # inserisco il documento nella collezione
        persone_collection.insert_one(p1)
        # inserisco un secondo documento nella collezione
        p2 = {"nome": "Roberto", "cognome": "Gianotto", "eta": 42, "computer": ["lenovo", "msi"]}
        persone_collection.insert_one(p2)