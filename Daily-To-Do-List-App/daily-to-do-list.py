import json 
import os

def load_file():

    if os.path.exists("tasks.json"):
        with open("tasks.json", "r") as file:
            return json.load(file)
        
    else:
        print("Empty save file. New save file created")
        return []
    
tasks = load_file()


def save_file(tasks):

    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)


def add_task(): 
    while True:
        task = input("\nAdd a task (n to return): ")
        if task == "":
            print("Invalid input")
            continue
        if task == "n":
            break
        tasks.append({"task_item": task, "done": False})
        save_file(tasks)


def view_task():
    print("\n--Tasks--")

    if not tasks:
        print("No task entered")
        return
    
    for i, task in enumerate(tasks, start = 1) :

        if task["done"]:
            status = "✔"
        else:
            status = " "
            
        print(f"{i}) [{status}] {task['task_item']}")


def mark_task():

    if not tasks:
        print("\n--Tasks--")
        print("No task entered")
        return
    
    while True:
        view_task()
        marked = input("\nSelect task number you want to mark as done (n to return): ")
    
        if marked == "n":
            break
        
        if not marked.isdigit():
            print("Invalid Input")
            continue
            
        marked = int(marked)

        if not 1 <= marked <= len(tasks):
            print("Task number is out of range")
            continue

        tasks[marked - 1]["done"] = not tasks[marked - 1]["done"]
        save_file(tasks)


def edit_task():

    if not tasks:
        print("\n--Tasks--")
        print("No task entered")
        return
    
    view_task()
    
    while True:
        edit = input("\nSelect task number you want to edit (n to return): ")

        if edit == "n":
            break  

        if not edit.isdigit():
            print("Invalid Input")
            continue
            
        edit = int(edit)

        if not 1 <= edit <= len(tasks):
            print("Task number is out of range")
            continue

        task_to_edit = tasks[edit - 1]['task_item']
        print(f"\n{edit}) {task_to_edit}")

        while True:
            
            edited_task = input("Enter edit (n to return): ")

            if edited_task != 'n':
                tasks[edit - 1]["task_item"] = edited_task
                save_file(tasks)
                view_task()


def remove_task():

    if not tasks:
        print("\n--Tasks--")
        print("No task entered")
        return
    
    view_task()
    
    while True:
        remove = input("\nSelect task number you want to remove (n to return): ")

        if remove == "n":
            break  

        if not remove.isdigit():
            print("Invalid Input")
            continue
            
        remove = int(remove)

        if not 1 <= remove <= len(tasks):
            print("Task number is out of range")
            continue
        
        deleted = tasks[remove-1]['task_item']
        tasks.pop(remove - 1)

        save_file(tasks)

        view_task()

        
        print(f"\n{deleted} was removed")
        break
        
        
    
def clear_all():

    with open("tasks.json", "w") as file:
        json.dump([],file)
        global tasks
        tasks = []
        save_file(tasks) 
    print("\nAll tasks have been cleared")

#Might get rid of it later/ not really needed
def go_back():
    back = input("\nn to return: ").lower()
    while back != "n":
        print("Invalid input")
        back = input("\nn to return: ").lower()
    
def run():
    
    while True:

        print("\n---Menu--- \n1. Add task\n2. View tasks\n3. Mark tasks\n4. Edit tasks\n5. Remove task\n6. Clear all tasks\n7. Exit \n")
        user_input = input("Enter number for option: ")

        if user_input == "1":
            add_task()

        elif user_input == "2":
            view_task()
            go_back()

        elif user_input == "3":
            mark_task()

        elif user_input == "4":
            edit_task()

        elif user_input == "5":
            remove_task()
            go_back()

        elif user_input == "6":
            clear_all()

        elif user_input == "7":
            save_file(tasks)

            print("Exit")
            break
        
        else:
            print("Invalid Entry")

run()
