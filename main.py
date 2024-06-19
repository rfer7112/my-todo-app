import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    todo = st.session_state['new_todo'] + '\n'
    print(todo)
    todos.append(todo)
    functions.write_todos(todos)


st.title("Checklist")
st.subheader("Create a list of task to follow")
st.write("Add a <span style='color: green;'>task</span> or "
         "<span style='color: blue;'>check</span> the task to delete it", unsafe_allow_html=True)

for index, item in enumerate(todos):
    checkbox = st.checkbox(item, key=item)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[item]
        st.rerun()

st.text_input(label="", placeholder="Enter a task", on_change=add_todo, key='new_todo')
