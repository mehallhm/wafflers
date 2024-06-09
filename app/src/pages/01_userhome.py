import streamlit as st
from modules.nav import side_bar_links

side_bar_links()

st.header(f"Welcome, {st.session_state['first_name']}")

st.write("### Navigation")

col1, col2, col3 = st.columns(3)
with col1:
    if st.button("## Take Emissions Survey"):
        st.switch_page("pages/02_userSurvey.py")

    st.write('')

    if st.button("## View Settings"):
        st.switch_page("pages/05_userSettings.py")

with col2:
    if st.button("## View Emissions History"):
        st.switch_page("pages/03_userHistory.py")

with col3:
    if st.button("## View NGO Recommendations"):
        st.switch_page("pages/04_userMatch.py")
