import streamlit as st
import pandas as pd

st.write("""
# California Housing Prediction
## Dataset 
""")


df = pd.read_csv("dataset/housing.csv")

st.dataframe(df)

st.divider()
st.subheader("Map of Data Points")
st.map(df)

st.subheader("Metrics")
st.metric(label="Total Rows", value=len(df))
st.metric(label="Average Median Income Per Household", value=round(df['median_income'].mean(), 2))
