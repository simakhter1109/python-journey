tasks = []
while True:
    print("\n--- TO DO LIST ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")
    
    choice = input("Enter your choice: ")

    match choice:
        case "1":
            task = input("Enter a task: ")
            tasks.append(task)
            print("Task added successfully!")

        case "2":
            if len(tasks) == 0:
                print("No tasks available.")
            else:
                print("\nYour Tasks:")
                for i in range(len(tasks)):
                    print(i + 1, ".", tasks[i])

        case "3":
            if len(tasks) == 0:
                print("No tasks to remove.")
            else:
                print("\nYour Tasks:")
                for i in range(len(tasks)):
                    print(i + 1, ".", tasks[i])

                num = int(input("Enter task number to remove: "))
                if 1 <= num <= len(tasks):
                    removed = tasks.pop(num - 1)
                    print(removed, "removed successfully!")
                else:
                    print("Invalid task number.")

        case "4":
            print("Goodbye!")
            break

        case _:
            print("Invalid choice. Try again.")