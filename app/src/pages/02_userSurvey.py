import streamlit as st
from modules.nav import SideBarLinks
import requests
import json

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

st.header("User Survey")
st.write("##### Let's take a look at your Carbon Footprint!")
st.write("Please complete the survey to the best of your ability.")
country = st.selectbox(
    "Country :flag-eu:",
    ("Austria 🇦🇹", "Belgium 🇧🇪", "Bulgaria 🇧🇬", "Croatia 🇭🇷", "Cyprus 🇨🇾", "Czechia 🇨🇿", "Denmark 🇩🇰", "Estonia 🇪🇪", "Finland 🇫🇮", "France 🇫🇷", "Germany 🇩🇪", "Greece 🇬🇷", "Hungary 🇭🇺", "Ireland 🇮🇪", "Italy 🇮🇹", "Latvia 🇱🇻", "Lithuania 🇱🇹", "Luxembourg 🇱🇺", "Malta 🇲🇹", "Netherlands 🇳🇱", "Poland 🇵🇱", "Portugal 🇵🇹", "Romania 🇷🇴", "Slovakia 🇸🇰", "Slovenia 🇸🇮", "Spain 🇪🇸", "Sweden 🇸🇪", "Iceland 🇮🇸", "Liechtenstein 🇱🇮", "Norway 🇳🇴", "Switzerland 🇨🇭"))
st.write("You selected:", country)

with st.expander("Residential Data"):
    
    houseHoldMembers = st.number_input("How many people live in your household?", 1, None, 2)
    
    electricityUsage = 0.0000036 * 12 * st.number_input("How much electricity does your household use per month (kWh)?", 0.0, None, 6320.0)
    st.write("I use approximately ", electricityUsage / houseHoldMembers , "terajoules per year.")

    heating = 0.0000036 * 12 * st.number_input("How much heating does your household use per month (kWh)?", 0.0, None, 3000.0)
    st.write("I use approximately ", heating / houseHoldMembers, "terajoules per year.")

    waterHeating = 0.0000036 * 12 * st.number_input("How much water heating does your household use per month (kWh)?", 0.0, None, 2000.0)
    st.write("I use approximately ", waterHeating / houseHoldMembers, "terajoules per year.")

    cookingGas = 0.0000036 * 12 * st.number_input("Per month, how much energy is used cooking? (kWh)?", 0.0, None, 2000.0)
    st.write("I use approximately ", cookingGas / houseHoldMembers, "terajoules per year.")
    
    st.write("Total Residential Usage (TJ): ", (electricityUsage + heating + waterHeating + cookingGas) / houseHoldMembers)
    
    if st.button("Submit"):
        if houseHoldMembers and electricityUsage and heating and waterHeating and cookingGas:
            api_url = "http://api:4000/u/UserAddRes"
            data = {
                "elec_usage": electricityUsage,
                "heating": heating,
                "water_heating": waterHeating,
                "cooking_gas": cookingGas}
            
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
            st.error("Please fill in all the fields before submitting.")
   
# data = {} 
# try:
#   data = requests.get('http://api:4000/u/UserResidential').json()
# except:
#   st.write("**Important**: Could not connect to sample api, so using dummy data.")
#   data = {"a":{"b": "123", "c": "hello"}, "z": {"b": "456", "c": "goodbye"}}

# st.dataframe(data)

with st.expander("Car Data"):
    
    numCars = st.number_input("How many cars do you own?", 0)
    
    if (numCars > 0): 
        fuelType = st.select_slider(
        "",
        options=["red", "orange", "yellow", "green", "blue", "indigo", "violet"])
    st.write("My favorite color is", color)
    
    electricityUsage = 0.0000036 * 12 * st.number_input("How much electricity does your household use per month (kWh)?", 0.0, None, 6320.0)
    st.write("I use approximately ", electricityUsage / houseHoldMembers , "terajoules per year.")

    heating = 0.0000036 * 12 * st.number_input("How much heating does your household use per month (kWh)?", 0.0, None, 3000.0)
    st.write("I use approximately ", heating / houseHoldMembers, "terajoules per year.")

    waterHeating = 0.0000036 * 12 * st.number_input("How much water heating does your household use per month (kWh)?", 0.0, None, 2000.0)
    st.write("I use approximately ", waterHeating / houseHoldMembers, "terajoules per year.")

    cookingGas = 0.0000036 * 12 * st.number_input("Per month, how much energy is used cooking? (kWh)?", 0.0, None, 2000.0)
    st.write("I use approximately ", cookingGas / houseHoldMembers, "terajoules per year.")
    
    st.write("Total Residential Usage (TJ): ", (electricityUsage + heating + waterHeating + cookingGas) / houseHoldMembers)
    
    if st.button("Submit"):
        if houseHoldMembers and electricityUsage and heating and waterHeating and cookingGas:
            api_url = "http://api:4000/u/UserAddRes"
            data = {
                "elec_usage": electricityUsage,
                "heating": heating,
                "water_heating": waterHeating,
                "cooking_gas": cookingGas}
            
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
            st.error("Please fill in all the fields before submitting.")
   
    
    
carNumber = st.slider("How many cars do you currently have?", 0, 130, 25)
st.write("I have ", carNumber , "cars")

