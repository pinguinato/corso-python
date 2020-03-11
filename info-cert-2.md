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

