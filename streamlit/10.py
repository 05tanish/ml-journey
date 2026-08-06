import streamlit as st
import pandas as pd

# Create DataFrame
df = pd.DataFrame({
    "day": ["Mon", "Tue", "Wed", "Thu", "Fri"],
    "sales": [120, 95, 150, 200, 175],
    "returns": [10, 5, 30, 15, 8]
})

# Title
st.header("Sales Data")

# Display DataFrame
st.dataframe(df)

# Line Chart
st.line_chart(df.set_index("day"))

# Bar Chart (Sales only)
st.bar_chart(df.set_index("day")["sales"])

