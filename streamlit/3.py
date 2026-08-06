import pandas as pd 
import streamlit as st 
uploaded = st.file_uploader("Upload CSV")

if uploaded:
    import pandas as pd
    df = pd.read_csv(uploaded)
    st.dataframe(df)