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

transport = []
flights = []
energy = []
heat = []

for item in data:
    if item['description'] == 'Transport':
        transport.append(item['name'])
    elif item['description'] == 'Flights':
        flights.append(item['name'])
    elif item['description'] == 'Energy':
        energy.append(item['name'])
    elif item['description'] == 'Heat':
        heat.append(item['name'])

with st.expander("Transport NGOs", expanded=False):
    st.write("#### NGO list:")
    st.markdown("- " + "\n- ".join(transport))

with st.expander("Flights NGOs", expanded=False):
    st.write("#### NGO list:")
    st.markdown("- " + "\n- ".join(flights))

with st.expander("Energy NGOs", expanded=False):
    st.write("#### NGO list:")
    st.markdown("- " + "\n- ".join(energy))

with st.expander("Heat NGOs", expanded=False):
    st.write("#### NGO list:")
    st.markdown("- " + "\n- ".join(heat))

data = {} 
try:
  data = requests.get('http://api:4000/e/EntCompare').json()
except:
  st.write("**Important**: Could not connect to sample api, so using dummy data.")
  data = {"a":{"b": "123", "c": "hello"}, "z": {"b": "456", "c": "goodbye"}}

avg_emission = data[0]["AVG Emission (by Country in kilotonnes)"]
country = data[0]["Country"]
your_emissions = data[0]["Your Emissions (in kilotonnes)"]
multiplier = your_emissions / avg_emission

st.write('')

if st.button("View comparison"):
   st.write("#### In", country + ", your emissions in kilotonnes is ", your_emissions, ", while the average enterprise's is ", avg_emission)
   st.write("#### That means your emissions are", multiplier, "times the average enterprise's emissions in " + country)

