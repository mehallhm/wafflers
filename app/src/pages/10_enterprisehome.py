import streamlit as st
from modules.nav import SideBarLinks

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

col1, col2, col3 = st.columns(3)

with col1:
    st.write("Logged in as:")
    st.write("Enterprise")
    st.image('https://cdn-icons-png.freepik.com/256/834/834504.png?ga=GA1.1.1507691374.1717099387', width = 50)

st.write("# To get started take the survey below")
st.write('')
st.write('')

if st.button('Take enterprise general emissions survey'):
    st.switch_page('pages/11_enterpriseSurvey.py')
