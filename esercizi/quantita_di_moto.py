"""

Author: Gianotto Roberto

Quantità di moto = massa X velocità

"""

massa = float(input('Inserisci il tuo peso in kg: '))
velocita = float(input('Inserisci la velocità in m/s: '))

quantitaDiMoto = massa * velocita
print("La quantità di moto è pari a: " + str(quantitaDiMoto))
energiaCinetica = (0.5) * massa * (velocita * 2)
print("L'energia cinetica è pari a: " + str(energiaCinetica))

