import pandas as pd
import streamlit as st

my_file = st.file_uploader('Upload your **parameters** file (.csv)',type=['csv'])

df = pd.read_csv(my_file)

st.write(df)
