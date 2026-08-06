import streamlit as st
import pandas as pd


st.title("📊 CSV Column Bar Chart")

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    # Read CSV
    df = pd.read_csv(uploaded_file)

    # Display DataFrame
    st.subheader("Dataset")
    st.dataframe(df)

    # Select column
    column = st.selectbox("Select a column for Bar Chart", df.columns)

    # Count occurrences of each value
    chart_data = df[column].value_counts().reset_index()
    chart_data.columns = [column, "Count"]

    st.subheader(f"Bar Chart of {column}")

    # Bar chart
    st.bar_chart(chart_data.set_index(column))

else:
    st.info("Please upload a CSV file.")