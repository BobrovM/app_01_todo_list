import PySimpleGUI as sgui


def convertor(feet, inches):
    return int(feet) * 0.3048 + int(inches) * 0.0254


sgui.theme("Black")

label_feet = sgui.Text("Enter feet:")
input_feet = sgui.Input(key="feet")

label_inches = sgui.Text("Enter inches:")
input_inches = sgui.Input(key="inches")

convert_button = sgui.Button("Convert")
result = sgui.Text(key="result")

exit_button = sgui.Button("Exit", key="exit")

window = sgui.Window("Convertor",
                     layout=[[label_feet, input_feet],
                             [label_inches, input_inches],
                             [convert_button, result],
                             [exit_button]])

while True:
    event, values = window.read()
    match event:
        case sgui.WIN_CLOSED:
            break
        case "exit":
            break
        case "Convert":
            try:
                result = convertor(values["feet"], values["inches"])
                window["result"].update(value=result)
            except ValueError:
                sgui.popup("Please provide 2 numbers!")

window.close()