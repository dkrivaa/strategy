import pandas as pd
import streamlit as st


import engine

# Setting top of page
engine.home_title()

st.markdown(f'<span style="color: #ed7011; '
            f'font-size: 18px"><b>'
            f'App to simplify strategic planning based on user defined parameters'
            f'</b></span>'
            , unsafe_allow_html=True)
st.markdown('___')

url1 = 'https://www.iconfinder.com/icons/115746/data_icon'
st.image(url1)


df = engine.parameters()
st.data_editor(df)

engine.upload_file()

