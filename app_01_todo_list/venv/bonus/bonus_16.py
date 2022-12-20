import PySimpleGUI as sgui


label_up_select = sgui.Text("Select files to compress:")
input_select = sgui.Input()
choose_button_select = sgui.FileBrowse("Choose")

label_folder = sgui.Text("Choose destination folder:")
input_folder = sgui.Input()
choose_button_folder = sgui.FolderBrowse("Choose")

compress_button = sgui.Button("Compress")

window = sgui.Window("Custom compressor",
                     layout=[[label_up_select, input_select, choose_button_select],
                             [label_folder, input_folder, choose_button_folder],
                             [compress_button]])

window.read()
window.close()