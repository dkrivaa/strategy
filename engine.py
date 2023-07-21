import streamlit as st


def home_title():
    st.set_page_config(page_title='StraApp',
                       layout='wide',)
    st.markdown(f'<span style="color: #18448c; '
                f'font-size: 32px"><b>StraApp - Strategic Planning</b></span>'
                , unsafe_allow_html=True)
    st.markdown(f'<span style="color: #ed7011; '
                f'font-size: 18px"><b>'
                f'App to simplify strategic planning based on user defined parameters'
                f'</b></span>'
                , unsafe_allow_html=True)
    st.markdown('___')


def explanation():
    with st.container():
        st.write('Strategic planning is the cornerstone of any organizations '
                 'attempt to prepare for and embrace the opportunities and challenges '
                 'of the future. This significant process enables stakeholders '
                 'to define strategic goals, identify possible paths and facilitate '
                 'a proactive decision-making process.\nThis '
                 'App is intended to assist any organization, public or private, '
                 'to perform such a strategic process by identifying the main '
                 'areas that warrant attention and explicit strategic decisions '
                 'through development of various possible scenario designs.')


def external_variables():
    with st.container():
        st.write('Define up to 5 external factors that significantly affects '
                 'the organization:')
        e_var1 = st.text_input('#1', key='ext_var1')
        e_var2 = st.text_input('#2', key='ext_var2')
        st.session_state(e_var1, e_var2)


