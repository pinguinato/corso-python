"""
Calcola la superfice di un cubo prendendo in input la misura del lato
"""

latoDelCubo = float(input("Inserisci la misura del lato del cubo: "))
superficeCubo = 6 * (latoDelCubo * latoDelCubo)
print("La superfice del cubo è = " + str(round(superficeCubo)))