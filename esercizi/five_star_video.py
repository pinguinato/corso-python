PREZZO_VIDEO_VECCHIO = 2.00
PREZZO_VIDEO_NUOVO = 30.00
numeroVideoVecchi = int(input("Numero di video vecchi affittati: "))
numeroVideoNuovi = int(input("Numero di video nuovi affittati: "))
totaleCostoVideoVecchi = float(numeroVideoVecchi * PREZZO_VIDEO_VECCHIO)
totaleCostoVideoNuovi = float(numeroVideoNuovi * PREZZO_VIDEO_NUOVO)
totaleComplessivo = float(totaleCostoVideoNuovi + totaleCostoVideoVecchi)
print("Devi pagare € " + str(totaleComplessivo))