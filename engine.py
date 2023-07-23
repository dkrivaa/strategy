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

        parameter1 = st.text_input(f'**Parameter** #1', key='param1_e')
        if parameter1 is None:
            parameter1 = 0
        significance1 = st.radio('**Significance** to organization',
                                ['low', 'average', 'above average', 'high'],
                                 index=3, horizontal=True, key='sig1_e')
        probability1 = st.slider('**Probability**', min_value=0, max_value=100,
                                 step=5, value=(45, 55), key='prob1_e')
        st.markdown('___')

        parameter2 = st.text_input(f'**Parameter** #2', key='param2_e')
        if parameter2 is None:
            parameter2 = 0
        significance2 = st.radio('**Significance** to organization',
                                 ['low', 'average', 'above average', 'high'],
                                 index=3, horizontal=True, key='sig2_e')
        probability2 = st.slider('**Probability**', min_value=0, max_value=100,
                                 step=5, value=(45, 55), key='prob2_e')
        st.markdown('___')

        parameter3 = st.text_input(f'**Parameter** #3', key='param3_e')
        if parameter3 is None:
            parameter3 = 0
        significance3 = st.radio('**Significance** to organization',
                                 ['low', 'average', 'above average', 'high'],
                                 index=3, horizontal=True, key='sig3_e')
        probability3 = st.slider('**Probability**', min_value=0, max_value=100,
                                 step=5, value=(45, 55), key='prob3_e')
        st.markdown('___')

        parameter4 = st.text_input(f'**Parameter** #4', key='param4_e')
        if parameter4 is None:
            parameter4 = 0
        significance4 = st.radio('**Significance** to organization',
                                 ['low', 'average', 'above average', 'high'],
                                 index=3, horizontal=True, key='sig4_e')
        probability4 = st.slider('**Probability**', min_value=0, max_value=100,
                                 step=5, value=(45, 55), key='prob4_e')
        st.markdown('___')

        parameter5= st.text_input(f'**Parameter** #5', key='param5_e')
        if parameter5 is None:
            parameter5 = 0
        significance5 = st.radio('**Significance** to organization',
                                 ['low', 'average', 'above average', 'high'],
                                 index=3, horizontal=True, key='sig5_e')
        probability5 = st.slider('**Probability**', min_value=0, max_value=100,
                                 step=5, value=(45, 55), key='prob5_e')
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
    if dfe not in st.session_state:
        st.session_state.dfe = dfe
    return dfe


def data_internal():
    # This function enables the user to enter data -
    # internal variables affecting the organization

    with st.form('internal_form'):

        parameter1 = st.text_input(f'**Parameter** #1', key='param1_i')
        if parameter1 is None:
            parameter1 = 0
        significance1 = st.radio('**Significance** to organization',
                                ['low', 'average', 'above average', 'high'],
                                 index=3, horizontal=True, key='sig1_i')
        probability1 = st.slider('**Probability**', min_value=0, max_value=100,
                                 step=5, value=(45, 55), key='prob1_i')
        st.markdown('___')

        parameter2 = st.text_input(f'**Parameter** #2', key='param2_i')
        if parameter2 is None:
            parameter2 = 0
        significance2 = st.radio('**Significance** to organization',
                                 ['low', 'average', 'above average', 'high'],
                                 index=3, horizontal=True, key='sig2_i')
        probability2 = st.slider('**Probability**', min_value=0, max_value=100,
                                 step=5, value=(45, 55), key='prob2_i')
        st.markdown('___')

        parameter3 = st.text_input(f'**Parameter** #3', key='param3_i')
        if parameter3 is None:
            parameter3 = 0
        significance3 = st.radio('**Significance** to organization',
                                 ['low', 'average', 'above average', 'high'],
                                 index=3, horizontal=True, key='sig3_i')
        probability3 = st.slider('**Probability**', min_value=0, max_value=100,
                                 step=5, value=(45, 55), key='prob3_i')
        st.markdown('___')

        parameter4 = st.text_input(f'**Parameter** #4', key='param4_i')
        if parameter4 is None:
            parameter4 = 0
        significance4 = st.radio('**Significance** to organization',
                                 ['low', 'average', 'above average', 'high'],
                                 index=3, horizontal=True, key='sig4_i')
        probability4 = st.slider('**Probability**', min_value=0, max_value=100,
                                 step=5, value=(45, 55), key='prob4_i')
        st.markdown('___')

        parameter5 = st.text_input(f'**Parameter** #5', key='param5_i')
        if parameter5 is None:
            parameter5 = 0
        significance5 = st.radio('**Significance** to organization',
                                 ['low', 'average', 'above average', 'high'],
                                 index=3, horizontal=True, key='sig5_i')
        probability5 = st.slider('**Probability**', min_value=0, max_value=100,
                                 step=5, value=(45, 55), key='prob5_i')
        st.markdown('___')

        submit_internal = st.form_submit_button(type='primary')

        if submit_internal:
            parameter = [parameter1, parameter2, parameter3, parameter4, parameter5]
            significance = [significance1, significance2, significance3,
                            significance4, significance5]
            prob_low = [probability1[0], probability2[0], probability3[0],
                        probability4[0], probability5[0]]
            prob_high = [probability1[1], probability2[1], probability3[1],
                         probability4[1], probability5[1]]
            dfi = pd.DataFrame({'parameter': parameter,
                                'significance': significance,
                                'prob_low': prob_low,
                                'prob_high': prob_high})
    if 'dfi' not in st.session_state:
        st.session_state.dfi = dfi
    return dfi


def initial_dataframes():
    dfi = pd.DataFrame({'parameter': [],
                        'significance': [],
                        'prob_low': [],
                        'prob_high': []})
    dfe = pd.DataFrame({'parameter': [],
                        'significance': [],
                        'prob_low': [],
                        'prob_high': []})
    return dfe, dfi


def parameters():
    # Function that joins the dataframes for external and internal
    # parameters affecting the organization
    dfe = data_external()
    dfi = data_internal()
    df = pd.concat([dfe, dfi], axis=0)
    return df


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







