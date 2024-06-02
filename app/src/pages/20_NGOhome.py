import streamlit as st
from modules.nav import SideBarLinks

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

col1, col2, col3 = st.columns(3)

with col1:
    st.write("Logged in as:")
    st.write("NGO")
    st.image('https://cdn-icons-png.freepik.com/256/3101/3101045.png?ga=GA1.1.1507691374.1717099387', width = 50)

st.write("# To get started we need some information from you")
st.write('')
st.write('')

if st.button('NGO information questions'):
    st.switch_page('pages/21_NGOInfo.py')
