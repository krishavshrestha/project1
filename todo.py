# ===============================
# DecodeLabs Project 1
# To-Do List Application
# ===============================

# List to store all tasks
tasks = []

print("Welcome to the To-Do List Application!")

while True:
    print("\n========== TO-DO LIST ==========")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    # Add Task
    if choice == "1":
        task = input("Enter a new task: ")
        tasks.append(task)
        print(f'"{task}" has been added successfully!')

    # View Tasks
    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\n------ Your Tasks ------")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")

    # Exit
    elif choice == "3":
        print("Thank you for using the To-Do List Application!")
        break

    # Invalid Choice
    else:
        print("Invalid choice! Please enter 1, 2, or 3.")
