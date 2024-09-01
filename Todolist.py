# To-Do List Application

def add_task(task):
    with open("tasks.txt", "a") as file:
        file.write(task + "\n")

def view_tasks():
    with open("tasks.txt", "r") as file:
        tasks = file.readlines()
        for task in tasks:
            print(task.strip())

def main():
    while True:
        print("\n1. Add Task\n2. View Tasks\n3. Exit the Tab")
        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter task: ")
            add_task(task)
        elif choice == "2":
            print("\nTasks:")
            view_tasks()
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
