import streamlit as st


def home_title():
    url = icon()
    st.set_page_config(page_title='StraApp',
                       layout='wide',
                       page_icon=url)
    st.image(url)
    st.markdown(f'<span style="color: #4b7fd1; '
                f'font-size: 24px"><b>StraApp - Strategic Planning</b></span>'
                , unsafe_allow_html=True)



def icon():
    url = 'https://cdn4.iconfinder.com/data/icons/success-filloutline/64/jigsaws-puzzle_pieces-planning-creative-strategy-128.png'
    return url

def page_title():
    url = icon()
    st.image(url)
    st.markdown(f'<span style="color: #18448c; '
                f'font-size: 32px"><b>StraApp - Strategic Planning</b></span>'
                , unsafe_allow_html=True)




def explanation():
    with st.container():
        st.write('Strategic planning is the cornerstone of any organizations '
                 'attempt to prepare for and embrace the opportunities and challenges '
                 'of the future. This significant process enables stakeholders '
                 'to define strategic goals, identify possible paths and facilitate '
                 'a proactive decision-making process.\nThis '
                 'App is intended to assist any organization, public or private, '
                 'to perform such a strategic process by:'
                 )
        st.write('*  identifying the main areas that warrant attention')
        st.write('* develop possible scenario designs')
        st.write('* promote explicit strategic decisions')



def external_variables():
    # This function gets up to 5 external factors that significantly affects '
    #                  'the organizations ability to execute its mission statement
    with st.container():
        st.write('Define up to 5 external factors that significantly affects '
                 'the organizations ability to execute its mission statement:')
        # st.text_input('#1', key='ext_var1')
        # st.text_input('#2', key='ext_var2')
        # st.text_input('#3', key='ext_var3')


def upload_file():
    with st.container():
        user_file = st.file_uploader('Upload your file (.xlsx or .csv)',
                                     type=['xlsx', 'csv'])


