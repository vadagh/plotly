import streamlit as st
#import plotly
import plotly.express as px
import pandas as pd
import warnings
import sys
print(sys.executable)
st.write("Python executable used by Streamlit:")
st.code(sys.executable)

warnings.filterwarnings('ignore')

df = px.data.iris()
fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species")
st.plotly_chart(fig)
#fig.show()