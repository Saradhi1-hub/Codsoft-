
todo_list = []

def show_menu():
    print("\n====== TO-DO LIST MENU ======")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")

def add_task():
    task = input("Enter task: ")
    todo_list.append({"task": task, "done": False})
    print("Task added successfully!")

def view_tasks():
    if not todo_list:
        print("No tasks found.")
        return
    print("\nYour Tasks:")
    for index, item in enumerate(todo_list):
        status = "✅" if item["done"] else "❌"
        print(f"{index + 1}. {item['task']} [{status}]")

def mark_done():
    view_tasks()
    try:
        choice = int(input("Enter task number to mark as done: ")) - 1
        if 0 <= choice < len(todo_list):
            todo_list[choice]["done"] = True
            print("Task marked as done!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Enter a valid number.")

def delete_task():
    view_tasks()
    try:
        choice = int(input("Enter task number to delete: ")) - 1
        if 0 <= choice < len(todo_list):
            removed = todo_list.pop(choice)
            print(f"Deleted task: {removed['task']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Enter a valid number.")

while True:
    show_menu()
    option = input("Choose an option (1-5): ")

    if option == '1':
        add_task()
    elif option == '2':
        view_tasks()
    elif option == '3':
        mark_done()
    elif option == '4':
        delete_task()
    elif option == '5':
        print("Exiting To-Do List App. Goodbye!")
        break
    else:
        print("Invalid option. Please select 1-5.")





Added Task 1 - To-Do List in Python
