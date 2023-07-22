import pandas as pd
import streamlit as st


def home_title():
    # This function sets the generale outlay of page and the top banner
    url = icon()
    st.set_page_config(page_title='StraApp',
                       layout='wide',
                       page_icon=url)
    st.image(url)
    st.markdown(f'<span style="color: #4b7fd1; '
                f'font-size: 24px"><b>StraApp - Strategic Planning</b></span>'
                , unsafe_allow_html=True)



def icon():
    url = 'https://cdn4.iconfinder.com/data/icons/success-filloutline/64/' \
          'jigsaws-puzzle_pieces-planning-creative-strategy-128.png'
    return url


def data_input():
    # This function enables the user to enter data -
    # external and internal variables affecting the organization
    if 'num' not in st.session_state:
        st.session_state.num = 0

    st.write(st.session_state.num)

    placeholder = st.empty()
    num = st.session_state.num

    with placeholder.form(key=str(num)):
        st.text_input(f'test{num + 1}')
        st.slider('test')

        if st.form_submit_button():
            st.session_state.num += 1
            if st.session_state.num >= 5:
                return
        else:
            return

        st.write(st.session_state.num)


    # parameter = st.text_input(f'parameter {num +1}', key=num+1)
    #         if parameter is None:
    #             parameter = 0
    #         significance = st.radio('Significance to organization',
    #                                 ['low', 'average', 'above average', 'high'],
    #                                 index=3, horizontal=True, key=num+10)
    #         probability = st.slider('probability', min_value=0, max_value=100,
    #                                 step=5, value=(45, 55), key=num+100)


def upload_file():
    with st.container():
        user_file = st.file_uploader('Upload your file (.xlsx or .csv)',
                                     type=['xlsx', 'csv'])


def explanation():
    # This function presents the info on the 'About' page
    with st.container():
        st.write('Strategic planning is the cornerstone of any organizations '
                 'attempt to prepare for and embrace the opportunities and challenges '
                 'of the future. This significant process enables stakeholders '
                 'to define strategic goals, identify possible paths and facilitate '
                 'a proactive decision-making process. This '
                 'App is intended to assist any organization, public or private, '
                 'to perform such a strategic process by:'
                 )
        st.write('* identifying the main areas that warrant attention')
        st.write('* develop possible scenario designs')
        st.write('* promote explicit strategic decisions')









