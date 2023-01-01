import PySimpleGUI as sgui
from bonus_18_back_zip import extract_archive


sgui.theme("Kayak")

label_select = sgui.Text("Select archive:")
input_select = sgui.Input()
choose_button_file = sgui.FileBrowse("Choose", key="archive")

label_select_dest = sgui.Text("Select dest dir:")
input_select_dest = sgui.Input()
choose_button_folder = sgui.FolderBrowse("Choose", key="folder")

extract_button = sgui.Button("Extract")
label_output = sgui.Text(key="output", text_color="green")

window = sgui.Window("Archive Extractor",
                     layout=[[label_select, input_select, choose_button_file],
                             [label_select_dest, input_select_dest, choose_button_folder],
                             [extract_button, label_output]])

while True:
    event, values = window.read()

    match event:
        case sgui.WIN_CLOSED:
            break

    print(event)
    print(values)
    archive_path = values["archive"]
    dest_dir = values["folder"]
    extract_archive(archive_path, dest_dir)
    window["output"].update(value="Extraction Completed")

window.close()