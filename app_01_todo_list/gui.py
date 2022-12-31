# done with pysimplegui
import func_todos
import PySimpleGUI as sgui
import time
import os


if not os.path.exists(func_todos.SAVEFILE):
    with open(func_todos.SAVEFILE, "w") as file:
        pass

sgui.theme("Kayak")

clock = sgui.Text("", key="clock")
label = sgui.Text("Type in a to-do task:")
input_box = sgui.InputText(tooltip="Enter a task", key="todo")
add_button = sgui.Button("Add")
list_box = sgui.Listbox(values=func_todos.read_todos(), key="todos",
                        enable_events=True, size=(50, 10))
edit_button = sgui.Button("Edit")
complete_button = sgui.Button("Complete")
exit_button = sgui.Button("Exit")

window = sgui.Window("To Do app",
                     layout=[[label, clock],
                             [input_box, add_button],
                             [list_box, edit_button, complete_button],
                             [exit_button]],
                     font=("Calibri", 13))

while True:
    event, values = window.read(timeout=1000)
    window["clock"].update(value=time.strftime("%d-%m-%Y %H:%M:%S %z"))
    match event:
        case "Add":
            todos = func_todos.read_todos()
            todos.append(values["todo"] + "\n")
            func_todos.write_todos(todos)
            window["todos"].update(values=todos)
            window["todo"].update(value="")
        case "Edit":
            try:
                todo_edit = values["todos"][0]
                new_todo = values["todo"]
                todos = func_todos.read_todos()
                index = todos.index(todo_edit)
                todos[index] = new_todo + "\n"
                func_todos.write_todos(todos)
                window["todos"].update(todos)
            except IndexError:
                sgui.popup("Please select an item from the list.",
                           font=("Calibri", 13))
        case "Complete":
            todo_completed = values["todos"][0]
            todos = func_todos.read_todos()
            todos.remove(todo_completed)
            func_todos.write_todos(todos)
            window["todos"].update(values=todos)
            window["todo"].update(value="")
        case "todos":
            window["todo"].update(value=values["todos"][0])
        case "Exit":
            break
        case sgui.WIN_CLOSED:
            break

window.close()
