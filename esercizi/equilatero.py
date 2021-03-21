"""
Verifica se un triangolo è equilatero
Verifica se un trinagolo è rettangolo
"""

lato1 = int(input("Inserisci la dimensione intera per il primo lato del triangolo: "))
lato2 = int(input("Inserisci la dimensione intera per il secondo lato del triangolo: "))
lato3 = int(input("Inserisci la dimensione intera per il terzo lato del triangolo: "))


def verificatriangoloequilatero(lato1, lato2, lato3):
    if lato1 == lato2 and lato2 == lato3:
        print("Il triangolo è equilatero!")
    else:
        print("Il triangolo non è equilatero")


def verificatriangolorettangolo(ipotenusa, cateto1, cateto2):
    quadratoipotenusa = ipotenusa * ipotenusa
    sommaquadraticateti = (cateto1 * cateto1) + (cateto2 * cateto2)
    if quadratoipotenusa == sommaquadraticateti:
        print("Il triangolo è rettangolo")
    else:
        print("Il trinagolo non è rettangolo")


# verifica equilatero
verificatriangoloequilatero(lato1, lato2, lato3)

# verifica rettangolo
verificatriangolorettangolo(lato1, lato2, lato3)