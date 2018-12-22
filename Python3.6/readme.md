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

## LABORATORIO 1 - CACLOLATRICE IN PYTHON 3.6

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

