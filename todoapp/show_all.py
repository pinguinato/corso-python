def show_all_tasks():
    path = "task_list.txt"
    tasks_list = open(path, "r")
    todo_list = tasks_list.read()
    print("\n-----------@@@------------\n")
    print(todo_list)
    print("\n-----------@@@------------\n")