# Outlines NGO page navigation
import streamlit as st
from modules.nav import side_bar_links


# Show appropriate sidebar links for the role of the currently logged in user
side_bar_links()

("# Welcome, ", f"{st.session_state['first_name']}")

with st.container(border=True):
    st.write("### Navigation")
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("## Update Profile Info"):
            st.switch_page("pages/21_NGOInfo.py")
    with col2:
        if st.button("## User/Enterprise Matches"):
            st.switch_page("pages/22_NGOMatch.py")