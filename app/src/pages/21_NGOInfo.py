import streamlit as st
from modules.nav import SideBarLinks
import requests
import json

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

col1, col2, col3 = st.columns(3)

with col1:
    st.write("Logged in as:")
    st.write("NGO")
    st.image('https://cdn-icons-png.freepik.com/256/3101/3101045.png?ga=GA1.1.1507691374.1717099387', width = 50)

st.write("# To get started fill in the following information")

st.write('')

NGO_name = st.text_input("NGO name")

Website_link = st.text_input("Website link:")

Contact_email = st.text_input("Head contact email:")

# Multiselect tags option
options = ["Transport", "Flights", "Energy", "Heat"]

selected_tags = st.multiselect("Select your associated tags", options)

st.write("Selected tags:", selected_tags)


if st.button("Submit"):
    if NGO_name and Website_link and Contact_email:
        
        api_url = "http://api:4000/n/NGOadd"
        data = {
            "name": NGO_name,
            "website": Website_link,
            "email": Contact_email,
            "tags": selected_tags 
        }
                
        try:
            response = requests.post(api_url, json=data)
            
            if response.status_code == 201 or response.status_code == 200:
                st.success("Data successfully inserted!")
            else:
                try:
                    error_message = response.json().get('error', 'No error message provided')
                except json.JSONDecodeError:
                    error_message = response.text  # Raw response if not JSON
                
                st.error(f"Failed to insert data. Status code: {response.status_code}, Error: {error_message}")
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.error("Please fill in all the fields before submitting.")


if st.button('Proceed to tools'):
    st.switch_page('pages/22_NGOTools.py')
