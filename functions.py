FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """ Reads a text file and returns the list of
    to-do items back to the call
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
        return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ writes a to-do list to a  text file """
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)
