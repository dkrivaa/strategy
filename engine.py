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
    placeholder = st.empty()
    e_form = placeholder.form('external_vars')
    with e_form:
        st.write('**EXTERNAL** parameters')

        e_var1 = st.text_input('**#1**.')
        e_sig1 = st.radio('**Significance to organization**',
                          ['low', 'average', 'above average', 'high'],
                          index=3, horizontal=True, key='evar1')
        e_prob1 = st.slider('**probability**', min_value=0, max_value=100,
                            step=5, value=(45, 55), key='s_evar1')
        st.markdown('___')

        e_var2 = st.text_input('**#2**.')
        e_sig2 = st.radio('**Significance to organization**',
                          ['low', 'average', 'above average', 'high'],
                          index=3, horizontal=True, key='evar2')
        e_prob2 = st.slider('**probability**', min_value=0, max_value=100,
                            step=5, value=(45, 55), key='s_evar2')
        st.markdown('___')

        e_var3 = st.text_input('**#3**.')
        e_sig3 = st.radio('**Significance to organization**',
                          ['low', 'average', 'above average', 'high'],
                          index=3, horizontal=True, key='evar3')
        e_prob3 = st.slider('**probability**', min_value=0, max_value=100,
                            step=5, value=(45, 55), key='s_evar3')
        st.markdown('___')

        e_var4 = st.text_input('**#4**.')
        e_sig4 = st.radio('**Significance to organization**',
                          ['low', 'average', 'above average', 'high'],
                          index=3, horizontal=True, key='evar4')
        e_prob4 = st.slider('**probability**', min_value=0, max_value=100,
                            step=5, value=(45, 55), key='s_evar4')
        st.markdown('___')

        e_var5 = st.text_input('**#5**.')
        e_sig5 = st.radio('**Significance to organization**',
                          ['low', 'average', 'above average', 'high'],
                          index=3, horizontal=True, key='evar5')
        e_prob5 = st.slider('**probability**', min_value=0, max_value=100,
                            step=5, value=(45, 55), key='s_evar5')
        st.markdown('___')

        st.form_submit_button('Continue', type='primary')

    # e_var = []
    # e_var_sig = []
    # e_var_prob = []
    # for i in range(0, 5):
    #     e_var.append('e_var' + str(i))
    #     e_var_sig.append(('e_var' + str(i) + '_sig'))
    #     e_var_prob.append(('e_var' + str(i) + '_prob'))
    # dfe = pd.DataFrame({'e_var': e_var, 'e_var_sig': e_var_sig, 'e_var_prob': e_var_prob})


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


def data_input1():
    data = {'parameter': [], 'significance': [], 'probability_low': [],
            'probability_high': []}
    df = pd.DataFrame(data)

    if 'df' not in st.session_state:
        st.session_state.df = df

    df.loc[len(df)] = internal()

    st.write(df)


def internal():

    if 'num' not in st.session_state:
        st.session_state.num = 0

    st.write(st.session_state.num)

    placeholder = st.empty()
    num = st.session_state.num

    with placeholder.form(key=str(num)):
        parameter = st.text_input(f'parameter {num +1}', key=num+1)
        if parameter is None:
            parameter=0
        significance = st.radio('Significance to organization',
                                ['low', 'average', 'above average', 'high'],
                                index=3, horizontal=True, key=num+10)
        probability = st.slider('probability', min_value=0, max_value=100,
                                step=5, value=(45, 55), key=num+100)

        if st.form_submit_button():
            st.session_state.num += 1
            new_row = {'parameter': parameter,
                       'significance': significance,
                       'probability_low': probability[0],
                       'probability_high': probability[1]}
            if st.session_state.num >= 5:
                placeholder.empty()
        else:
            st.stop()
    st.write(st.session_state.num)

    return new_row





