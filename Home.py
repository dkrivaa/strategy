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


st.write(st.session_state)
# df = pd.concat([st.session_state['dfe'], st.session_state['dfi']], axis=0)

# st.write(df)
# st.write(st.session_state['dfi'])
# st.write(st.session_state['dfe'])

engine.upload_file()

