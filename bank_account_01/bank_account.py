# implementa funzionalità di un bacomat

# autore: Gianotto Roberto

saldo = 0

# stampa saldo del tuo CC
def get_saldo(saldo):
    print('Il tuo saldo attuale: ' + str(saldo))

# versamento sul CC
def versamento(saldo,versamento):
    saldo += versamento


def prelievo(saldo,prelievo):
    saldo -= prelievo

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
        get_saldo(saldo)
        print('\n')
    elif scelta == '2':
        print("Versamento")
    elif scelta == '3':
        print("Prelievo")
    else:
        print("Grazie ed arrivederci.")
        break