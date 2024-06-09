import streamlit as st
from modules.nav import SideBarLinks
import requests
import validators
from streamlit_pills import pills
import json

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

col1, col2, col3 = st.columns(3)

with col1:
    st.write("Logged In As:")
    st.write("NGO")
    st.image('assets/NGOicon.png', width = 50)

st.write("# Account Info")
st.write("### Edit Your Account Info")
st.write('')

NGO_name = st.text_input("NGO Name")

def is_valid_url_with_tld(url, tld_list):
    if not url.startswith(('http://', 'https://')):
        url = 'http://' + url
    
    if validators.url(url):
        domain = url.split('/')[2]
        for tld in tld_list:
            if domain.endswith(tld):
                return True
    return False

Website_link = st.text_input("Website Link:")

if Website_link:
    if is_valid_url_with_tld(Website_link, ['.com', '.gov', '.net', '.org', '.tv', '.cz', '.jp', '.de', '.br', '.edu']):
        st.success('Valid URL!')
    else:
        st.error('Invalid URL or TLD')

Contact_email = st.text_input("Head Contact Email:")

if Contact_email:
    if validators.email(Contact_email):
        st.success('Valid Email Address!')
    else:
        st.error('Invalid Email Address. Please Enter A Valid Email.')

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
                st.success("Data Successfully Inserted!")
            else:
                try:
                    error_message = response.json().get('error', 'No Error Message Provided')
                except json.JSONDecodeError:
                    error_message = response.text  # Raw response if not JSON
                
                st.error(f"Failed To Insert Data. Status Code: {response.status_code}, Error: {error_message}")
        except Exception as e:
            st.error(f"An Error Occurred: {e}")
    else:
        st.error("Please Fill In All The Fields Before Submitting And Have Valid Emails/Urls")

st.write('### My Current Data')

data = {} 
try:
    data = requests.get('http://api:4000/n/ngomine').json()
except:
    st.write("**Important**: Could Not Connect To Sample API, So Using Dummy Data.")
    data = {"a":{"b": "123", "c": "hello"}, "z": {"b": "456", "c": "goodbye"}}


# st.dataframe(data)



#data = {} 
#try:
def fetch_tag_descriptions():
    try:
        response = requests.get('http://api:4000/n/tags')  
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


# st.dataframe(data)

col1, col2 = st.columns(2)

with col1:
    def add_tags():
        st.write('### Add New NGO Tags')

        options = ["Transport", "Flights", "Energy", "Heat"]

        selected_tags = st.selectbox("Select Your Associated Tags", options)

        if st.button("Add Tags"):
            add_tags_api_url = "http://api:4000/n/NGOadd"
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
            delete_tags_api_url = "http://api:4000/n/TagDelete"
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


