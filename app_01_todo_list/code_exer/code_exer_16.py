import PySimpleGUI as sgui


label_feet = sgui.Text("Enter feet:")
input_feet = sgui.Input()

label_inches = sgui.Text("Enter inches:")
input_inches = sgui.Input()

convert_button = sgui.Button("Convert")

window = sgui.Window("Convertor",
                     layout=[[label_feet, input_feet],
                             [label_inches, input_inches],
                             [convert_button]])

window.read()
window.close()