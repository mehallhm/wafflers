import streamlit as st
from modules.nav import SideBarLinks
import requests

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

matches = requests.get("http://api:4000/n/NGOMatch/1?q=100", timeout=100).json()

st.header("My Matches")

for match in matches:
    with st.container(border=True):
        st.write(match)

