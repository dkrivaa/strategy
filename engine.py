import streamlit as st


def home_title():
    st.set_page_config(page_title='Strategy',
                       layout='wide',
                       page_icon='https://www.flaticon.com/free-icon/worldwide_7368309?term=globe&page=1&position=1&origin=search&related_id=7368309')
    st.markdown(f'<span style="color: #18448c; '
                f'font-size: 32px"><b>Strategic Planning</b></span>'
                , unsafe_allow_html=True)
    st.markdown(f'<span style="color: #18448c; '
                f'font-size: 18px"><b>Strategic Planning</b></span>'
                , unsafe_allow_html=True)
    st.markdown('___')