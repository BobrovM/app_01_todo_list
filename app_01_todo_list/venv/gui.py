#done with pysimplegui
import func_todos
import PySimpleGUI as sgui


label = sgui.Text("Type in a to-do task:")
input_box = sgui.InputText(tooltip="Enter a task", key="todo")
add_button = sgui.Button("Add")
list_box = sgui.Listbox(values=func_todos.read_todos(), key="todos",
                        enable_events=True, size=(50, 10))
edit_button = sgui.Button("Edit")

window = sgui.Window("To Do app",
                     layout=[[label], [input_box, add_button], [list_box, edit_button]],
                     font=("Calibri", 13))

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = func_todos.read_todos()
            todos.append(values["todo"] + "\n")
            func_todos.write_todos(todos)
            window["todos"].update(values=todos)
        case "Edit":
            todo_edit = values["todos"][0]
            new_todo = values["todo"]

            todos = func_todos.read_todos()
            index = todos.index(todo_edit)
            todos[index] = new_todo + "\n"
            func_todos.write_todos(todos)
            window["todos"].update(todos)
        case "todos":
            window["todo"].update(value=values["todos"][0])
        case sgui.WIN_CLOSED:
            break

window.close()