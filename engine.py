import streamlit as st


def home_title():
    st.set_page_config(page_title='Strategy',
                       layout='wide',)
    st.markdown(f'<span style="color: #18448c; '
                f'font-size: 32px"><b>Strategic Planning</b></span>'
                , unsafe_allow_html=True)
    st.markdown(f'<span style="color: #1f66db; '
                f'font-size: 18px"><b>Strategic Planning</b></span>'
                , unsafe_allow_html=True)
    st.markdown('___')