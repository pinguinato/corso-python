'''
Todo list with mongoDB e Python
Autore: Gianotto Roberto
'''

# MENU

def main_menu():
    print("\n\n* * * TODO LIST * * *\n\n")
    print("\t\t|0| Esci dal programma\n\n")


while True:
    main_menu()
    choice = input("Cosa devi fare oggi?")

    if choice == 0:
        break