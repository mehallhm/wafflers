import streamlit as st
from modules.nav import SideBarLinks

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

st.write("# Welcome, ", f"{st.session_state['first_name']}")

st.write("### Navigation")
col1, col2, col3 = st.columns(3)
with col1: 
    if st.button('## Take Emissions Survey'):
        st.switch_page('pages/02_userSurvey.py')
with col2: 
    if st.button('## View Emissions History'):
        st.switch_page('pages/03_userHistory.py')
with col3: 
    if st.button('## View NGO Recommendations'):
        st.switch_page('pages/04_userMatch.py')

("#### Role:", f"{st.session_state['role']}")