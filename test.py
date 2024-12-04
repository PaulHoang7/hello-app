import streamlit as st

st.title("Submit Button Example")

# Input
user_input = st.text_input("Enter your name:")

# Button
if st.button("Submit"):
    st.write(f"Hello, {user_input}!")
