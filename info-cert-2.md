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

