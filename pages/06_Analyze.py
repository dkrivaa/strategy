import streamlit as st

import engine

# Setting top of page
engine.home_title()

st.markdown(f'<span style="color: #ed7011; '
            f'font-size: 18px"><b>'
            f'Analyze your data'
            f'</b></span>'
            , unsafe_allow_html=True)
st.markdown('___')

url = 'https://cdn4.iconfinder.com/data/icons/success-filloutline/64/' \
      'chart-analysis-analytics-data_analytics-pie-48.png'

st.image(url)

engine.analyze()

