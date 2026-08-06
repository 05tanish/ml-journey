import streamlit as st
import pandas as pd

st.title("Interactive EDA App")

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    
    # 2. Display top 5 rows
    st.subheader("Top 5 Rows of the Dataset")
    st.dataframe(df.head())
    
    # 3. Display Metrics Matrix
    st.subheader("Dataset Overview & Metrics")
    
    num_cols = df.select_dtypes(include=["number"]).columns.tolist()
    cat_cols = df.select_dtypes(exclude=["number"]).columns.tolist()
    total_missing = int(df.isnull().sum().sum())
    
    m1, m2, m3, m4, m5 = st.columns(5)
    m1.metric("Total Rows", f"{df.shape[0]:,}")
    m2.metric("Total Columns", df.shape[1])
    m3.metric("Missing Values", total_missing)
    m4.metric("Numerical Columns", len(num_cols))
    m5.metric("Categorical Columns", len(cat_cols))
    
    st.markdown("---")
    
    # 4. Dropdown menus for numerical columns
    st.subheader("Select Axis for Visualization")
    
    if len(num_cols) == 0:
        st.warning("⚠️ No numerical columns found in the uploaded dataset for plotting.")
    else:
        col_x,col_y = st.columns(2)
        with col_x:
            x_axis = st.selectbox("X-axis", num_cols)
        with col_y:
            y_axis = st.selectbox("Y-axis", num_cols)
        if st.button("Generate Visualization", type="primary"):
            st.markdown("---")
            chart_col1, chart_col2 = st.columns(2)
            with chart_col1:
                with st.container(border=True):
                    st.subheader("📈 Line Chart")
                    st.line_chart(df.set_index(x_axis)[y_axis])
                    
            with chart_col2:
                with st.container(border=True):
                    st.subheader("📊 Bar Chart")
                    st.bar_chart(df.set_index(x_axis)[y_axis])
else:
    st.info("Please upload a CSV file to get started.")