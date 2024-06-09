"""
The Navbar element. Contains the logo as well as navigation links for all
user roles. Updates active links depedning on active roll

Idea borrowed from https://github.com/fsmosca/sample-streamlit-authenticator
"""

import streamlit as st


def side_bar_links():
    """
    This function handles adding links to the sidebar of the app based upon the logged-in
    user's role, which was put in the streamlit session_state object when logging in.
    """

    # add a logo to the sidebar always
    st.sidebar.image("assets/thin-logo.png", width=150)
    # If there is no logged in user, redirect to the Home (Landing) page
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False
        st.switch_page("App.py")

    # Show the other page navigators depending on the users' role.
    if st.session_state["authenticated"]:

        if st.session_state["role"] == "General User":
            st.sidebar.page_link("pages/01_userhome.py", label="Home")
            st.sidebar.page_link("pages/02_userSurvey.py", label="Survey")
            st.sidebar.page_link("pages/03_userHistory.py", label="Survey History")
            st.sidebar.page_link("pages/04_userMatch.py", label="NGO Suggestions")
            st.sidebar.page_link("pages/05_userSettings.py", label="Settings")

        if st.session_state["role"] == "Enterprise":
            st.sidebar.page_link("pages/10_enterprisehome.py", label="Home")
            st.sidebar.page_link("pages/12_enterpriseMatch.py", label="NGO Match")
            st.sidebar.page_link("pages/11_enterpriseSurvey.py", label="Survey")

        if st.session_state["role"] == "NGO":
            st.sidebar.page_link("pages/20_NGOhome.py", label="Home")
            st.sidebar.page_link("pages/21_NGOInfo.py", label="Info")
            st.sidebar.page_link("pages/22_NGOMatch.py", label="Enterprise/User Match")

    if not st.session_state["authenticated"]:
        st.sidebar.page_link("App.py", label="Home")

    # Always show the About page at the bottom of the list of links
    st.sidebar.page_link("pages/30_about.py", label="About")

    if st.session_state["authenticated"]:
        # Always show a logout button if there is a logged in user
        if st.sidebar.button("Logout"):
            del st.session_state["role"]
            del st.session_state["authenticated"]
            st.switch_page("App.py")
