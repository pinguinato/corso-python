# calcolatrice in python

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