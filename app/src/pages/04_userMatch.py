import streamlit as st
from modules.nav import side_bar_links
import requests

side_bar_links()

matches = requests.get("http://api:4000/n/NGOMatch/1?q=100", timeout=500).json()

st.header("My Matches")
st.write("")

for match in matches:
    with st.container(border=True):
        st.write(f'### {match["name"]}')
        st.write(match["bio"])
        st.write(f'[Visit Site]({match["website"]})')
