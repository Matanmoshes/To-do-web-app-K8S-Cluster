import streamlit as st                # Importing streamlit module for creating and running the web application.
import functions                      # Importing custom functions for handling to-do operations.

todos = functions.get_todos()         # Retrieving the list of to-dos from the functions module.

def add_todo():                       # Defining a function to add a new to-do item.
    todo = st.session_state["new_todo"] + "\n"  # Getting the new to-do from the session state and appending a newline.
    todos.append(todo)                # Adding the new to-do to the list of to-dos.
    functions.write_todos(todos)      # Saving the updated list of to-dos using a function from the functions module.

st.title("My Todo App")               # Setting the title of the web application.
st.subheader("This is my todo app.")  # Adding a subheader to the web application.
st.write("Thus app is to increase your productivity.")  # Displaying a message on the web application.

for index, todo in enumerate(todos):  # Iterating over the list of to-dos with their indices.
    checkbox = st.checkbox(todo, key=f"todo {index}")  # Creating a checkbox for each to-do item.
    if checkbox:                      # Checking if the checkbox is marked (to-do is completed).
        todos.pop(index)              # Removing the completed to-do from the list.
        functions.write_todos(todos)  # Saving the updated list after removal of the completed to-do.
        #del st.session_state[todo]
        st.experimental_rerun()       # Rerunning the app to update the list of to-dos displayed.

st.text_input(label="", placeholder="Add new todo...",  # Creating an input field for adding new to-dos.
              on_change=add_todo, key='new_todo')       # Calling the add_todo function when the input value changes.

