# NGO info page allowing editing of name, website, email, and bio, 
# Shows my NGO tags and features add/delete tag functionality
import streamlit as st
from modules.nav import side_bar_links
import requests
import validators
from streamlit_pills import pills
import json

# Show appropriate sidebar links for the role of the currently logged in user
side_bar_links()

st.write("# Account Info")
st.write("#### Edit Organization Information Below")

with st.container(border=True):
    ngo_name = st.text_input("Organization Name")
    def url_check(url, tld_list):
        if not url.startswith(("http://", "https://")):
            url = "http://" + url
        if validators.url(url):
            domain = url.split("/")[2]
            for tld in tld_list:
                if domain.endswith(tld):
                    return True
        return False

    website_link = st.text_input("Website Link:")
    if website_link:
        if url_check(
            website_link,
            [".com", ".gov", ".net", ".org", ".tv", ".cz", ".jp", ".de", ".br", ".edu"],
        ):
            st.success("Valid URL!")
        else:
            st.error("Invalid URL or TLD")

    contact_email = st.text_input("Head Contact Email:")
    if contact_email:
        if validators.email(contact_email):
            st.success("Valid Email Address!")
        else:
            st.error("Invalid Email Address. Please Enter A Valid Email.")

    current_bio = requests.get("http://api:4000/n/Bio", timeout=200).json()["bio"]

    bio = st.text_area(
        "Bio",
        help="Enter a quick bio here. Mention some environmental interests if any",
        height=100,
        value=current_bio,
    )

    if st.button("Submit"):
        if (ngo_name
            and url_check(
                website_link,
                [".com", ".gov", ".net", ".org", ".tv", ".cz", ".jp", ".de", ".br", ".edu"],
            )
            and validators.email(contact_email)
        ):

            data = {"name": ngo_name, "website": website_link, "email": contact_email, "bio": bio}

            try:
                response = requests.put("http://api:4000/n/NGOUpdate", json=data, timeout=200)

                if response.status_code == 201 or response.status_code == 200:
                    st.success("Data Successfully Inserted!")
                else:
                    try:
                        error_message = response.json().get(
                            "error", "No Error Message Provided"
                        )
                    except json.JSONDecodeError:
                        error_message = response.text  # Raw response if not JSON

                    st.error(
                        f"Failed To Insert Data. Status Code: {response.status_code}, Error: {error_message}"
                    )
            except Exception as e:
                st.error(f"An Error Occurred: {e}")
        else:
            st.error(
                "Please Fill In All The Fields Before Submitting And Have Valid Emails/Urls"
            )

with st.container(border=True):
    st.write("### My Tags")

    try:
        response = requests.get("http://api:4000/n/tags")
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching data: {e}")


    emoji_map = {
        "Heat": "🔥",
        "Flights": "🛫",
        "Energy": "💡",
        "Transport": "🚗",
    }

    tags = [tag["description"] for tag in data]

    if data:
        tags = [tag["description"] for tag in data]
        selected = pills("Current tags", tags, [emoji_map[tag] for tag in tags], index=None)
    else:
        tags = []
        st.info("No tags available to display.")


    col1, col2 = st.columns(2)
    with col1:
        st.write("### Add New NGO Tags")
        options = ["Transport", "Flights", "Energy", "Heat"]
        options = [option for option in options if option not in tags]

        selected_tags = st.selectbox("Select Your Associated Tags", options)
        if st.button("Add Tags"):
            tag_data = {"tag": selected_tags}
            try:
                response = requests.post("http://api:4000/n/NGOAdd", json=tag_data, timeout=200)
                if response.status_code == 200:
                    st.success("Tags Successfully Added!")
                else:
                    st.error(f"Failed To Add Tags. Status Code: {response.status_code}")
            except Exception as e:
                st.error(f"An Error Occurred While Adding Tags: {e}")
    with col2:
        st.write("### Delete NGO Tags")
        options = ["Transport", "Flights", "Energy", "Heat"]
        options = [option for option in options if option in tags]
        selected_tag = st.selectbox("Select Tags To Delete", options)
        if st.button("Delete Tags"):
            tag_data = {"tag": selected_tag}
            try:
                response = requests.delete("http://api:4000/n/TagDelete", json=tag_data, timeout=200)
                if response.status_code == 200:
                    st.success("Tags Successfully Deleted!")
                else:
                    st.error(
                        f"Failed To Delete Tags. Status Code: {response.status_code}"
                    )
            except Exception as e:
                st.error(f"An Error Occurred While Deleting Tags: {e}")