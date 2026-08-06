import streamlit as st 
st.header("coloums layout")
col1, col2 , col3 = st.columns(3)


with col1:
    st.metric("Temprature","36 Celcius",delta ="1 celcius")
with col2:
    st.metric("Humidity","80%", delta="10%")
with col3:
    st.metric("WindSpeed","15 Km/h", delta="-5 Km/h")