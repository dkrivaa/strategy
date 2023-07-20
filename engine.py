import streamlit as st


def home_title():
    st.set_page_config(page_title='Strategy',
                       layout='wide',
                       page_icon=':Globe:')
    st.markdown(f'<span style="color: #18448c; '
                f'font-size: 32px"><b>Strategic Planning</b></span>'
                , unsafe_allow_html=True)
    st.markdown('___')