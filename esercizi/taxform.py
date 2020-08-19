"""
Program: taxform.py
Author: Gianotto Roberto
"""

# costanti
ALIQUOTA = 0.20
DEDUZIONE_STANDARD = 10000.0
DEDUZIONE_DIPENDENTE = 3000.0

# input
grossIncome = float(input('Digita il reddito lordo: '))
numDipendenti = int(input('Digitail numero dei dipenti: '))

# calcolo tassa sul reddito
taxableIncome = grossIncome - DEDUZIONE_STANDARD - DEDUZIONE_DIPENDENTE * numDipendenti
incomeTax = taxableIncome * ALIQUOTA

# output del risultato
print("Tassa sul reddito = " + str(incomeTax))
print("Tassa sul reddito arrotondata con la funzione round() = " + str(round(incomeTax)))
