import streamlit as st
import pandas as pd
import plotly.express as px

st.write("""
# California Housing Prediction
## Dataset 
""")


# Read and display DataFrame info
df = pd.read_csv("dataset/housing.csv")
st.dataframe(df)
st.divider()

# Metrics
st.subheader("Metrics")
st.metric(label="Total Rows", value=len(df))
st.metric(label="Average Median Income Per Household", value=round(df['median_income'].mean(), 2))
st.divider()

# Plots
# # Map
st.subheader("Map of Data Points")
st.map(df)
st.write("") 
st.write("") 
st.write("") 


# # HeatMap
st.subheader("HeatMap Representation")
corr = df.select_dtypes(include='number').corr()
fig = px.imshow(corr, text_auto=True)
st.plotly_chart(fig)



