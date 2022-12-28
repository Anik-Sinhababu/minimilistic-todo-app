import streamlit as st
from functions import get_todos, write_todos


def add_todo():
    todo_item = st.session_state['new_todo'] + '\n'
    todo_list.append(todo_item)
    write_todos(todo_list)


st.title("Hello Everyone")
st.subheader("This is a small web app named todo app list")
st.write("my self anik and i hope you will like my todo app")

todo_list = get_todos()
for todo in todo_list:
    st.checkbox(todo)

st.text_input(label="Hey", placeholder="Add a new todo item....", on_change=add_todo, key='new_todo')


