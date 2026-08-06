import streamlit as st
st.title("My First Streamlit App")
st.header("Section Header")
st.subheader("Sub Header")
st.text("This is plain text")
st.markdown("**bold**, *italic*, and `code`")
st.write("st.write() handles almost anything:", {"key": "value"})

name = "Tanish"
age = 23

age = st.slider(
    "Age",
    1,
    100,
    20
)

st.write(age)

agree = st.checkbox("I agree")

if agree:
    st.success("Thank you!")

color = st.radio(
    "Choose",
    ["Red", "Green", "Blue"]
)

st.write(color)

city = st.selectbox(
    "Choose City",
    ["Delhi", "Mumbai", "Bangalore"]
)

st.write(city)

languages = st.multiselect(
    "Languages",
    ["Python", "Java", "C++", "Go"]
)

st.write(languages)

st.metric("Revenue", "$1200", "+12%")
col1, col2 = st.columns(2)

with col1:
    st.write("Left")

with col2:
    st.write("Right")

st.sidebar.title("Menu")

option = st.sidebar.selectbox(
    "Choose",
    ["Home", "About"]
)

st.write(option)