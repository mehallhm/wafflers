import streamlit as st
from modules.nav import SideBarLinks

    
# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

("# Welcome, ", f"{st.session_state['first_name']}")

st.write("### Navigation")
col1, col2, col3 = st.columns(3)
with col1: 
    if st.button('## Update Profile Info'):
        st.switch_page('pages/21_NGOInfo.py')
with col2: 
    if st.button('## User/Enterprise Matches'):
        st.switch_page('pages/22_NGOMatch.py')

("#### Role:", f"{st.session_state['role']}")
