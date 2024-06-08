import streamlit as st
from modules.nav import SideBarLinks
import requests
import json
from streamlit_pills import pills


# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

st.header("My Settings")
country = st.selectbox(
    "Country :flag-eu:",
    ("Belgium 🇧🇪", "Bulgaria 🇧🇬", "Croatia 🇭🇷", "Cyprus 🇨🇾", "Czechia 🇨🇿", "Denmark 🇩🇰", 
     "Estonia 🇪🇪", "Finland 🇫🇮", "France 🇫🇷", "Germany 🇩🇪", "Greece 🇬🇷", "Hungary 🇭🇺", "Ireland 🇮🇪", 
     "Italy 🇮🇹", "Latvia 🇱🇻", "Lithuania 🇱🇹", "Luxembourg 🇱🇺", "Malta 🇲🇹", "Netherlands 🇳🇱", "Poland 🇵🇱", 
     "Portugal 🇵🇹", "Romania 🇷🇴", "Slovakia 🇸🇰", "Slovenia 🇸🇮", "Spain 🇪🇸", "Sweden 🇸🇪", "Iceland 🇮🇸", 
     "Liechtenstein 🇱🇮", "Norway 🇳🇴", "Switzerland 🇨🇭"))
st.write("You selected:", country)
country_id = [
    "Belgium 🇧🇪", "Bulgaria 🇧🇬", "Croatia 🇭🇷", "Cyprus 🇨🇾", "Czechia 🇨🇿", "Denmark 🇩🇰", 
    "Estonia 🇪🇪", "Finland 🇫🇮", "France 🇫🇷", "Germany 🇩🇪", "Greece 🇬🇷", "Hungary 🇭🇺", "Ireland 🇮🇪", 
    "Italy 🇮🇹", "Latvia 🇱🇻", "Lithuania 🇱🇹", "Luxembourg 🇱🇺", "Malta 🇲🇹", "Netherlands 🇳🇱", 
    "Poland 🇵🇱", "Portugal 🇵🇹", "Romania 🇷🇴", "Slovakia 🇸🇰", "Slovenia 🇸🇮", "Spain 🇪🇸", 
    "Sweden 🇸🇪", "Iceland 🇮🇸", "Liechtenstein 🇱🇮", "Norway 🇳🇴", "Switzerland 🇨🇭"
].index(country) + 1
try:
    data = {"country_id": country_id }
    response = requests.put('http://api:4000/u/UserCountry', json=data, timeout=300)
except Exception as e:
    st.error(f"An error occurred: {e}")

bio = st.text_area("Bio", 
                   help="Enter a quick bio here. Mention some environmental interests if any.",
                   height=100, max_chars=200)

consent = st.toggle("NGO Recommendations", value=1,
                    help="By selecting this option, you consent to your name and description being shared with organizations that also use CarbonConnect. ")

user_data = {
        'consent': consent, 
        'bio': bio
    }

if st.button("Submit"):
    response = requests.put('http://api:4000/u/UserUpdateInfo', json=user_data, timeout=300)

def fetch_tag_descriptions():
    try:
        response = requests.get('http://api:4000/u/tags')  
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

selected = pills('Current tags', tags, [emoji_map[tag] for tag in tags])

col1, col2 = st.columns(2)

with col1:
    def add_tags():
        st.write('### Add Tags')

        options = ["Transport", "Flights", "Energy", "Heat"]

        selected_tags = st.selectbox("Select your associated tags", options)

        if st.button("Add Tags"):
            add_tags_api_url = "http://api:4000/u/TagAdd"
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

with col2:
    def delete_tags():
        st.write('### Delete Tags')

        options = ["Transport", "Flights", "Energy", "Heat"]

        selected_tag = st.selectbox("Select tags to delete", options)  

        if st.button("Delete Tags"):
            delete_tags_api_url = "http://api:4000/u/TagDelete"
            tag_data = {"tag": selected_tag}  

            try:
                response = requests.delete(delete_tags_api_url, json=tag_data)
                if response.status_code == 200:
                    st.success("Tags successfully deleted!")
                else:
                    st.error(f"Failed to delete tags. Status code: {response.status_code}")
            except Exception as e:
                st.error(f"An error occurred while deleting tags: {e}")

    delete_tags()