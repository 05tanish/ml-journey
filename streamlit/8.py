import streamlit as st

name = st.text_input("Enter the name", placeholder = "eg . Mallesh")
age = st.number_input("Enter the age", min_value = 1, max_value=100, value = 20)
lang = st.selectbox("favoriate language ",["python ", "java","c++","javascript"])
agree = st.checkbox("I agree")
if st.button("Submit"):
    if agree:
        st.write("name ", name)
        st.write("age ", age)
        st.write("language ", lang)
    else:
        st.write("Please agree to the terms and conditions")
else:
    st.write("Please click on submit")


