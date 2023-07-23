import streamlit as st

import engine

engine.home_title()
st.markdown(f'<span style="color: #ed7011; '
            f'font-size: 18px"><b>'
            f'Influencers - factors affecting strategic parameters influenced by organizations decisions'
            f'</b></span>'
            , unsafe_allow_html=True)
st.markdown('___')

st.markdown(f'<span style="color: #ed7011; '
            f'font-size: 14px"><b>'
            f'Enter up to 3 influencers for each parameter'
            f'</b></span>'
            , unsafe_allow_html=True)
