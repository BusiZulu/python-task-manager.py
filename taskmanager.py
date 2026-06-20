# Simple Task Manager - Python Project

tasks = []

def show_tasks():
    print("\n===== YOUR TASKS =====")
    if len(tasks) == 0:
        print("No tasks added yet.")
    else:
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print("Task added successfully!")

def delete_task():
    show_tasks()
    try:
        task_num = int(input("Enter task number to delete: "))
        if 0 < task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            print(f"Deleted task: {removed}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

while True:
    print("\n===== TASK MANAGER MENU =====")
    print("1. View tasks")
    print("2. Add task")
    print("3. Delete task")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        show_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, try again.")
