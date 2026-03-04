tasks = ["Wake Up", "Stretch", "Study", "Draw"]

def add_task(task):
    while True:
        task = input("\nAdd a task (n to return): ")
        if task == "":
            print("Invalid input")
            continue
        if task == "n":
            break
        tasks.append(task)

def view_task():
    print("\n--Tasks--")
    if not tasks:
        print("No task entered")

    for i, task in enumerate(tasks, start = 1) :
        print(f"{i}) {task}")

def remove_task():
    while True:
            remove = input("\nSelect task number you want to delete (n to return): ")

            if remove == "n":
                break  

            if not remove.isdigit():
                print("Invalid Input")
                continue
            
            remove = int(remove)

            if not 1 <= remove <= len(tasks):
                print("Task number is out of range")
                continue
        
            tasks.pop(remove - 1 )
            print(f"\nTask {remove} was deleted")
            break
    
def go_back():
    back = input("\nn to return: ").lower()
    while back != "n":
        print("Invalid input")
        back = input("\nn to return: ").lower()
    
def run():
    while True:
        print("\n---Menu--- \n1. Add task\n2. View tasks\n3. Remove task\n4. Exit \n")
        user_input = input("Enter number for option: ")

        if user_input == "1":

            add_task(tasks)

        elif user_input == "2":
            view_task()

            go_back()

        elif user_input == "3":
            view_task()

            remove_task()

            go_back()

        elif user_input == "4":
            print("Exit")
            break
        
        else:
            print("Invalid Entry")

run()
