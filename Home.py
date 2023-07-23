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

if 'dfi' not in st.session_state:
    st.write('not in session_state')
else:
    st.write('dfi in session_state')
    st.write(st.session_state.dfi)
df = engine.parameters()
st.write(df)

engine.upload_file()

