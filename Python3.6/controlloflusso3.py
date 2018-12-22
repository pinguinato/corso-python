# break e continue

contatore = 0
while True:
    print(contatore)
    contatore += 1
    if contatore > 5:
        print('Sto uscendo dal loop!')
        break

contatore = 0
while contatore < 10:
    contatore += 1
    if contatore == 6:
        print('saltato')
        continue
    print(contatore)