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
    col1, col2, col3 = st.columns([1, 1, 8])
    url1 = 'https://cdn0.iconfinder.com/data/icons/set-app-incredibles/24/Edit-01-48.png'
    url2 = 'https://cdn0.iconfinder.com/data/icons/phosphor-regular-vol-4/256/upload-simple-48.png'
    with col1:
        st.image(url1)
        st.button('Enter data')
    with col2:
        st.image(url2)
        st.button('Upload data file')

engine.upload_file()


df = engine.parameters()
st.data_editor(df)