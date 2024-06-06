import streamlit as st
from modules.nav import SideBarLinks

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

col1, col2, col3 = st.columns(3)

with col1:
    st.write("Logged in as:")
    st.write(f"{st.session_state['role']} {st.session_state['first_name']}")
    st.image('assets/NGOicon.png', width = 50)

st.write("# Navigate to your desired tool")
st.write('')
st.write('')

if st.button('Update NGO information questions'):
    st.switch_page('pages/21_NGOInfo.py')

st.write('')

if st.button('View my user and enterprise matches'):
    st.switch_page('pages/22_NGOMatch.py')
