'''
Todo list with mongoDB e Python
Autore: Gianotto Roberto
'''

from main_menu import application_menu
from main_menu import list_all_todos
from main_menu import create_new_todo
from main_menu import delete_a_todo

while True:
    application_menu()
    choice = input("\nCosa devi fare oggi? ")
    
    if choice == '0': # exit program
        print("\nUscita dal programma\n")
        break
    elif choice == '1': # create
        create_new_todo()
    elif choice == '2': # read
        list_all_todos()
    elif choice == '4': # delete first
        delete_a_todo()
    else:
        print("\nScelta errata, fai una scelta tra quelle disponibili...\n")