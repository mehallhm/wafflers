import streamlit as st
from modules.nav import SideBarLinks
import requests

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

st.write("# NGO suggestions")

st.write('')
st.write('')

st.write("## Your emission tags are: ")

data = {} 
try:
  data = requests.get('http://api:4000/e/tags').json()
except:
  st.write("**Important**: Could not connect to sample api, so using dummy data.")
  data = {"a":{"b": "123", "c": "hello"}, "z": {"b": "456", "c": "goodbye"}}

st.dataframe(data)

st.write("## NGOs with these tags are: ")

data = {} 
try:
  data = requests.get('http://api:4000/e/NGOMatch').json()
except:
  st.write("**Important**: Could not connect to sample api, so using dummy data.")
  data = {"a":{"b": "123", "c": "hello"}, "z": {"b": "456", "c": "goodbye"}}

st.dataframe(data)

st.write('## Comparison to average company in your country')

st.write('')

data = {} 
try:
  data = requests.get('http://api:4000/e/EntCompare').json()
except:
  st.write("**Important**: Could not connect to sample api, so using dummy data.")
  data = {"a":{"b": "123", "c": "hello"}, "z": {"b": "456", "c": "goodbye"}}

st.dataframe(data)