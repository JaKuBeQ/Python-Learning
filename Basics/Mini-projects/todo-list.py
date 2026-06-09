tasks = []


def add(task):
    tasks.append(task)
    print("Task added.")


def show():
    if len(tasks) == 0:
        print("Your list is empty.")
    else:
        for i, task in enumerate(tasks, start=1):
            print(i, "-", task)


def delete(task):
    if task in tasks:
        tasks.remove(task)
        print("Task removed.")
    else:
        print("Task not found.")


while True:
    print("\nThis is your to-do list!")
    print("What do you want to do?")
    print("add / delete / show / close")

    choice = input("Choose an option: ")

    if choice == "add":
        task = input("Add task: ")
        add(task)

    elif choice == "delete":
        task = input("Task to delete: ")
        delete(task)

    elif choice == "show":
        show()

    elif choice == "close":
        print("Program closed.")
        break
    else:
        print("Invalid choice.")