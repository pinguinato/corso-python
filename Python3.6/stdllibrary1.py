# uso dei metodi della standard library

# import di tutte le funzioni di random library
import random
# import della sola funzione sqrt della math library, non è necessario citare la libreria di dipendenza
from math import sqrt

for numero in range(10):
    valore = random.randint(1,50)
    print(valore)

testmath = int(sqrt(4))
print(testmath)