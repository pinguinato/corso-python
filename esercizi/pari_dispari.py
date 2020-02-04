Evens = 0 # quanti pari
Odds = 0 # quanti dispari

Number = int(input("Enter the value or 0 to stop: "))

while Number != 0:
    if Number % 2 == 1: # dispari
        Odds += 1
    else:
        Evens += 1

    Number = int(input("Enter the value or 0 to stop: "))

print("\nI numeri pari sono: ", Evens)
print("\nI numeri dispari sono: ", Odds)