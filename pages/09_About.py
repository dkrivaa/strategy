import streamlit as st

import engine

engine.home_title()
st.markdown(f'<span style="color: #ed7011; '
            f'font-size: 18px"><b>'
            f'About'
            f'</b></span>'
            , unsafe_allow_html=True)

engine.explanation()

