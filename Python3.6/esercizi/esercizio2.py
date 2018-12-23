# funzione che prende in input 3 numeri e ne ritorna il più grande tra loro

def massimo_tre_numeri(a, b, c):

    max = a

    if max < b:
        max = b
    if max < c:
        max = c

    return (max)

a = input('\nInserisci il primo valore: ')
b = input('\nInserisci il secondo valore: ')
c = input('\nInserisci il terzo valore: ')

risultato = massimo_tre_numeri(a, b, c)

print("\nIl massimo dei tre valori e' = " + str(risultato))