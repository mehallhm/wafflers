import streamlit as st
from modules.nav import SideBarLinks
import requests
from streamlit_pills import pills
import pandas as pd

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

st.write("# Enterprise survey")

emission = st.text_input("Emissions in kilotonnes")

if st.button("Submit Emission"):
    url = "http://api:4000/e/EntResult"
    data = {"emission": emission}
    try:
        response = requests.post(url, json=data)
        if response.status_code == 200:
            st.success("Successfully Added!")
        else:
            st.error(f"Failed, Status Code: {response.status_code}")
    except Exception as e:
        st.error(f"An Error Occurred: {e}")


def fetch_tag_descriptions():
    try:
        response = requests.get('http://api:4000/e/tags')  
        response.raise_for_status()  
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching data: {e}")
        return []
    
data = fetch_tag_descriptions()

emoji_map = {
    "Heat": "🔥",
    "Flights": "🛫",
    "Energy": "💡",
    "Transport": "🚗",
}

tags = [tag["description"] for tag in data]

selected = pills('Current Tags', tags, [emoji_map[tag] for tag in tags])

col1, col2 = st.columns(2)

with col1:
    def add_tags():
        st.write('### Add New Enterprise Tags')

        options = ["Transport", "Flights", "Energy", "Heat"]

        selected_tags = st.selectbox("Select Your Associated Tags", options)

        if st.button("Add Tags"):
            add_tags_api_url = "http://api:4000/e/TagAdd"
            tag_data = {"tag": selected_tags}
            try:
                response = requests.post(add_tags_api_url, json=tag_data)
                if response.status_code == 200:
                    st.success("Tags Successfully Added!")
                else:
                    st.error(f"Failed To Add Tags. Status Code: {response.status_code}")
            except Exception as e:
                st.error(f"An Error Occurred While Adding Tags: {e}")

    add_tags()

with col2:
    def delete_tags():
        st.write('### Delete NGO Tags')

        options = ["Transport", "Flights", "Energy", "Heat"]

        selected_tag = st.selectbox("Select Tags To Delete", options)  

        if st.button("Delete Tags"):
            delete_tags_api_url = "http://api:4000/e/TagDelete"
            tag_data = {"tag": selected_tag}  

            try:
                response = requests.delete(delete_tags_api_url, json=tag_data)
                if response.status_code == 200:
                    st.success("Tags Successfully Deleted!")
                else:
                    st.error(f"Failed To Delete Tags. Status Code: {response.status_code}")
            except Exception as e:
                st.error(f"An Error Occurred While Deleting Tags: {e}")

    delete_tags()

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

st.write("#### In", country + ", your emissions in kilotonnes is ", round(your_emissions, 2), ", while the average enterprise's is ", round(avg_emission,2))
st.write("#### That means your emissions are", round(multiplier, 2), "times the average enterprise's emissions in " + country)

# st.write('### Display Enterprise Survey Result History')

# data = {}

# try:
#     data = requests.get('http://api:4000/e/EnterpriseHistory', timeout=100).json()
# except requests.exceptions.RequestException as e:
#     st.error(f"An error occurred: {e}")

# st.dataframe(data)


st.write('### Display Enterprise Survey Result History')




st.write('### Display Enterprise Survey Result History')

data = []

try:
    response = requests.get('http://api:4000/e/EnterpriseHistory', timeout=100)
    response.raise_for_status()
    data = response.json()
except requests.exceptions.RequestException as e:
    st.error(f"An error occurred: {e}")

if data:
    df = pd.DataFrame(data)
    
    display_option = st.selectbox(
        'Select how to display the data:',
        ('View entire history', 'Show one history result at a time')
    )

    if display_option == 'View entire history':
        st.dataframe(df)

    elif display_option == 'Show one history result at a time':
        for index, row in df.iterrows():
            with st.expander(f"Result {index + 1}"):
                st.write(row['emission_history'])
else:
    st.write("No data available to display.")

