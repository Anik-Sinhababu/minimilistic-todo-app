import streamlit as st
from functions import get_todos, write_todos
import base64


def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
        f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
        unsafe_allow_html=True
    )


add_bg_from_local("pexels-oleksandr-pidvalnyi-1227513.jpg")

todo_list = get_todos()


def add_todo():
    todo_item = st.session_state['new_todo'] + '\n'
    todo_list.append(todo_item)
    write_todos(todo_list)


st.title("Hello Everyone")
st.subheader("This is a small web app named todo app list",)
st.write("my self Anik and i hope you will like my todo app")

for index, todo in enumerate(todo_list):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todo_list.pop(index)
        write_todos(todo_list)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="Hey", placeholder="Add a new todo item....", on_change=add_todo, key='new_todo')
