import streamlit as st
from modules.nav import SideBarLinks
import requests
import validators
import json

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

col1, col2, col3 = st.columns(3)

with col1:
    st.write("Logged in as:")
    st.write("NGO")
    st.image('https://cdn-icons-png.freepik.com/256/3101/3101045.png?ga=GA1.1.1507691374.1717099387', width = 50)

st.write("# Account Info")
st.write("## Edit your account info")
st.write('')

NGO_name = st.text_input("NGO name")

def is_valid_url_with_tld(url, tld_list):
    if not url.startswith(('http://', 'https://')):
        url = 'http://' + url
    
    if validators.url(url):
        domain = url.split('/')[2]
        for tld in tld_list:
            if domain.endswith(tld):
                return True
    return False

Website_link = st.text_input("Website link:")

if Website_link:
    if is_valid_url_with_tld(Website_link, ['.com', '.gov', '.net', '.org', '.tv', '.cz', '.jp', '.de', '.br', '.edu']):
        st.success('Valid URL!')
    else:
        st.error('Invalid URL or TLD')

Contact_email = st.text_input("Head contact email:")

if Contact_email:
    if validators.email(Contact_email):
        st.success('Valid email address!')
    else:
        st.error('Invalid email address. Please enter a valid email.')

# Multiselect tags option
# options = ["Transport", "Flights", "Energy", "Heat"]

# selected_tags = st.multiselect("Select your associated tags", options)

# st.write("Selected tags:", selected_tags)


if st.button("Submit"):
    if NGO_name and is_valid_url_with_tld(Website_link, ['.com', '.gov', '.net', '.org', '.tv', '.cz', '.jp', '.de', '.br', '.edu']) and validators.email(Contact_email):
        
        api_url = "http://api:4000/n/NGOupdate"
        data = {
            "name": NGO_name,
            "website": Website_link,
            "email": Contact_email        }
                
        try:
            response = requests.put(api_url, json=data)
            
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
        st.error("Please fill in all the fields before submitting and have valid emails/urls")

st.write('## My NGO data')

data = {} 
try:
  data = requests.get('http://api:4000/n/ngomine').json()
except:
  st.write("**Important**: Could not connect to sample api, so using dummy data.")
  data = {"a":{"b": "123", "c": "hello"}, "z": {"b": "456", "c": "goodbye"}}


st.dataframe(data)

def add_tags():
    st.write('### Add New NGO Tags')

    options = ["Transport", "Flights", "Energy", "Heat"]

    selected_tags = st.selectbox("Select your associated tags", options)

    if st.button("Add Tags"):
        add_tags_api_url = "http://api:4000/n/NGOadd"
        tag_data = {"tag": selected_tags}
        try:
            response = requests.post(add_tags_api_url, json=tag_data)
            if response.status_code == 200:
                st.success("Tags successfully added!")
            else:
                st.error(f"Failed to add tags. Status code: {response.status_code}")
        except Exception as e:
            st.error(f"An error occurred while adding tags: {e}")
 
add_tags()
st.write("Display my current tags")
data = {} 
try:
  data = requests.get('http://api:4000/n/tags').json()
except:
  st.write("**Important**: Could not connect to sample api, so using dummy data.")
  data = {"a":{"b": "123", "c": "hello"}, "z": {"b": "456", "c": "goodbye"}}
st.dataframe(data)

def delete_tags():
    st.write('### Delete NGO Tags')

    options = ["Transport", "Flights", "Energy", "Heat"]

    selected_tag = st.selectbox("Select tags to delete", options)  

    if st.button("Delete Tags"):
        delete_tags_api_url = "http://api:4000/n/TagDelete"
        tag_data = {"tag": selected_tag}  

        try:
            response = requests.delete(delete_tags_api_url, json=tag_data)
            if response.status_code == 200:
                st.success("Tags successfully deleted!")
            
        except Exception as e:
            st.error(f"An error occurred while deleting tags: {e}")

delete_tags()

