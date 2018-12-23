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