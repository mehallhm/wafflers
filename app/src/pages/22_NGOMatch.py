import streamlit as st
from modules.nav import side_bar_links
import requests
from streamlit_pills import pills

# Show appropriate sidebar links for the role of the currently logged in user
side_bar_links()

st.write("# NGO suggestions")

st.write("")
st.write("")

st.write("## Your emission tags are: ")

data = {}
try:
    data = requests.get("http://api:4000/n/tags").json()
except:
    st.write("**Important**: Could not connect to sample api, so using dummy data.")
    data = {"a": {"b": "123", "c": "hello"}, "z": {"b": "456", "c": "goodbye"}}

emoji_map = {
    "Heat": "🔥",
    "Flights": "🛫",
    "Energy": "💡",
    "Transport": "🚗",
}

if data:
    tags = [tag["description"] for tag in data]
    selected = pills("Current Tags", tags, [emoji_map[tag] for tag in tags])
else:
    st.info("No tags available to display.")

st.write("## Enterprises with these tags are: ")

data = {}
try:
    data = requests.get("http://api:4000/n/EnterpriseMatch").json()
except:
    st.write("**Important**: Could not connect to sample api, so using dummy data.")
    data = {"a": {"b": "123", "c": "hello"}, "z": {"b": "456", "c": "goodbye"}}

transport = []
flights = []
energy = []
heat = []

for item in data:
    if item["description"] == "Transport":
        transport.append(item["name"])
    elif item["description"] == "Flights":
        flights.append(item["name"])
    elif item["description"] == "Energy":
        energy.append(item["name"])
    elif item["description"] == "Heat":
        heat.append(item["name"])

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

st.write("## Users you matched with")

data = {}
try:
    data = requests.get("http://api:4000/n/UserMatch").json()
except:
    st.write("**Important**: Could not connect to sample api, so using dummy data.")
    data = {"a": {"b": "123", "c": "hello"}, "z": {"b": "456", "c": "goodbye"}}

st.dataframe(data)

