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
        
### Attributi di istanza (metodi)
