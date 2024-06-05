import streamlit as st
from modules.nav import SideBarLinks


st.session_state['authenticated'] = False
SideBarLinks(show_home=True)

def App():
    
    st.title('Welcome to Carbon Connect!')
    st.header('Choose your persona below')

    st.write('')

    # icons designed by freepik

    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("Act as Dave, a general user and citizen"):
          st.session_state['authenticated'] = True
          st.session_state['role'] = 'General User'
          st.session_state['first_name'] = 'Dave'
          st.switch_page("pages/01_userhome.py")
        st.image('https://cdn-icons-png.freepik.com/256/552/552848.png?ga=GA1.1.1507691374.1717099387', width = 100)

    with col2:
        if st.button("Act as Farm to Table, a medium sized business"):
          st.session_state['authenticated'] = True
          st.session_state['role'] = 'Enterprise'
          st.session_state['first_name'] = 'FarmtoTable'
          st.switch_page("pages/10_enterprisehome.py")
        st.image('https://cdn-icons-png.freepik.com/256/834/834504.png?ga=GA1.1.1507691374.1717099387', width = 100)

    with col3:
        if st.button("Act as NoEmissions, a transport emission NGO"):
          st.session_state['authenticated'] = True
          st.session_state['role'] = 'NGO'
          st.session_state['first_name'] = 'CarEmissions'
          st.switch_page("pages/20_NGOhome.py")
        st.image('https://cdn-icons-png.freepik.com/256/3101/3101045.png?ga=GA1.1.1507691374.1717099387', width = 100)


App()