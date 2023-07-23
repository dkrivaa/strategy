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


with st.container():
    col1, col2, col3 = st.columns([1, 1, 10])
    url1 = 'https://cdn1.iconfinder.com/data/icons/unicons-line-vol-3/24/edit-48.png'
    url2 = 'https://cdn1.iconfinder.com/data/icons/unicons-line-vol-6/24/upload-48.png'
    with col1:
        st.image(url1)
        st.button('Enter data')
    with col2:
        st.image(url2)
        st.button('Upload data file')

engine.upload_file()


df = engine.parameters()
st.data_editor(df)