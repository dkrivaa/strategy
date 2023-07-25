import pandas as pd
import streamlit as st
# from streamlit_extras.switch_page_button import switch_page

# TITLES AND HOME
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


def home_menu():
    # with st.container():
    #     url1 = 'https://cdn4.iconfinder.com/data/icons/evil-icons-user-interface/64/arrow_right-64.png'
    #     st.image(url1)
    #
    #     st.markdown(f'<span style="color: #4b7fd1; '
    #                 f'font-size: 18px"><b>Data  **  Analyze  **  Results</b></span>'
    #                 , unsafe_allow_html=True)
    # st.markdown('___')

    with st.container():
        url2 = 'https://cdn1.iconfinder.com/data/icons/unicons-line-vol-3/24/edit-48.png'
        url3 = 'https://cdn1.iconfinder.com/data/icons/unicons-line-vol-6/24/upload-48.png'
        st.image(url2)
        if st.button('Enter data'):
            st.success("Press 'Enter External Parameters' on sidebar")

        st.image(url3)
        upload_file()
        # st.write(st.session_state)
    save_file()


def save_file():
    # Function to save and download datafile in csv format
    if 'df' in st.session_state:
        df = st.session_state.df
        csv = df.to_csv(index=False)

        st.sidebar.markdown(f'<span style="color: #f0410c; '
                    f'font-size: 16px"><b>Download and save data</b></span>'
                    , unsafe_allow_html=True)
        st.sidebar.download_button('Press to download',
                                   data=csv,
                                   file_name='my_data.csv',
                                   )

    else:
        pass


# ENTERING, UPLOADING AND EDITING DATA
def data_external():
    # This function enables the user to enter data -
    # external variables affecting the organization

    dfe = initial_dfe()

    with st.form('external_form'):

        parameter1 = st.text_input(f'**Parameter** #1', key='param1_e')
        if parameter1 is None:
            parameter1 = 0
        significance1 = st.radio('**Significance** to organization',
                                ['average', 'above average', 'high', 'very high'],
                                 index=3, horizontal=True, key='sig1_e')
        probability1 = st.slider('**Probability**', min_value=0, max_value=100,
                                 step=5, value=(45, 55), key='prob1_e')
        influencer11 = st.text_input('**Influencer** #1', key='inf11_e')
        influencer12 = st.text_input('**Influencer** #2', key='inf12_e')
        influencer13 = st.text_input('**Influencer** #3', key='inf13_e')
        st.markdown('___')

        parameter2 = st.text_input(f'**Parameter** #2', key='param2_e')
        if parameter2 is None:
            parameter2 = 0
        significance2 = st.radio('**Significance** to organization',
                                 ['average', 'above average', 'high', 'very high'],
                                 index=3, horizontal=True, key='sig2_e')
        probability2 = st.slider('**Probability**', min_value=0, max_value=100,
                                 step=5, value=(45, 55), key='prob2_e')
        influencer21 = st.text_input('**Influencer** #1', key='inf21_e')
        influencer22 = st.text_input('**Influencer** #2', key='inf22_e')
        influencer23 = st.text_input('**Influencer** #3', key='inf23_e')
        st.markdown('___')

        parameter3 = st.text_input(f'**Parameter** #3', key='param3_e')
        if parameter3 is None:
            parameter3 = 0
        significance3 = st.radio('**Significance** to organization',
                                 ['average', 'above average', 'high', 'very high'],
                                 index=3, horizontal=True, key='sig3_e')
        probability3 = st.slider('**Probability**', min_value=0, max_value=100,
                                 step=5, value=(45, 55), key='prob3_e')
        influencer31 = st.text_input('**Influencer** #1', key='inf31_e')
        influencer32 = st.text_input('**Influencer** #2', key='inf32_e')
        influencer33 = st.text_input('**Influencer** #3', key='inf33_e')
        st.markdown('___')

        parameter4 = st.text_input(f'**Parameter** #4', key='param4_e')
        if parameter4 is None:
            parameter4 = 0
        significance4 = st.radio('**Significance** to organization',
                                 ['average', 'above average', 'high', 'very high'],
                                 index=3, horizontal=True, key='sig4_e')
        probability4 = st.slider('**Probability**', min_value=0, max_value=100,
                                 step=5, value=(45, 55), key='prob4_e')
        influencer41 = st.text_input('**Influencer** #1', key='inf41_e')
        influencer42 = st.text_input('**Influencer** #2', key='inf42_e')
        influencer43 = st.text_input('**Influencer** #3', key='inf43_e')
        st.markdown('___')

        parameter5= st.text_input(f'**Parameter** #5', key='param5_e')
        if parameter5 is None:
            parameter5 = 0
        significance5 = st.radio('**Significance** to organization',
                                 ['average', 'above average', 'high', 'very high'],
                                 index=3, horizontal=True, key='sig5_e')
        probability5 = st.slider('**Probability**', min_value=0, max_value=100,
                                 step=5, value=(45, 55), key='prob5_e')
        influencer51 = st.text_input('**Influencer** #1', key='inf51_e')
        influencer52 = st.text_input('**Influencer** #2', key='inf52_e')
        influencer53 = st.text_input('**Influencer** #3', key='inf53_e')
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
            influencer1 = [influencer11, influencer21, influencer31, influencer41,
                           influencer51]
            influencer2 = [influencer12, influencer22, influencer32, influencer42,
                           influencer52]
            influencer3 = [influencer13, influencer23, influencer33, influencer43,
                           influencer53]
            dfe = pd.DataFrame({'parameter': parameter,
                                'significance': significance,
                                'prob_low': prob_low,
                                'prob_high': prob_high,
                                'influencer1': influencer1,
                                'influencer2': influencer2,
                                'influencer3': influencer3})
    if dfe not in st.session_state:
        st.session_state.dfe = dfe
    else:
        st.session_state.dfe = dfe

    # Adding dfi (internal parameters) if does not exist in session.state
    if 'dfi' not in st.session_state:
        dfi = initial_dfi()
        st.session_state.dfi = dfi

    parameters()

    return dfe


def data_internal():
    # This function enables the user to enter data -
    # internal variables affecting the organization

    dfi = initial_dfi()

    with st.form('internal_form'):

        parameter1 = st.text_input(f'**Parameter** #1', key='param1_i')
        if parameter1 is None:
            parameter1 = 0
        significance1 = st.radio('**Significance** to organization',
                                ['average', 'above average', 'high', 'very high'],
                                 index=3, horizontal=True, key='sig1_i')
        probability1 = st.slider('**Probability**', min_value=0, max_value=100,
                                 step=5, value=(45, 55), key='prob1_i')
        influencer11 = st.text_input('**Influencer** #1', key='inf11_i')
        influencer12 = st.text_input('**Influencer** #2', key='inf12_i')
        influencer13 = st.text_input('**Influencer** #3', key='inf13_i')
        st.markdown('___')

        parameter2 = st.text_input(f'**Parameter** #2', key='param2_i')
        if parameter2 is None:
            parameter2 = 0
        significance2 = st.radio('**Significance** to organization',
                                 ['average', 'above average', 'high', 'very high'],
                                 index=3, horizontal=True, key='sig2_i')
        probability2 = st.slider('**Probability**', min_value=0, max_value=100,
                                 step=5, value=(45, 55), key='prob2_i')
        influencer21 = st.text_input('**Influencer** #1', key='inf21_i')
        influencer22 = st.text_input('**Influencer** #2', key='inf22_i')
        influencer23 = st.text_input('**Influencer** #3', key='inf23_i')
        st.markdown('___')

        parameter3 = st.text_input(f'**Parameter** #3', key='param3_i')
        if parameter3 is None:
            parameter3 = 0
        significance3 = st.radio('**Significance** to organization',
                                 ['average', 'above average', 'high', 'very high'],
                                 index=3, horizontal=True, key='sig3_i')
        probability3 = st.slider('**Probability**', min_value=0, max_value=100,
                                 step=5, value=(45, 55), key='prob3_i')
        influencer31 = st.text_input('**Influencer** #1', key='inf31_i')
        influencer32 = st.text_input('**Influencer** #2', key='inf32_i')
        influencer33 = st.text_input('**Influencer** #3', key='inf33_i')
        st.markdown('___')

        parameter4 = st.text_input(f'**Parameter** #4', key='param4_i')
        if parameter4 is None:
            parameter4 = 0
        significance4 = st.radio('**Significance** to organization',
                                 ['average', 'above average', 'high', 'very high'],
                                 index=3, horizontal=True, key='sig4_i')
        probability4 = st.slider('**Probability**', min_value=0, max_value=100,
                                 step=5, value=(45, 55), key='prob4_i')
        influencer41 = st.text_input('**Influencer** #1', key='inf41_i')
        influencer42 = st.text_input('**Influencer** #2', key='inf42_i')
        influencer43 = st.text_input('**Influencer** #3', key='inf43_i')
        st.markdown('___')

        parameter5 = st.text_input(f'**Parameter** #5', key='param5_i')
        if parameter5 is None:
            parameter5 = 0
        significance5 = st.radio('**Significance** to organization',
                                 ['average', 'above average', 'high', 'very high'],
                                 index=3, horizontal=True, key='sig5_i')
        probability5 = st.slider('**Probability**', min_value=0, max_value=100,
                                 step=5, value=(45, 55), key='prob5_i')
        influencer51 = st.text_input('**Influencer** #1', key='inf51_i')
        influencer52 = st.text_input('**Influencer** #2', key='inf52_i')
        influencer53 = st.text_input('**Influencer** #3', key='inf53_i')
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
            influencer1 = [influencer11, influencer21, influencer31, influencer41,
                           influencer51]
            influencer2 = [influencer12, influencer22, influencer32, influencer42,
                           influencer52]
            influencer3 = [influencer13, influencer23, influencer33, influencer43,
                           influencer53]
            dfi = pd.DataFrame({'parameter': parameter,
                                'significance': significance,
                                'prob_low': prob_low,
                                'prob_high': prob_high,
                                'influencer1': influencer1,
                                'influencer2': influencer2,
                                'influencer3': influencer3})
    if 'dfi' not in st.session_state:
        st.session_state.dfi = dfi
    else:
        st.session_state.dfi = dfi

    parameters()

    return dfi


def initial_dfe():
    dfe = pd.DataFrame({'parameter': [],
                        'significance': ['very high', 'very high', 'very high', 'very high', 'very high'],
                        'prob_low': [45, 45, 45, 45, 45],
                        'prob_high': [55, 55, 55, 55, 55],
                        'influencer1': [],
                        'influencer2': [],
                        'influencer3': []})
    return dfe


def initial_dfi():
    dfi = pd.DataFrame({'parameter': [],
                        'significance': ['very high', 'very high', 'very high', 'very high', 'very high'],
                        'prob_low': [45, 45, 45, 45, 45],
                        'prob_high': [55, 55, 55, 55, 55],
                        'influencer1': [],
                        'influencer2': [],
                        'influencer3': []})
    return dfi


def parameters():
    # Function that joins the dataframes for external and internal
    # parameters affecting the organization
    if 'dfe' in st.session_state and 'dfi' in st.session_state:
        df = pd.concat([st.session_state['dfe'], st.session_state['dfi']], axis=0)
    elif 'dfe' not in st.session_state and 'dfi' not in st.session_state:
        dfe = pd.DataFrame({'parameter': [],
                            'significance': [],
                            'prob_low': [],
                            'prob_high': [],
                            'influencer1': [],
                            'influencer2': [],
                            'influencer3': []})
        dfi = pd.DataFrame({'parameter': [],
                            'significance': [],
                            'prob_low': [],
                            'prob_high': [],
                            'influencer1': [],
                            'influencer2': [],
                            'influencer3': []})
        df = pd.concat([dfe, dfi], axis=0)
    elif 'dfe' not in st.session_state and 'dfi' in st.session_state:
        dfe = pd.DataFrame({'parameter': [],
                            'significance': [],
                            'prob_low': [],
                            'prob_high': [],
                            'influencer1': [],
                            'influencer2': [],
                            'influencer3': []})
        df = pd.concat([dfe, st.session_state.dfi], axis=0)
    elif 'dfe' in st.session_state and 'dfi' not in st.session_state:
        dfi = pd.DataFrame({'parameter': [],
                            'significance': [],
                            'prob_low': [],
                            'prob_high': [],
                            'influencer1': [],
                            'influencer2': [],
                            'influencer3': []})
        df = pd.concat([st.session_state.dfe, dfi], axis=0)
    else:
        df = None
        st.warning('Something is wrong')

    if df is not None:
        if 'df' not in st.session_state:
            st.session_state.df = df
        elif 'df' in st.session_state:
            st.session_state.df = df

    return df


def upload_file():
    with st.container():
        # upload file containing internal and external parameters affecting the organization
        my_file = st.file_uploader('Upload your **parameters** file (.csv)', type=['csv'])
        if my_file is not None:

            # Make dataframe from uploaded file
            df = pd.read_csv(my_file)
            if 'df' not in st.session_state:
                st.session_state.df = df
            else:
                st.session_state.df = df

            # checking to make sure uploaded file is ok
            column_list = df.columns.tolist()
            if column_list == ['parameter', 'significance', 'prob_low',
                              'prob_high', 'influencer1', 'influencer2', 'influencer3']:
                if len(df) <= 10:
                    st.success("Your file was uploaded successfully. To edit your data go to 'Edit data' page")
            else:
                st.warning('Your file is not in the correct layout')


def edit_data():
    # Defining df - from uploaded file or from data entering
    if 'df' in st.session_state:
        df = st.session_state.df
    else:
        df = parameters()

    # if df is empty
    if df.shape == (0, 0):
        st.warning('There is no data. Please enter data on relevant pages')

    df = st.data_editor(data=df, column_config={
                                            'significance': st.column_config.SelectboxColumn(
                                               'significance',
                                               options=['average', 'above average', 'high', 'very high']),
                                            'prob_low': st.column_config.SelectboxColumn(
                                                options=range(0, 100, 5)),
                                            'prob_high': st.column_config.SelectboxColumn(
                                                options=range(0, 100, 5)),
                                            },
                                     hide_index=True)

    st.session_state.df = df
# ABOUT
def explanation():
    # This function presents the info on the 'About' page
    with st.container():
        st.write('Strategic planning is the cornerstone of any organizations '
                 'attempt to prepare for and embrace the opportunities and challenges '
                 'of the future. This significant process enables stakeholders '
                 'to define strategic goals, identify possible paths and facilitate '
                 'a proactive decision-making process. This '
                 'App is intended to assist any organization, public or private, '
                 'to perform such a strategic process by:')
        st.write('* identifying the main areas that warrant attention')
        st.write('* develop possible scenario designs')
        st.write('* promote explicit strategic decisions')
        st.markdown('___')

        st.write('Terminology:')
        st.write('EXTERNAL PARAMETERS: Exogenous factors which significantly '
                 'affect the organizations ability to achieve its vision and mission. '
                 'The organization have little or no influence on these parameters.')
        st.write('INTERNAL PARAMETERS: Parameters within the scope of influence by the '
                 'organization which significantly affect the organizations '
                 'ability to achieve its vision and mission.')
        st.write('INFLUENCERS: Variables subject to decisions by the organization '
                 'that can influence the ability to cope with / exploit the challenges and '
                 'opportunities presented by the external and internal parameters.')
        st.markdown('___')






