import streamlit as st
from functions import get_todos, write_todos

st.title("Hello Everyone")
st.subheader("This is a small web app named todo app list")
st.write("my self anik and i hope you will like my todo app")

todo_list = get_todos()
for todo in todo_list:
    st.checkbox(todo)

st.text_input(label="", placeholder="Add a new todo item....")
