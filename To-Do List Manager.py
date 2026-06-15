
FILE_NAME = "tasks.txt"

# LOAD TASKS
def load_tasks():
    try:
        with open(FILE_NAME, "r") as file:
            return [task.strip() for task in file.readlines()]
    except:
        return []

# SAVE TASKS
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")

# SHOW TASKS
def show_tasks(tasks):
    print("\n========== YOUR TASKS ==========")

    if len(tasks) == 0:
        print("No tasks available!")
    else:
        for i in range(len(tasks)):
            print(f"{i+1}. {tasks[i]}")

    print("=================================\n")

# ADD TASK
def add_task(tasks):
    task = input("Enter your task: ")

    if task.strip() == "":
        print("Task cannot be empty!")
    else:
        tasks.append(task)
        save_tasks(tasks)
        print("Task added successfully!")

# DELETE TASK
def delete_task(tasks):
    show_tasks(tasks)

    if len(tasks) == 0:
        return

    try:
        index = int(input("Enter task number to delete: ")) - 1

        if index < 0 or index >= len(tasks):
            print("Invalid task number!")
        else:
            removed = tasks.pop(index)
            save_tasks(tasks)
            print(f"Deleted: {removed}")

    except:
        print("Please enter valid number!")

# ==========================
# COMPLETE TASK (NEW FEATURE)
# ==========================
def complete_task(tasks):
    show_tasks(tasks)

    if len(tasks) == 0:
        return

    try:
        index = int(input("Enter task number to mark complete: ")) - 1

        if index < 0 or index >= len(tasks):
            print("Invalid task number!")
        else:
            tasks[index] = "✔ COMPLETED - " + tasks[index]
            save_tasks(tasks)
            print("Task marked as completed!")

    except:
        print("Please enter valid number!")

# MAIN PROGRAM
tasks = load_tasks()

while True:
    print("\n===== TO-DO MENU =====")
    print("1. Show Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Complete Task")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        show_tasks(tasks)

    elif choice == "2":
        add_task(tasks)

    elif choice == "3":
        delete_task(tasks)

    elif choice == "4":
        complete_task(tasks)

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice! Try again.")