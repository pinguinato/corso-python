MAX_IS = "Il massimo è "

a = int(input("Inserisci il primo numero intero: "))
b = int(input("Inserisci il secondo numero intero: "))
c = int(input("Inserisci il terzo numero intero: "))

if a > b and a > c:
    print(MAX_IS, a)
elif b > a and b > c:
    print(MAX_IS, b)
else:
    print(MAX_IS, c)