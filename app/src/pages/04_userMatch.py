import streamlit as st
from modules.nav import side_bar_links
import requests

side_bar_links()

matches = requests.get("http://api:4000/n/NGOMatch/1?q=100", timeout=100).json()

st.header("My Matches")

for match in matches:
    st.divider()
    st.write(match["name"])
    st.write(match["website"])
