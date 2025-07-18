import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

import warnings
warnings.filterwarnings('ignore')

st.set_page_config(page_title="Superstore!!!", page_icon=":bar_chart:",layout="wide")

st.title(" :bar_chart: Sample SuperStore EDA")
st.markdown('<style>div.block-container{padding-top:1rem;}</style>',unsafe_allow_html=True)

file= st.file_uploader(":file_folder: Upload a file",type=["csv"])
if file:
    filename = file.name
    st.write(filename)
    df = pd.read_csv(file)
    st.dataframe(df)

    col1, col2 = st.columns((2))
    df["DATE"] = pd.to_datetime(df["DATE"], errors='coerce')
    df['DATE'].dropna(inplace = True)

    # Getting the min and max date 
    startDate = pd.to_datetime(df["DATE"]).min()
    endDate = pd.to_datetime(df["DATE"]).max()

    with col1:
        date1 = pd.to_datetime(st.date_input("Start Date", startDate))

    with col2:
        date2 = pd.to_datetime(st.date_input("End Date", endDate))

    df = df[(df["DATE"] >= date1) & (df["DATE"] <= date2)].copy()

    st.write("Data Shape: ", df)

df = px.data.iris()
fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species")
st.plotly_chart(fig)
