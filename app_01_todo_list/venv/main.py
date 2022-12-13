savefile="saved.txt"

while True:
    action=input("Type add, show, edit (by a number), done (by a number) or exit: ")

    if action.startswith("add"):
        with open(savefile, "r") as file:
            todos = file.readlines()
        todos.append(action[4:]+"\n")
        with open(savefile, "w") as file:
            file.writelines(todos)
    elif action.startswith("show"):
        with open(savefile, "r") as file:
            todos = file.readlines()
        for index, item in enumerate(todos):
            item = item.strip("\n")
            print(f"{index+1}-{item}")
    elif action.startswith("edit"):
        with open(savefile, "r") as file:
            todos = file.readlines()
        num=int(action[5:])-1
        new_item=input("Enter the replacement: ")
        todos[num] = new_item
        with open(savefile, "w") as file:
            file.writelines(todos)
    elif action.startswith("done"):
        with open(savefile, "r") as file:
            todos = file.readlines()
        num = int(action[5:])-1
        todos.pop(num)
        with open(savefile, "w") as file:
            file.writelines(todos)
    elif action.startswith("exit"):
        break
    else:
        print("You typed with a mistake or a wrong keyword")