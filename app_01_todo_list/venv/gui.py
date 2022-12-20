#done with pysimplegui
import func_todos
import PySimpleGUI as sgui


label = sgui.Text("Type in a to-do task:")
input_box = sgui.InputText(tooltip="Enter a task")
add_button = sgui.Button("Add")

window = sgui.Window("To Do app", layout=[[label], [input_box, add_button]])
window.read()
window.close()