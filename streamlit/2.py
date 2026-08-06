import streamlit as st 
st.title("read and display data frame ")

import pandas as pd 


df = pd.read_csv("/Users/tanishjain/carrer/languages /ml-journey/Datasets/fifa_world_cup_2026_player_performance.csv")
if st.button("Click Me"):
    st.write(df)
    st.dataframe(df)

