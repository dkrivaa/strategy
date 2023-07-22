import pandas as pd
import streamlit as st
from time import sleep


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


def data_external():
    # This function enables the user to enter data -
    # external variables affecting the organization
    with st.form('external_form'):

        parameter1 = st.text_input(f'**Parameter** #1', key='param1')
        if parameter1 is None:
            parameter1 = 0
        significance1 = st.radio('**Significance** to organization',
                                ['low', 'average', 'above average', 'high'],
                                 index=3, horizontal=True, key='sig1')
        probability1 = st.slider('**Probability**', min_value=0, max_value=100,
                                 step=5, value=(45, 55), key='prob1')
        st.markdown('___')

        parameter2 = st.text_input(f'**Parameter** #2', key='param2')
        if parameter2 is None:
            parameter2 = 0
        significance2 = st.radio('**Significance** to organization',
                                 ['low', 'average', 'above average', 'high'],
                                 index=3, horizontal=True, key='sig2')
        probability2 = st.slider('**Probability**', min_value=0, max_value=100,
                                 step=5, value=(45, 55), key='prob2')
        st.markdown('___')

        parameter3 = st.text_input(f'**Parameter** #3', key='param3')
        if parameter3 is None:
            parameter3 = 0
        significance3 = st.radio('**Significance** to organization',
                                 ['low', 'average', 'above average', 'high'],
                                 index=3, horizontal=True, key='sig3')
        probability3 = st.slider('**Probability**', min_value=0, max_value=100,
                                 step=5, value=(45, 55), key='prob3')
        st.markdown('___')

        parameter4 = st.text_input(f'**Parameter** #4', key='param4')
        if parameter4 is None:
            parameter4 = 0
        significance4 = st.radio('**Significance** to organization',
                                 ['low', 'average', 'above average', 'high'],
                                 index=3, horizontal=True, key='sig4')
        probability4 = st.slider('**Probability**', min_value=0, max_value=100,
                                 step=5, value=(45, 55), key='prob4')
        st.markdown('___')

        parameter5= st.text_input(f'**Parameter** #5', key='param5')
        if parameter5 is None:
            parameter5 = 0
        significance5 = st.radio('**Significance** to organization',
                                 ['low', 'average', 'above average', 'high'],
                                 index=3, horizontal=True, key='sig5')
        probability5 = st.slider('**Probability**', min_value=0, max_value=100,
                                 step=5, value=(45, 55), key='prob5')
        st.markdown('___')

        submit_external = st.form_submit_button(type='primary')

        if submit_external:
            parameter = [parameter1, parameter2, parameter3, parameter4, parameter5]
            significance = [significance1, significance2, significance3,
                            significance4, significance5]
            prob_low = [probability1[0], probability2[0], probability3[0],
                        probability4[0], probability5[0]]
            prob_high = [probability1[1], probability2[1], probability3[1],
                         probability4[1], probability5[1]]
            dfe = pd.DataFrame({'parameter': parameter,
                                'significance': significance,
                                'prob_low': prob_low,
                                'prob_high': prob_high})
    return dfe


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









    # if 'num' not in st.session_state:
    #     st.session_state.num = 0
    #
    # st.write(st.session_state.num)
    #
    # placeholder = st.empty()
    # num = st.session_state.num
    # test = [0, 1, 2, 3, 4]
    # for i in test:
    #     with placeholder.form(key=str(num + i)):
    #         st.text_input(f'test{num + 1}')
    #         st.slider('test')
    #
    #         if st.form_submit_button():
    #             st.session_state.num += 1
    #             if st.session_state.num >= 5:
    #                 st.session_state.num = 0
    #             placeholder.empty()
    #             sleep(0.01)
    #
    #     st.write(st.session_state.num)
    #
    #     return