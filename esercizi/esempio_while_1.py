max = -999999999

number = int(input("Enter the value or -1 to stop while: "))

while number != -1 :
    if number > max :
        max = number

    number = int(input("Enter the value or -1 to stop while: "))

print("The largest number is ", max)
