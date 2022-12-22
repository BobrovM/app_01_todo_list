import PySimpleGUI as sgui
import bonus_16_17_zip_creator

label_up_select = sgui.Text("Select files to compress:")
input_select = sgui.Input()
choose_button_select = sgui.FileBrowse("Choose", key="files")

label_folder = sgui.Text("Choose destination folder:")
input_folder = sgui.Input()
choose_button_folder = sgui.FolderBrowse("Choose_Folder", key="folder")

compress_button = sgui.Button("Compress")
output_result = sgui.Text(key="output", text_color="green")

window = sgui.Window("Custom compressor",
                     layout=[[label_up_select, input_select, choose_button_select],
                             [label_folder, input_folder, choose_button_folder],
                             [compress_button, output_result]])

while True:
    event, values = window.read()
    match event:
        case sgui.WIN_CLOSED:
            break
    print(event, values)
    filepaths = values["files"].split(";")
    folder = values["folder"]
    bonus_16_17_zip_creator.make_archive(filepaths, folder)
    window["output"].update(value="Completed")

window.close()
