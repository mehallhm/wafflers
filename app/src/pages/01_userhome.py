import streamlit as st
from modules.nav import SideBarLinks

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

col1, col2, col3 = st.columns(3)

with col1:
    st.write("Logged in as:")
    st.write(f"{st.session_state['role']} {st.session_state['first_name']}")
    st.image('assets/profile-user.png', width = 50)

st.write("# Navigate to your desired tool")
st.write('')
st.write('')

if st.button('Retake user general emissions survey'):
    st.switch_page('pages/02_userSurvey.py')
st.write('')
if st.button('See my survey history'):
    st.switch_page('pages/03_userHistory.py')
st.write('')
if st.button('See my NGO recommendations'):
    st.switch_page('pages/04_userMatch.py')
