FILEPATH = "todos.txt"  # Defining the default file path for the to-do list.

def get_todos(filepath=FILEPATH):  # Function to read to-dos from a file; accepts a file path, defaults to FILEPATH.
    """ Read a text file and return the list of to-do items."""
    with open(filepath, 'r') as file_local:  # Opening the file in read mode.
        todos_local = file_local.readlines()  # Reading all lines from the file into a list.
    return todos_local  # Returning the list of to-dos.

def write_todos(todos_local, filepath=FILEPATH):  # Function to write to-dos to a file; accepts a list and a file path, defaults to FILEPATH.
    """ Write the to-do items list in the text file. """
    with open(filepath, 'w') as file:  # Opening the file in write mode.
        file.writelines(todos_local)  # Writing the list of to-dos to the file.

if __name__ == "__main__":  # Standard boilerplate to call the main() function to begin the program.
    print("Hello")  # Printing a greeting message.
    print(get_todos())  # Printing the list of to-dos retrieved from the file.
