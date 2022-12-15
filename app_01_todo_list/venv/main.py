savefile = "saved.txt"


def read_todos():
    with open(savefile, "r") as file:
        file_input = file.readlines()
    return file_input


def write_todos(user_input):
    with open(savefile, "w") as file:
        file.writelines(user_input)


while True:
    action=input("Type add, show, edit (by a number), done (by a number) or exit: ")

    if action.startswith("add"):
        todos = read_todos()
        todos.append(action[4:]+"\n")
        write_todos(todos)
    elif action.startswith("show"):
        todos = read_todos()
        for index, item in enumerate(todos):
            item = item.strip("\n")
            print(f"{index+1}-{item}")
    elif action.startswith("edit"):
        try:
            todos = read_todos()
            num=int(action[5:])-1
            new_item=input("Enter the replacement: ")
            todos[num] = new_item+"\n"
            write_todos(todos)
        except ValueError:
            print("Your edit command is not valid. Try using task number, which can be provided by command show.")
            continue
        except IndexError:
            print("Your edit command is not valid. There is no task with that number.")
            continue
    elif action.startswith("done"):
        try:
            todos = read_todos()
            num = int(action[5:])-1
            todos.pop(num)
            write_todos(todos)
        except ValueError:
            print("Your done command is not valid. Try using task number, which can be provided by command show.")
            continue
        except IndexError:
            print("Your done command is not valid. There is no task with that number.")
            continue
    elif action.startswith("exit"):
        break
    else:
        print("You typed with a mistake or a wrong keyword")