def BMI(weight, height):
    return weight / (height * 2)


print("*** CALCOLO INDICE DI MASSA CORPOREA IN PYTHON ***")
weightOnKg = float(input("Inserisci il tuo peso in Kg: "))
heightInMt = float(input("Inserisci la tua altezza in metri: "))
print("Il tuo indice di massa corporea è = ", BMI(weightOnKg, heightInMt))
