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
    
    household_members = st.number_input("How many people live in your household?", 1, None, 2)
    
    electricity_usage = 0.0000036 * 12 * st.number_input("How much electricity does your household use per month (kWh)?", 0.0, None, 6320.0)
    st.write("I use approximately ", electricity_usage / household_members , "terajoules per year.")

    heating = 0.0000036 * 12 * st.number_input("How much heating does your household use per month (kWh)?", 0.0, None, 3000.0)
    st.write("I use approximately ", heating / household_members, "terajoules per year.")

    water_heating = 0.0000036 * 12 * st.number_input("How much water heating does your household use per month (kWh)?", 0.0, None, 2000.0)
    st.write("I use approximately ", water_heating / household_members, "terajoules per year.")

    cooking_gas = 0.0000036 * 12 * st.number_input("Per month, how much energy is used cooking? (kWh)?", 0.0, None, 2000.0)
    st.write("I use approximately ", cooking_gas / household_members, "terajoules per year.")
    
    st.write("Total Residential Usage (TJ): ", (electricity_usage + heating + water_heating + cooking_gas) / household_members)
    
    if st.button("Submit Residential Data"):
        if household_members and electricity_usage and heating and water_heating and cooking_gas:
            api_url = "http://api:4000/u/UserAddRes"
            data = {
                "elec_usage": electricity_usage,
                "heating": heating,
                "water_heating": water_heating,
                "cooking_gas": cooking_gas}
            
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
    
    # numCars = st.number_input("How many cars do you own?", 0)
    # if (numCars > 0): 
    fuel_type = st.select_slider(
         "Fuel Type",
        options=["Gasoline/Hybrid", "Diesel", "Electric"])   
    
    if (fuel_type == "Gasoline/Hybrid"):
        fuel_capacity = st.number_input("How many liters of gasoline does your vehicle hold?", 0.0, None, 50.0)
        fuel_used_monthly = st.slider("How many times a month do you fill up your tank?", 0, 10, 5)
        fuel_used = st.number_input("Total fuel used per year (liters): ", 0.0, None, fuel_capacity * fuel_used_monthly * 12) * 1.11302E-6
    elif (fuel_type == "Diesel"):
        fuel_capacity = st.number_input("How many liters of diesel does your vehicle hold?", 0.0, None, 50.0)
        fuel_used_monthly = st.slider("How many times a month do you fill up your tank?", 0, 10, 5)
        fuel_used = st.number_input("Total fuel used per year (liters): ", 0.0, None, fuel_capacity * fuel_used_monthly * 12) * 1.1571E-6

    elif (fuel_type == "Electric"): 
        st.write("Please include charging data in residential data.")
        
    if st.button("Submit Car Data"):
        if fuel_type and fuel_used:
            api_url = "http://api:4000/u/UserAddCar"
            data = {
                "fuel_type": fuel_type,
                "fuel_used": fuel_used }
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
   
# # View Car Data   
# data = {} 
# try:
#   data = requests.get('http://api:4000/u/UserCars').json()
# except:
#   st.write("**Important**: Could not connect to sample api, so using dummy data.")
#   data = {"a":{"b": "123", "c": "hello"}, "z": {"b": "456", "c": "goodbye"}}

# st.dataframe(data)


if st.button("View Prediction"): 
    api_url = "http://api:4000/u/UserPrediction/"
    try: 
        response = requests.get(api_url)
        responseJSON = response.json()
        finalCarbon = responseJSON['result']
        st.write("Estimated Carbon Footprint (ktons of CO2 equivalent): ", finalCarbon)
        
        # HEY PROFS: THIS IS THE ML PREDICTION
        if response.status_code == 201 or response.status_code == 200:
            st.success("Successfully Predicted!")

            
        else:
            try:
                error_message = response.json().get('error', 'No error message provided')
            except json.JSONDecodeError:
                error_message = response.text  # Raw response if not JSON
            
            st.error(f"Failed to insert data. Status code: {response.status_code}, Error: {error_message}")
    except Exception as e:
        st.error(f"An error occurred: {e}")
        
        
        
