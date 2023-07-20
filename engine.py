import streamlit as st


def home_title():
    st.set_page_config(page_title='Strategy',
                       layout='wide',)
    st.markdown(f'<span style="color: #18448c; '
                f'font-size: 32px"><b>Strategic Planning</b></span>'
                , unsafe_allow_html=True)
    st.markdown(f'<span style="color: #ed7011; '
                f'font-size: 18px"><b>'
                f'App to simplify strategic planning based on user defined parameters'
                f'</b></span>'
                , unsafe_allow_html=True)
    st.markdown('___')