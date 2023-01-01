import streamlit as st
import func_todos as ft


todos = ft.read_todos()


def add_todo():
    new_todo = st.session_state["new_todo"] + "\n"
    todos.append(new_todo)
    ft.write_todos(todos)


st.title("Todo App")
st.subheader("Simple todo app")
st.write("This web app is created to give me more practise in coding.")

for index, todo in enumerate(todos):
    key = "todo - "+todo
    checkbox = st.checkbox(todo, key=key)
    if checkbox:
        todos.pop(index)
        ft.write_todos(todos)
        del st.session_state[key]
        st.experimental_rerun()

st.text_input(label="", placeholder="Add a todo",
              on_change=add_todo, key="new_todo")
