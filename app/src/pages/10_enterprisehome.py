import streamlit as st
from modules.nav import side_bar_links

# Show appropriate sidebar links for the role of the currently logged in user
side_bar_links()

("# Welcome, ", f"{st.session_state['first_name']}")

st.write("### Navigation")
col1, col2 = st.columns(2)
with col1:
    if st.button("## Complete Emissions Survey"):
        st.switch_page("pages/11_enterpriseSurvey.py")

with col2:
    if st.button("## View NGO Recommendations"):
        st.switch_page("pages/12_enterpriseMatch.py")

("#### Role:", f"{st.session_state['role']}")

