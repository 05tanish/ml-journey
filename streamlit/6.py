import pandas as pd 
import streamlit as st 
uploaded = st.file_uploader("Upload CSV")

if uploaded:
    import pandas as pd
    df = pd.read_csv(uploaded)
    st.dataframe(df)
    st.write("first 5 rows")
    st.write(df.head())
    st.write("last 5 rows")
    st.write(df.tail())
    st.write("information")
    st.write(df.info)
    st.write("Statical data")
    st.write(df.describe())
    st.write("Null Values")
    st.write(df.isnull().sum())
