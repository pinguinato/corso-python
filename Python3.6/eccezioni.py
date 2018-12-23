def divisione(a,b):
    try:
        risultato = a / b
        print("Il risultato della divisione = " + str(risultato))
    except ZeroDivisionError:
        print("Non posso dividere per 0")


divisione(10,0)