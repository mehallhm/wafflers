import streamlit as st
from modules.nav import SideBarLinks

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

("# Welcome, ", f"{st.session_state['first_name']}")

st.write("### Navigation")
col1, col2, col3 = st.columns(3)
with col1: 
    if st.button('## Complete Emissions Survey'):
        st.switch_page('pages/11_enterpriseSurvey.py')
with col2: 
    if st.button('## View Emissions History'):
        st.switch_page('pages/13_enterpriseHistory.py')
with col3: 
    if st.button('## View NGO Recommendations'):
        st.switch_page('pages/04_enterpriseMatch.py')

("#### Role:", f"{st.session_state['role']}")