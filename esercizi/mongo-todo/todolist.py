'''
Todo list with mongoDB e Python
Autore: Gianotto Roberto
'''

from main_menu import application_menu, modify_a_todo, list_all_todos, create_new_todo, delete_a_todo, delete_all, list_all_todos_only_values 

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
    elif choice == '3': # modify
        modify_a_todo()
    elif choice == '4': # delete first
        delete_a_todo()
    elif choice == '5': # delete all
        delete_all()
    elif choice == '6': # list alla todos wit only values
        list_all_todos_only_values()
    else:
        print("\nScelta errata, fai una scelta tra quelle disponibili...\n")