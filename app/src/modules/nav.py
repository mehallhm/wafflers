# Idea borrowed from https://github.com/fsmosca/sample-streamlit-authenticator

import streamlit as st

#### ------------------------ General ------------------------
def HomeNav():
    st.sidebar.page_link("App.py", label="Home", icon='🏠')

def AboutPageNav():
    st.sidebar.page_link("pages/30_about.py", label="About")

def testAPINav():
    st.sidebar.page_link("pages/31_apiPage.py", label="Test API")

# user role

def UserHomeNav():
    st.sidebar.page_link("pages/01_userhome.py", label="General User Home")

def UserSurveyNav():
    st.sidebar.page_link("pages/02_userSurvey.py", label="General User Survey")

# enterprise role

def EnterpriseHomeNav():
    st.sidebar.page_link("pages/10_enterprisehome.py", label="Enterprise Home")

# NGO role

def NGOHomeNav():
    st.sidebar.page_link("pages/20_NGOhome.py", label="NGO home")

# --------------------------------Links Function -----------------------------------------------
def SideBarLinks(show_home=False):
    """
    This function handles adding links to the sidebar of the app based upon the logged-in user's role, which was put in the streamlit session_state object when logging in. 
    """    

    # add a logo to the sidebar always
    # st.sidebar.image("assets/logo.png", width = 150)

    # If there is no logged in user, redirect to the Home (Landing) page
    if 'authenticated' not in st.session_state:
        st.session_state.authenticated = False
        st.switch_page('App.py')
        
    if show_home:
        # Show the Home page link (the landing page)
        HomeNav()
        testAPINav()

    # Show the other page navigators depending on the users' role.
    if st.session_state["authenticated"]:

        if st.session_state['role'] == 'citizen':
            UserHomeNav()
            UserSurveyNav()

        if st.session_state['role'] == 'enterprise':
            EnterpriseHomeNav()
        
        if st.session_state['role'] == 'NGO':
            NGOHomeNav()

    
    # Always show the About page at the bottom of the list of links
    AboutPageNav()

    if st.session_state["authenticated"]:
        # Always show a logout button if there is a logged in user
        if st.sidebar.button("Logout"):
            del st.session_state['role']
            del st.session_state['authenticated']
            st.switch_page('App.py')

