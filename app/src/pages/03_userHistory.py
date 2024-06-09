import streamlit as st
from modules.nav import side_bar_links
import requests

# Show appropriate sidebar links for the role of the currently logged in user
side_bar_links()

st.title("Survey History")
st.write("##### Sorted by Completion Date")

outCol1, outCol2 = st.columns(2)
with outCol1:
    st.header("Residential Data")
    data = requests.get("http://api:4000/u/UserResidential", timeout=100).json()
    with st.expander("Electricity Usage"):
        for item in data:
            elec_usage = item["elec_usage"]
            fCol1, fCol2 = st.columns(2)
            with fCol1:
                st.write("Submission #", data.index(item))
            with fCol2:
                st.write(round(elec_usage / 0.0000036, 2), "kWh")
        st.bar_chart(data, y="elec_usage")

    with st.expander("Heating Data (only)"):
        for item in data:
            heating = item["heating"]
            inCol1, inCol2 = st.columns(2)
            with inCol1:
                st.write("Submission #", data.index(item))
            with inCol2:
                st.write(round(heating / 0.0000036, 2), "kWh")
        st.bar_chart(data, y="heating")
    with st.expander("Water Heating Data (only)"):
        for item in data:
            water_heating = item["water_heating"]
            inCol1, inCol2 = st.columns(2)
            with inCol1:
                st.write("Submission #", data.index(item))
            with inCol2:
                st.write(round(water_heating / 0.0000036, 2), "kWh")
        st.bar_chart(data, y="water_heating")
    with st.expander("Cooking Data"):
        for item in data:
            cooking = item["cooking_gas"]
            inCol1, inCol2 = st.columns(2)
            with inCol1:
                st.write("Submission #", data.index(item))
            with inCol2:
                st.write(round(cooking / 0.0000036, 2), "kWh")
        st.bar_chart(data, y="cooking_gas")

with outCol2:
    st.header("Car Data")
    data = requests.get("http://api:4000/u/UserCars", timeout=100).json()
    with st.expander("Fuel Type"):
        for item in data:
            fuel_type = item["fuel_type"]
            col1, col2 = st.columns(2)
            with col1:
                st.write("Submission #", data.index(item))
            with col2:
                st.write(fuel_type)

    with st.expander("Fuel Used"):
        for item in data:
            fuel_used = item["fuel_used"]
            col1, col2 = st.columns(2)
            with col1:
                st.write("Submission #", data.index(item))
            with col2:
                st.write(round(fuel_used / 1.1571e-6, 2), "liters")
        st.bar_chart(data, y="fuel_used")


# data = {}
# try:
#   data = requests.get('http://api:4000/u/UserFlights').json()
# except:
#   st.write("**Important**: Could not connect to sample api, so using dummy data.")
#   data = {"a":{"b": "123", "c": "hello"}, "z": {"b": "456", "c": "goodbye"}}

# st.dataframe(data)

# data = {}
# try:
#   data = requests.get('http://api:4000/u/UserTransport').json()
# except:
#   st.write("**Important**: Could not connect to sample api, so using dummy data.")
#   data = {"a":{"b": "123", "c": "hello"}, "z": {"b": "456", "c": "goodbye"}}

# st.dataframe(data)
