import streamlit as st
from modules.nav import SideBarLinks


st.session_state['authenticated'] = False
SideBarLinks(show_home=True)

def App():
    
    st.title('Welcome to Carbon Connect!')
    st.header('Act as...')

    st.write('')

    # icons designed by freepik

    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("Natalie Allard"):
          st.session_state['authenticated'] = True
          st.session_state['role'] = 'General User'
          st.session_state['first_name'] = 'Natalie'
          st.switch_page("pages/01_userhome.py")
        st.image('assets/profile-user.png', width = 90)


    with col2:
        if st.button("EcoForward Enterprises"):
          st.session_state['authenticated'] = True
          st.session_state['role'] = 'Enterprise'
          st.session_state['first_name'] = 'EcoForward'
          st.switch_page("pages/10_enterprisehome.py")
        st.image('assets/suitcase.png', width = 90)

    with col3:
        if st.button("EcoUnity Europe"):
          st.session_state['authenticated'] = True
          st.session_state['role'] = 'NGO'
          st.session_state['first_name'] = 'EcoUnity'
          st.switch_page("pages/20_NGOhome.py")
        st.image('assets/NGOicon.png', width = 100)


App()