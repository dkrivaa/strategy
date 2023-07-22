import pandas as pd
import streamlit as st

import engine

engine.home_title()
st.markdown(f'<span style="color: #ed7011; '
            f'font-size: 18px"><b>'
            f'External parameters affecting the organization'
            f'</b></span>'
            , unsafe_allow_html=True)
st.markdown('___')

st.markdown(f'<span style="color: #ed7011; '
            f'font-size: 14px"><b>'
            f'Enter up to 5 external parameters'
            f'</b></span>'
            , unsafe_allow_html=True)

# Dataframe of external parameters
dfe = engine.data_external()

engine.dfe_none()

st.write(dfe)

