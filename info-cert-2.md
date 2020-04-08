# Info Certificazione Python (PCAP) - Parte 2

## 4.1.1 Moduli

Codice crescente significa maggiore manutenzione. La soluzione è dividere in parti
il codice di un programma, e poi unirle tutte insieme. Ad esempio un programma si può
dividere in:
- interfaccia utente
- logica del programma

Tale processo viene chimato **decomposizione**.

Come si divide un software in tanti parti collaborative?

Si divide in **MODULI**.

Un modulo è un file contenente istruzioni e definizioni Python.

## 4.1.2 Gestione dei moduli

Prevede due diversi sistemi:

- usare un modulo preesistente, definito da qualcun altro (USER, sei l'utilizzatore del modulo) 
- creare un nuovo modulo per uso personale (SUPPLIER, sei il creatore del modulo)

## 4.1.3 Come utilizzare un modulo

Per prima cosa, se si vuole usare un modulo bisogna conoscerne il suo nome. Un numero
piuttosto consistente di moduli ci viene fornito da Python stesso. Tutti questi moduli, forniti
con Python vanno a formare quella che si chiama **libreira standard Python**.

Per informazioni aggiuntive guarda: https://docs.python.org/3/library/index.html

Ogni moduli si costituisce di **entità** che sono funzioni, variaibili, costanti, classi ed oggetti.

Ad esempio: il modulo **math**

Il modulo parla chiaro: raccoglie **funzionalità della matematica** come sin(), log() ecc...

## 4.1.4 Importare un modulo

Per poter usare un modulo, lo dobbiamo importare e possiamo farlo con la parola chiave

        import
        
Supponiamo di voler usare delle funzionalità del modulo **math**:

- supponiamo di voler usare il pi-greco
- supponiamo di voler usare la funzione sin()

Entrambi stanno dentro il modulo math, ma è come vengono importate nello script che ne permette
l'utilizzo.

Import è una parola chiave e permette l'importazione di moduli nei propri script.

Es:

        import math
        
La sintassi da seguire è:

        import nome_del_modulo
        
L'istruzione import può trovarsi in qualsiasi posizione all'interno del codice del modulo, ma
prima di usare le funzionalità del modulo va inserita la import altrimenti non si possono
richiamare le funzionalità del modulo se prima non c'è la importazione dello stesso.

## 4.1.6 Importazione multipla

Posso importare più moduli contemporaneamente:

Ad esempio:

        import math, sys

La lunghezza della lista dei moduli da importare ha una lunghezza arbitraria.

## 4.1.7 Namespace

Lo spazio di nomi è uno spazio, in cui esistono i nomi e non sono in conflitto tra loro.
Ovvero non esistono oggetti diversi con lo stesso nome. Ogni gruppo di nomi tende a nominare
i propri membri in forma univoca. All'interno di ogni namespace ogni nome deve rimanere univoco (ad 
esempio i genitori non daranno mai gli stessi nomi ai figli).

## 4.1.8 Ancora sull'importazione

Se il modulo con un nome specificato esiste ed è accessibile 
(un modulo è in realtà un file sorgente Python), 
Python importa i suoi contenuti, ovvero tutti i nomi definiti 
nel modulo diventano noti, 
ma non inseriscono lo spazio dei nomi del codice.

Ciò significa che puoi avere le tue entità denominate **sin** o **pi** 
e non saranno influenzate dall'importazione in alcun modo.

A questo punto, ti starai chiedendo come accedere al 
pi proveniente dal modulo di matematica. Per fare questo, **devi qualificare 
il pi con il nome del suo modulo originale**.

La via per "qualificare" l'importazione specifica di un modulo è:

        import math.pi
        import math.sin
        
La sintassi è la seguente:
    
        import nome_modulo.nome_entità
        
Si usa la **dot notation**.

Es.

        import math
        
        print(math.sin(math.pi/2))
        
        >>> 1.0
        
Se si rimuovono i qualificatori math davanti alle entità non c'è modo per usare
le entità del modulo math. Il codice sarebbe errato!

## 4.1.11 Coesistenza di spazio di nomi

Ora un esempio su come possono coesistere il nostro namespace e un altro namespace (quello di math)

Es.

        import math

        # definisco una mia fuzione pi(x)
        def sin(x):
            if 2 * x == pi:
                return 0.9999999
            else:
                return None

        pi = 3.14

        # uso il mio namespace
        print(sin(pi/2))
        
        # uso il namespace di math
        print(math.sin(math.pi/2))
        
        >>> 0.9999999
        >>> 1.0
        
Da come si può vedere dall'output le entità non vanno in conflitto!

## 4.1.12 Importazione di un modulo: la clausola FROM

Viene usata per importare selettivamente un modulo Python.

Es.

        from math import pi
        
In questo modo non vengono importate altre entità eccetto **pi**.

Es.

        print(math.e)
        
Causa un errore!

Es. 

Se riscriviamo il seno di pi/2 rispetto a prima avremo:

        from math import sin,pi
        
        print(sin(pi/2))
        
        >>> 1.0
        
Es.

        from math import sin,pi
        
        print(sin(pi/2))
        pi=3.14
        def sin(x):
            if 2 * x == pi:
                return 0.99999999
            else:
                return None
        print(sin(p/2))
        
        >>> 1.0
        >>> 0.99999999
        
Es.
        
        pi = 3.14
        def sin(x):
            if 2 * x == pi:
                return 0.99999999
            else:
                return None

        print(sin(pi / 2))
        from math import sin, pi
        print(sin(pi / 2))
        
        >>> 0.99999999
        >>> 1.0
        
## 4.1.16 Forma aggressiva di import from

Es.
        
        from module import *
        
I nomi delle entità vengono rimpazzati dal carattere asterisco. Questo permette di 
importare tutte le entità di un modulo, è conveniente, ma è rischiosa per il fatto
che espone lo script a conflitti di nomi. Non conviene usarla.

## 4.1.17 Ancora sull'import, aliasing

Se usi la variante del modulo di importazione e non ti piace il nome di un determinato 
modulo, ad esempio è lo stesso di uno già definito, quindi la qualificazione diventa 
problematica, allora puoi usare **l'aliasing**.

Es.

        import module as alias
        
Identifica l'importazione di un modulo con un nome diverso dall'originale. **Alias** è il 
nome che si desidera utilizzare rispetto all'originale. **As** è una parola chiave!

Es.

        import math as M
        
        print(M.sin(M.pi/2))
        
        >>> 1.0
        
## 4.1.19 Ancora sull'importazione di moduli, alias con from

Un altro esempio di eseguire l'import con from usando l'alias.

Es.

        from module import name as alias
        
        from module import n as a, m as b, o as c
        
        from math import pi as PI, sin as sine
        
Es.

        from math import pi as PI, sin as sine

        print(sine(PI/2))
        
        >>> 1.0
        
## 4.2.1 Lavorare con i moduli Standard (della libreria standard Python)

### La funzione dir()

Non ha la caratteristica della funzionalità **dir** di Windows/Unix, però permette 
di fare il listing di tutte le entità contenute all'interno di un modulo specifico. 
Per porterla usare su di un modulo, quest'ultimo deve essere prima importato.

Es. 

        import math as M

        print(dir(M))
        
        >>> [....., 'asin', 'atan',..., 'e', ...., 'log'....]
        
La funzione **dir()** restituisce un elenco in ordine alfabetico di tutte le entità 
disponibili. Se il nome del modulo è stato modiificato, dobbiamo usare l'**alias**.
L'uso della funzione in unoscript è disponibile anche se non ha molto senso.

Es.

        import math
        for name in dir(math):
            print(name, end='\t')

**Importante**

La funzione dir() può venir usata anche nella Python Shell per conoscere il contenuto 
di un modulo.

## 4.2.4 Alcune funzioni della libreria Math

Funzioni **trigonometriche**:

- sin(x)
- cos(x)
- tan(x)

e le loro inverse:

- asin(x)
- acos(x)
- atan(x)

Entità matematiche:

- pi
- radians(x)
- degrees(x)

Iperboliche:

- sinh(x)
- cosh(x)
- tanh(x)
- asinh(x)
- acosh(x)
- atanh(x)

Es.

        from math import pi, radians, degrees, sin, cos, tan, asin

        ad = 90
        ar = radians(ad)
        ad = degrees(ar)
        print(ad == 90.)
        print(ar == pi/2.)
        print(sin(ar) / cos(ar) == tan(ar))
        print(asin(sin(ar)) == ar)
        
        >>> True
        >>> True
        >>> True
        >>> True
        
Ancora altre funzioni del modulo math:

Esponenziali:

- e
- exp(x)
- log(x)
- log(x b)
- log10(x)
- log2(x)

Non deve essere importata ed è una funzione **built-in**:

- pox(x,y)

Es.

    from math import e, exp, log

    print(pow(e,1) == exp(log(e)))
    print(pow(2,2) == exp(2 * log(2)))
    print(log(e,e) == exp(0))
    
    >>> True
    >>> True
    >>> True
    
Ancora funzioni di math definite di **general purpose**:

- ceil(x)
- floor(x)
- trunc(x)
- factorial(x)
- hypot(x,y)

Es.

    from math import ceil, floor, trunc

    x = 1.4
    y = 2.6

    print(floor(x), floor(y)) # arrotondamento per difettos 
    print(floor(-x), floor(-y)) 
    print(ceil(x), ceil(y)) # arrotondamento per eccesso
    print(ceil(-x), ceil(-y))
    print(trunc(x), trunc(y)) # tronca la virgola
    print(trunc(-x), trunc(-y))
    
    >>> 1 2
        -2 -3
        2 3
        -1 -2
        1 2
        -1 -2
        
## 4.2.9 Funzioni RANDOM

Altro modulo degno di nota in Python è **random**. Fornisce meccanismi in grado di operare su numeri pseudocasuali.

**Nota**: i numeri generati dai moduli possono apparire casuali (prefisso pseudo), nel senso che non puoi prevedere i loro valori successivi, però va ricordato che vengono 
calcolati attraverso argoritmi raffinati e non sono quindi effettivamente casuali. Gli algoritmi stessi non sono casuali, sono deterministici e prevedibili. I dati prodotti 
dai computer deterministici non possono essere casuali in alcun modo. Solo ciò che sfugge al nostro controllo, tipo l'intensità della radiazione cosmica, è effettivamente casuale. 

Un generatore di numeri casuali prevede un valore noto come **seed** (seme), che viene dato in input e viene calcolato su di esso un numero casuale e produce un nuovo valore di seed. La durata di un ciclo si basa sul valore di seed, non è infinita e prima o poi torna a ripetersi.

## 4.2.10 Funzioni del modulo random

### funzione random

                from random import random

è la funzione più famosa del modulo. Produce un numero float nel range [0.0 ... 1.0]

                from random import random
                for i in range(5):
                        print(random())


                0.25719090407949696
                0.2466298423547747
                0.8709344043104064
                0.24521970019158656
                0.928175848095429

### funzione seed

è in grado di impostare direttamente il seed del generatore:

- seed() imposta il seed con l'ora corrente
- seed(i) imposta il seed con il valore intero i

Es.

        from random import random, seed
        
        seed(0)
        
        for i in range(5):
            print(random())
            
        0.8444218515250481
        0.7579544029403025
        0.420571580830845
        0.25891675029296335
        0.5112747213686085    
        
### funzioni per valori casuali interi


        randrange(end)
        randrange(beg,end)
        randrange(beg, end, step)
        randint(left, right)

Le prime tre funzioni generano un numero casuale intero preso dall'intervallo.

Es.

        from random import randint, randrange
        print(randrange(1), end=' ')
        print(randrange(0, 1), end=' ')
        print(randrange(0, 1, 1), end=' ')
        print(randint(0, 1))
        
        >>> 0 0 0 1
        
Notare l'esclusione implicita sul lato destro, end è sempre escluso.

### Svantaggi

Le funzioni precedenti possono produrre valori ripetitivi.

Es.

        from random import randint

        for i in range(10):
            print(randint(1, 10), end=',')
            
        >>> 2,6,5,6,5,7,6,6,5,1,
        
Quindi diciamo che non è un buon sistema per generare dei numeri per una lotteria,
ma per fortuna esistono soluzioni a questi problemi.

## 4.2.14 Altr funzioni randomiche

- choice(sequence)
- sample(sequence, element_to_choice=1)

Choice scegli un elemento random dalla sequenza e lo ritorna, sample invece crea una sequenza 
di numeri non ripetuti sulla base dell'element_to_choice, che non può essere più grande 
della lunghezza della sequenza di input.

Es. 

        from random import choice, sample
        lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        print(choice(lst))
        print(sample(lst, 5))
        print(sample(lst, 10))
        
        >>> 5
        >>> [5, 8, 3, 7, 9]
        >>> [8, 9, 7, 3, 10, 2, 5, 6, 4, 1]
        
## 4.2.15 Conoscere dove si è

L'ambiente Python può fornire informazioni sul sistema interrogando con delle specifiche 
funzioni i servizi del sistema operativo sottostante. I livello più basso è l'hardware, sul quale 
poggia il sistema operativo, poi Python stesso e per fninire il nostro codice Python.
Per interrogare il sistema cè un modulo Python che si occpua di tutte queste informazioni.

## 4.2.16 Funzioni del modulo platform

Es. **platform**

platform(aliased=se impostato presenta nome alternativo, terse=parametro che se 1(True) abbrevia il risultato)

        from platform import platform
        
        print(platform())
        print(platform(1))
        print(platform(0,1))
        
        >>> Windows-10-10.0.18362-SP0
        >>> Windows-10-10.0.18362-SP0
        >>> Windows-10

Es. **machine**

        from platform import machine
        
        print(machine())
        
        >>> AMD64
        
Viene stampato il nome generico dell'architettura della macchina fisica (nel nostro caso 64 bit)

Es. **processor**

        from platform import processor
        
        print(processor())
        
        >>> Intel64 Family 6 Model 142 Stepping 10, GenuineIntel
        
Questa funzione stampa il nome del vero processore fisico sulla macchina fisica.

Es. **system**

        from platform import system
        
        print(system())
        
        >>> Windows
        
System stampa il nome del sistema operativo installato sulla macchina fisica.

Es. **version**

        from platform import version
        print(version())
        
        >>> 10.0.18362
        
## 4.2.21 Ancora funzioni del modulo platform

- python_implementation(): ritorna una stringa che evidenzia la versione di python che
esegue il nostro codice.
- python_version_tuple(): ritorna una tupla con 3 valori numerici nell'ordine: **major** python version,
**minor** part, **patch** level number.

Es. (nel mio caso)

    from platform import python_implementation, python_version_tuple, python_version

    print(python_implementation())
    print(python_version_tuple())
    print(python_version())
    
    >>> CPython
    >>> ('3', '7', '1')
    >>> 3.7.1
    
## 4.2.22 Module Index per Python

https://docs.python.org/3/py-modindex.html

## 4.3.1 Modules and Packages

- **modulo**: contenitore di funzioni, si possono racchiudere tutte le funzioni che voglio e può essere distribuito ovunque,
è buona norma non mescolare funzioni di contensto diverso all'interno dello stesso modulo.
- **fare tanti moduli** crea confuzione ed esiste un contenitore al di sopra dei moduli, questo si chiama **package** e si può 
vendere esattamente come una **cartella** (o contenitore di moduli).

## 4.3.2 Il nostro primo modulo da zero

- crea un file **module.py** vuoto
- ci vogliono 2 file per creare questo processo
- crea un file **main.py** che importa il module.py

            
            import module.py # dentro main.py
            
- i file devono trovarsi nella stessa locazione(cartella), compilo main.py, non vedo nulla vuol dire che va bene perché è stato importato 
dentro module.py
- anche se non notiamo nulla dentro la nostra cartella si sono creati dei nuovi elementi "nascosti":
    - una cartella __pycache__
    - dentro pycache un file **module.cpython-37.pyc** che ripporta il nome del nostro modulo custom, questo
    è un file destinato esclusivamente all'uso di python e il suo contenuto è illeggibile è un codice semi compilato, che permette
    di velocizzare le importazioni successive, serve all'interprete di Python.
    
- quando un modulo viene importato, il suo contenuto **viene eseguito implicitamente da Python**.
- le assegnazioni avvengono una volta soltanto come le importazioni, queste non vengono inutilmente ripetute se sono già state fatte.
- adesso inserisco dentro module.py:

        print(__name__)
        
- se eseguo module.py ottengo:

        
            >>> I like to be a module
                __main__
                
- se eseguo main.py:

            
            >>> I like to be a module
                module
                
Possiamo affermare che:
- quando si esegue direttamente un file, la sua variabile __name__ è impostata su __main__
- quando un file viene importato come modulo, la sua variabile __name__ è impostata sul nome del file (escluso .py)

Es. (dentro module.py)


        if __name__ == "__main__":
            print("I prefer to be a module")
        else:
            print("I like to be a module")
            
è un modo per verificare in quale contesto è eseguita la variabile **name**.

- nel caso eseguo module l'output sarà: "I prefer to be a module"
- nel caso eseguo main l'output sarà: "I like to be a module"

Es. (di modulo)

        #!/usr/bin/env python3 # shebang, su alcuni sistemi è fondamentali

        """ module.py - an example of Python module """ # questa si chiama doc-string

        __counter = 0

        def suml(list): # funzione pronta per l'importazione
	        global __counter
	        __counter += 1
	        sum = 0
	        for el in list:
		        sum += el
	        return sum

        def prodl(list): # funzione pronta per l'importazione
	        global __counter	
	        __counter += 1
	        prod = 1
	        for el in list:
		        prod *= el
	        return prod

        if __name__ == "__main__": # evidenzia quando viene eseguito il modulo
	        print("I prefer to be a module, but I can do some tests for you")
	        l = [i+1 for i in range(5)]
	        print(suml(l) == 15)
	        print(prodl(l) == 120)
	        
	       
## 4.3.12 Un esempio più complesso

Come funziona se devo importare dei moduli che si trovano in percorsi differenti rispetto 
al file che li deve utilizzare, fino ad adesso abbiamo sempre disposto il file del modulo 
da importare dentro la stessa directory del file che lo importa.

Vediamo come Python ricerca i moduli.

In realtà esiste una variabile di Python chiamata **path** e raggiungibile con il modulo 
**sys**, che contiene tutti i percorsi di sistema, se il modulo non rientra in quel percorso, 
Python non riesce a trovarlo.

Es. 

        from sys import path
        
Supponiamo questa disposizione di file e cartelle(con Windows):

- il nostro file **main.py** si trova in C:\Users\user\py\progs\main.py
- il nostro modulo **module.py** si trova in C:\Users\user\py\modules\module.py

Es.

        from sys import path
        
        path.append('..\\modules')
        
        import module
        
        ....
        
Abbiamo usato un **path relativo** che parte dalla cartella dove è contenuto il programma main.py, 
nulla vieta di usare un percorso **assoluto** come: 

        path.append('C:\\Users\\user\\py\\modules')
        
**Nota**

Se voglio usare un solo backslash nel percorso devo farne l'escape.

## 4.3.13 Il tuo primo package

- Come dire a Python che una struttura complessa di cartelle è un **package**?
Risposta: devo predisporre uno speciale file __init__.py

- Dove metto questa struttura per renderla accessibile a Python? 
Risposta: lo posso mettere ovunque

## 4.3.18 __init__.py

- In ogni package c'è un file __init__.py, se non sono richieste inizializzazioni speciali il file può essere lasciato vuoto, ma ci deve essere!
Questo permette a Python di localizzare la struttura come package.

- init.py va messo nella root del package, oppure in altre sottocartelle del package.

- i moduli non hanno bisogno di un file init.py, ne hanno uno messo da Python implicitamente.






## 5.1.1 Concetti base della programmazione ad oggetti

Il paradigma ad oggetti è utile su progetti di grandi dimensioni. Python può essere utilizzato sia per programmare in forma 
procedurale, sia ad oggetti. Lo sviluppo di interfacce grafiche però richiede una rigorosa conoscenza della programmazione ad oggetti.

Nel paradigmi ad oggetti dati e codice stanno insieme e vengono suddivisi in **classi**, ogni classe è come una ricetta che viene usata 
quando si desidera creare un **oggetto** utile. Ogni oggetto ha una serie di tratti chiamati **attributi** o **proprietà** ed è in grado di 
eseguire una serie di **attività** o **operazioni** chiamati più comunemente **metodi**.

Gli oggetti sono incarnazioni di idee espresse in classi, gli oggetti interagiscono tra di loro scambiando i loro dati attraverso l'uso dei 
metodi.

Una classe ben costruita è in grado di proteggere l'accesso ai suoi dati e nasconderli quindi da modifiche non autorizzate.

Il paradigma ad oggetti riflette esperienze di vita reale.

La parola classe è come una **categoria**:

Es. (di gerarchia)

- Veicoli
    -   Veicoli terrestri
        -   Veicoli su gomma
        -   Veicoli su binari
        -   Hovercraft
    -   Veicoli marini
    -   Veicoli spaziali
    -   Veicoli aerei
    
Es. (di gerarchia)

- Animali
    - Mammiferi
        - Domestici
        - Selvaggi
    - Rettili
    - Uccelli
    - Pesci
    - Anfibi
    
## 5.1.15 Classi e oggetti

**Classe**

è un insieme di oggetti

**Oggetto**

insieme dei requisiti e caratteristiche di una specifica classe.

- le classi formano una gerarchia
- un oggetto appartenente ad una classe specifica appartiene a tutte le superclassi contemporaneamente, ma non 
alle sue sottoclassi.
- le sottoclassi sono più specializzate delle superclassi.

Ogni sottoclasse è più specializzata (o più specifica) della sua superclasse. Al contrario, ogni superclasse è più generale (più astratta) di qualsiasi sua sottoclasse. 

**Eredità**

Qualsiasi oggetto vincolato a un livello specifico di una gerarchia
 di classi eredita tutti i tratti (nonché i requisiti e le qualità) definiti 
 all'interno di una delle superclassi.
 
Ogni oggetto eredità tutte le peculiarità delle superclassi.

3 gruppi di attributi:

- un oggetto ha un nome che lo identifica in modo univoco nel suo spazio dei nomi di casa (anche se potrebbero esserci anche alcuni oggetti anonimi)
- un oggetto ha una serie di proprietà individuali che lo rendono originale, unico o eccezionale (anche se è possibile che alcuni oggetti non abbiano alcuna proprietà)
- un oggetto ha una serie di abilità per svolgere attività specifiche, in grado di cambiare l'oggetto stesso o alcuni degli altri oggetti.

C'è un suggerimento (anche se non sempre funziona) che può aiutarti a identificare una delle tre sfere sopra. Ogni volta che descrivi un oggetto e usi:

    un nome - probabilmente definisci il nome dell'oggetto;
    un aggettivo: probabilmente definisci la proprietà dell'oggetto;
    un verbo: probabilmente definisci l'attività dell'oggetto.
    
Due frasi di esempio dovrebbero servire da buon esempio:


        Max è un grosso gatto che dorme tutto il giorno.

        Nome oggetto = max

        Classe casa = Cat

        Proprietà = Dimensione (grande)

        Attività = Sonno (tutto il giorno)
        
## 5.1.8 La tua prima classe


        class OurClass:
            pass
            
La programmazione degli oggetti è l'arte di definire ed espandere le classi. Una classe è un 
modello di una parte molto specifica della realtà, che riflette le proprietà e le attività che si trovano nel mondo reale.

Le classi definite all'inizio sono troppo generali e imprecise per coprire il maggior numero possibile di casi reali.
Non ci sono ostacoli alla definizione di nuove sottoclassi più precise. Erediteranno tutto dalla loro superclasse, quindi il lavoro che è andato alla sua creazione non è sprecato.
La nuova classe può aggiungere nuove proprietà e nuove attività e pertanto può essere più utile in applicazioni specifiche. Ovviamente, può essere utilizzato come superclasse per qualsiasi numero di sottoclassi appena create.
Non è necessario che il processo abbia fine. Puoi creare tutte le classi di cui hai bisogno.

La classe definita non ha nulla a che fare con l'oggetto: l'esistenza di una classe non significa che nessuno degli oggetti compatibili verrà creato automaticamente. 
La classe stessa non è in grado di creare un oggetto: devi crearlo tu stesso e Python ti consente di farlo.

La classe si crea con la parola chiave **class** seguita dal nome della classe e poi mettiamo i due punti, per iniziare la classe. La parola 
chiave pass riempie la classe di nulla, senza proprietà o metodi.

La classe appena definita diventa uno strumento in grado di creare nuovi oggetti. Lo strumento deve essere utilizzato esplicitamente, su richiesta. 
Immagina di voler creare un (esattamente uno) oggetto della classe OurClass.

Es.

        ourobject = OurClass()
        
## 5.2.1 Che cosa è uno STACK

Lo stack è una struttura per lo storing dei dati. Il nome alternativo per lo stack è LIFO.
Lo stack viene usato per implementare tantissimi algoritmi.

Es. Implementazione di uno stack (procedurale)

        stack = []
        
        def push(val):
            stack.append(val)
            
        def pop():
            val = stack[-1]
            del stack[-1]
            return val
        
        push(3)
        push(2)
        push(1)
        print(pop())
        print(pop())
        print(pop())

Una implementazione di questo tipo è molto pratica e funziona, però è anche molto vulnerabile perché si può accedere alle variabili,
non c'è protezione e si può alterare la struttura della pila senza controllo. L'approccio ad oggetti impedisce, grazie al metodo 
dell'**incapsulamento** di intervenire direttamente sulle variabili, ma le nasconde dall'esterno. Inoltre se ho una classe che produce stack,
io posso fare tutti gli stack che voglio e in più posso arricchire questa classe creando delle nuove funzionalità o estensioni di questa classe.

Es. implementazione di uno stack (approccio ad oggetti)

Primo passo:

        class Stack:
            def __init__(self):
                print('Hi')
                
        stack = Stack()
        
Obiettivi:
- gli stack che definiamo devono essere indipendenti e i loro elementi nascosti
- ci vuole un elenco per ogni stack

Python non ha costrutti come altri linguaggi di programmazione per fare queste cose, è necessario equipaggiare la nostra classe
di una funzionalità in grado di garantirci questo comportamento: il **Costruttore**. Questo ci permette:
- di essere invocato solo quando viene creato un nuovo oggetto
- è nominato in modo rigoroso
- il costruttore sa tutto sulla natura dell'oggetto da creare
- il nome del costruttore è sempre __init__
- ha un parametro obbligatorio chiamato **self**, è una convenzione e semplifica la lettura del codice

Eseguendo il codice sopra l'output che si ottiene è:

        >>> Hi
        
Non c'è nessuna invocazione esplicita del costruttore, in realtà è stato invocato implicitamente nell'atto di creazione
dello **stack**. Qualsiasi modifica apportata all'interno del costruttore che modifica lo stato del parametro self, si riflette 
sull'oggetto creato, questo vuol dire che posso aggiungere proprietà all'oggetto che rimangono lì fino a quando l'oggetto non viene
 rimosso.
 
Es.

Secondo Passo(definizione di proprietà e accesso ad esse):

        class Stack:
            def __init__(self):
                self.stk = []
                
        stack = Stack()
        print(len(stack.stk))
        
Da come si vede usiamo la **dotted notation** per accedere alla proprietà **stk** dell'oggetto stack. Si accede alle proprietà 
degli oggetti in Python allo stesso modo di come si invocano i metodi. In questo modo, dall'esempio si vede che possiamo 
verificare la lunghezza dello stack però noi non vogliamo questa cosa, vorremmo nasconderla e adesso vediamo come si fa:

Es.

Terzo Passo (come Python implementa l'incapsulamento negli oggetti)

        class Stack:
            def __init__(self):
                self.__stk = []
                
        stack = Stack()
        print(len(stack.__stk))
        
Anteporre due underscore al nome della proprietà di un oggetto, vuol dire renderla **privata**, questo è il modo in cui Python
interpreta l'incapsulamento. Se una proprietà è privata allora è possibile solo accedervi dall'interno di una classe.

## 5.2.11 Classe Stack (Approccio ad oggetti)

Es.

Quarto Passo(implementiamo la pop e la push):









        
        