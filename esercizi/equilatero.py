"""
Verifica se un triangolo è equilatero
"""

lato1 = int(input("Inserisci la dimensione intera per il primo lato del triangolo: "))
lato2 = int(input("Inserisci la dimensione intera per il secondo lato del triangolo: "))
lato3 = int(input("Inserisci la dimensione intera per il terzo lato del triangolo: "))


def verificatriangoloequilatero(lato1, lato2, lato3):
    if lato1 == lato2 and lato2 == lato3:
        print("Il triangolo è equilatero!")
    else:
        print("Il triangolo non è equilatero")


verificatriangoloequilatero(lato1, lato2, lato3)