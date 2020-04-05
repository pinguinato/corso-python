from datetime import date
from credits import print_credits
from show_all import show_all_tasks

def my_app_menu():
    menu = '''\n+++ ToDo App +++\n
    1. Add New Task
    2. Read Task
    3. Delete Task
    4. Show All Tasks
    5. Save To File
    6. Credits
    7. Exit

    Please make your choice: '''

    choice = int(input(menu))

    while choice:
        if choice >= 7 or choice <= 0:
            print("entering Exit, bye bye")
            break
        elif choice == 1:
            print("entering Add New Task")
        elif choice == 2:
            print("entering Read Task")
        elif choice == 3:
            print("entering Delete Task")
        elif choice == 4:
            print("\nTASKS LIST\n")
            today = date.today()
            print("\n Today is: ", today)
            show_all_tasks()
        elif choice == 5:
            print("entering Save To File")
        elif choice == 6:
            print_credits()

        choice = int(input(menu))
