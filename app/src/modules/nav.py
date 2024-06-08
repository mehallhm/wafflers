# Idea borrowed from https://github.com/fsmosca/sample-streamlit-authenticator

import streamlit as st

#### ------------------------ General ------------------------
def HomeNav():
    st.sidebar.page_link("App.py", label="Home")

def AboutPageNav():
    st.sidebar.page_link("pages/30_about.py", label="About")

# user role

def UserHomeNav():
    st.sidebar.page_link("pages/01_userhome.py", label="General User Home")

def UserSurveyNav():
    st.sidebar.page_link("pages/02_userSurvey.py", label="General User Survey")

def UserHistoryNav():
    st.sidebar.page_link("pages/03_userHistory.py", label="General User Survey History")

def UserMatchNav():
    st.sidebar.page_link("pages/04_userMatch.py", label="NGO Suggestions")

# enterprise role

def EnterpriseHomeNav():
    st.sidebar.page_link("pages/10_enterprisehome.py", label="Enterprise Home")

def EnterpriseMatchNav():
    st.sidebar.page_link("pages/12_enterpriseMatch.py", label="NGO Match")

def EnterpriseSurveyNav():
    st.sidebar.page_link("pages/11_enterpriseSurvey.py", label="Enterprise Survey")

def EnterpriseHistoryNav():
    st.sidebar.page_link("pages/13_enterpriseHistory.py", label="Enterprise Survey History")

# NGO role

def NGOHomeNav():
    st.sidebar.page_link("pages/20_NGOhome.py", label="NGO Home")

def NGOInfoNav():
    st.sidebar.page_link("pages/21_NGOInfo.py", label="NGO Info")

def NGOMatchNav():
    st.sidebar.page_link("pages/22_NGOMatch.py", label="Enterprise/User Match")    

# --------------------------------Links Function -----------------------------------------------
def SideBarLinks(show_home=False):
    """
    This function handles adding links to the sidebar of the app based upon the logged-in user's role, which was put in the streamlit session_state object when logging in. 
    """    

    # add a logo to the sidebar always
    # st.sidebar.image("assets/logo.png", width = 150)
    # add a logo to the sidebar always
    st.sidebar.image("assets/logo3.png", width = 150)
    # If there is no logged in user, redirect to the Home (Landing) page
    if 'authenticated' not in st.session_state:
        st.session_state.authenticated = False
        st.switch_page('App.py')
        

    # Show the other page navigators depending on the users' role.
    if st.session_state["authenticated"]:

        if st.session_state['role'] == 'General User':
            UserHomeNav()
            UserSurveyNav()
            UserHistoryNav()
            UserMatchNav()

        if st.session_state['role'] == 'Enterprise':
            EnterpriseHomeNav()
            EnterpriseMatchNav()
            EnterpriseSurveyNav()
            EnterpriseHistoryNav()
        
        if st.session_state['role'] == 'NGO':
            NGOHomeNav()
            NGOInfoNav()
            NGOMatchNav()

    if not st.session_state["authenticated"]:
        HomeNav()
    
    # Always show the About page at the bottom of the list of links
    AboutPageNav()

    if st.session_state["authenticated"]:
        # Always show a logout button if there is a logged in user
        if st.sidebar.button("Logout"):
            del st.session_state['role']
            del st.session_state['authenticated']
            st.switch_page('App.py')


