Tasks = ["Wake up", "Clean", "Study", "Draw", "Code"]
while True:
    print("\n---Menu--- \n1. Add task\n2. View tasks\n3. Remove task\n4. Exit \n")
    user_input = input("Enter number for option: ")

    task = ""
    if user_input == "1":
        while task != "n":
            task = input("\nAdd a task (n to return): ")
            Tasks.append(task)
        Tasks.pop()

    elif user_input == "2":
        print("\n--Tasks--")
        if Tasks == []:
            print("No task entered")
        for i in Tasks:
            print(f"{i+1}. {task}")
        back = input("\nn to return: ")
        continue

    elif user_input == "3":
        print("\n--Tasks--")
        if Tasks == []:
            print("No task entered")
        for i in Tasks:
            print(f"{i+1}. {task}")
        remove = int(input("\nSelect task number you want to delete: "))
        for i in range(len(Tasks)):
            if remove-1 == i:
                Tasks.pop(i)
        print(f"\nTask{remove} deleted")

        back = input("\nn to return: ")
        continue

    elif user_input == "4":
        print("Exit")
        break
    
    else:
        print("Invalid Entry")