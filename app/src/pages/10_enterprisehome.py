import streamlit as st
from modules.nav import SideBarLinks

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

col1, col2, col3 = st.columns(3)

with col1:
    st.write("Logged in as:")
    st.write(f"{st.session_state['role']} {st.session_state['first_name']}")
    st.image('https://cdn-icons-png.freepik.com/256/834/834504.png?ga=GA1.1.1507691374.1717099387', width = 50)

st.write("# Navigate to your desired tool")
st.write('')
st.write('')

if st.button('Retake the enterprise general emissions survey'):
    st.switch_page('pages/11_enterpriseSurvey.py')
st.write('')
if st.button('See my survey history'):
    st.switch_page('pages/13_enterpriseHistory.py')
st.write('')
if st.button('See my tags, matches, and comparison to average country'):
    st.switch_page('pages/12_enterpriseMatch.py')
