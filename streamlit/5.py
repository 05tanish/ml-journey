import streamlit as st


user_name = st.text_input("Enter your name")
if user_name:
    st.write("Hello", user_name)

name  = st.text_input("Enter the name ")
height = st.number_input("Enter height ")

age = st.number_input("Enter the age",min_value=0 , max_value=120, value=18 , step=1)

if st.button("Display info"):
    st.success(f"name:{name}")
    st.write("name",name)
    st.success(f"age:{age}")
    st.success(f"height:{height}")
    