import streamlit as st
from modules.nav import SideBarLinks

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

#greets the user with their first name stored in st.session state 
st.write("# Welcome, ", f"{st.session_state['first_name']}")

#navigation section of the code containing all navigation buttons on the home page 
st.write("### Navigation")
#three columns to organize the buttons side by side 
col1, col2, col3 = st.columns(3)
#Each column has a button that allows the user to navigate to a different page of the application
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