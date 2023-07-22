import pandas as pd
import streamlit as st

import engine

engine.home_title()
st.markdown(f'<span style="color: #ed7011; '
            f'font-size: 18px"><b>'
            f'Internal parameters affecting the organization'
            f'</b></span>'
            , unsafe_allow_html=True)
st.markdown('___')

st.markdown(f'<span style="color: #ed7011; '
            f'font-size: 14px"><b>'
            f'Enter up to 5 internal parameters'
            f'</b></span>'
            , unsafe_allow_html=True)

# Dataframe of internal parameters
dfi = engine.data_internal()

engine.dfi_none()

st.write(dfi)

