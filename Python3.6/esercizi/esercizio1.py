# massimo tra due numeri interi

# funzione che calcola il massimo
def massimo(a,b):
    if a > b:
        print("\nIl massimo e\' = " + str(a) + "\n")
    elif a == b:
        print("\nI due valori inseriti sono uguali\n")
    else:
        print("\nIl massimo e\' = " + str(b) + "\n")

def eseguiMassimo():
    a = input('\nInserisci il primo numero: ')
    b = input('\nInserisci il secondo numero: ')
    #calcolo del massimo
    print(massimo(a,b))

# lancia il programma
eseguiMassimo()
