# esempi di cicli for

for count in range(5):
    print(count + 1, end=" ")

print("")

for count in range(1, 4):
    print(count, end=" ")
    
print("")

for count in range(1, 6, 2):
    print(count, end=" ")
    
print("")

for count in range(6, 1, -1):
    print(count, end=" ")

print("")
   
# visualizza 100 volte il mio nome
mioCognome = "Roberto"
for cognome in range(1, 101):
    print(cognome, " ", mioCognome)