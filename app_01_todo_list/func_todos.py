SAVEFILE = "saved.txt"


def read_todos(filepath=SAVEFILE):
    """ Read a text file and return the list of to-do items. """
    with open(filepath, "r") as file:
        file_input = file.readlines()
    return file_input


def write_todos(todos_input, filepath=SAVEFILE):
    """ Write the list of to-do items in a text file. """
    with open(filepath, "w") as file:
        file.writelines(todos_input)
