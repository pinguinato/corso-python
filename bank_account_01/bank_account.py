# implementa funzionalità di un bacomat

# autore: Gianotto Roberto

saldo = 0


# menu slezione operazioni CC
def menu_operazioni():
    print('--------------------')
    print('|1| VISUALIZZA SALDO')
    print('|2| VERSAMENTO')
    print('|3| PRELIEVO')
    print('--------------------')


while True:
    print('\nBANK ACCOUNT PYTHON ')
    menu_operazioni()
    scelta = input('Fai una scelta: ')
    if scelta == '1':
        print('Il tuo saldo attuale in Euro: ' + str(saldo) + ' €')
    elif scelta == '2':
        versamento = int(input('\nCifra da aggiungere al conto corrente: '))
        saldo += versamento
        print('Versamento eseguito correttamente')
    elif scelta == '3':
        prelievo = int(input('\nCifra da prelevare al coonto corrente: '))
        if prelievo > saldo:
            print('\nNon è possibile effettuare l\'operazione poichè sul conto non ci sono abbastanza soldi.')
        else:
            saldo -= prelievo
            print('Prelievo eseguito correttamente')
    else:
        print("Grazie ed arrivederci.")
        break
