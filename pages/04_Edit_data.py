import streamlit as st

import engine

# Setting top of page
engine.home_title()

st.markdown(f'<span style="color: #ed7011; '
            f'font-size: 18px"><b>'
            f'Edit your data'
            f'</b></span>'
            , unsafe_allow_html=True)
st.markdown('___')

engine.edit_data()

