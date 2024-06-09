import streamlit as st
from modules.nav import side_bar_links
import requests


# Show appropriate sidebar links for the role of the currently logged in user
side_bar_links()

# header telling the user what to do
st.header("User Survey")
st.write(
    "Let's take a look at your Carbon Footprint!",
    "Please complete the survey to the best of your ability.",
)

# expandable section that is expanded by default
st.divider()
st.write("### Energy Questions")
# user input section
household_members = st.number_input(
    "How many people live in your household?", 1, None, 2
)

electricity_usage = (
    0.0000036
    * 12
    * st.number_input(
        "How much electricity does your household use per month (kWh)?",
        0.0,
        None,
        6320.0,
    )
)

heating = (
    0.0000036
    * 12
    * st.number_input(
        "How much heating does your household use per month (kWh)?",
        0.0,
        None,
        3000.0,
    )
)

water_heating = (
    0.0000036
    * 12
    * st.number_input(
        "How much water heating does your household use per month (kWh)?",
        0.0,
        None,
        2000.0,
    )
)

cooking_gas = (
    0.0000036
    * 12
    * st.number_input(
        "Per month, how much energy is used cooking? (kWh)?", 0.0, None, 2000.0
    )
)

kWh_total = (electricity_usage + heating + water_heating + cooking_gas) / (
    household_members * 0.0000036 * 12
)
st.write("Your Total Residential Usage (kWh): ", round(kWh_total, 2))
st.write(
    "That's equivalent to running a 60w lightbulb for ",
    round((kWh_total * 1000) / 60),
    " hours!",
)

st.divider()
st.write("### Transportation Questions")

fuel_type = st.select_slider(
    "Fuel Type", options=["Gasoline/Hybrid", "Diesel", "Electric"]
)

if fuel_type == "Gasoline/Hybrid":
    fuel_capacity = st.number_input(
        "How many liters of gasoline does your vehicle hold?", 0.0, None, 50.0
    )
    fuel_used_monthly = st.slider(
        "How many times a month do you fill up your tank?", 0, 10, 5
    )
    fuel_used = fuel_capacity * fuel_used_monthly * 12 * 1.11302e-6
    st.write("Approx. fuel used per year (liters): ", fuel_used / 1.11302e-6)
    st.write(
        "That's equivalent to ",
        round((fuel_used / 1.11302e-6) / 302, 2),
        "bathtubs!",
    )

elif fuel_type == "Diesel":
    fuel_capacity = st.number_input(
        "How many liters of diesel does your vehicle hold?", 0.0, None, 50.0
    )
    fuel_used_monthly = st.slider(
        "How many times a month do you fill up your tank?", 0, 10, 5
    )
    fuel_used = fuel_capacity * fuel_used_monthly * 12 * 1.1571e-6
    st.write("Approx. fuel used per year (liters): ", fuel_used / 1.1571e-6)
    st.write(
        "That's equivalent to ",
        round((fuel_used / 1.1571e-6) / 302, 2),
        "bathtubs!",
    )

elif fuel_type == "Electric":
    st.write("Please include charging data in residential data.")

st.divider()

if st.button("View Prediction"):
    country_data = requests.get(
        "http://api:4000/u/UserCountryCarbon", timeout=10
    ).json()
    country_name = country_data[0]["name"]
    country_response = country_data[0]["emissions"]

    if (
        household_members
        and electricity_usage
        and heating
        and water_heating
        and cooking_gas
    ):
        API_URL = "http://api:4000/u/UserAddRes"
        data = {
            "elec_usage": electricity_usage,
            "heating": heating,
            "water_heating": water_heating,
            "cooking_gas": cooking_gas,
        }
        res_response = requests.post(API_URL, json=data, timeout=300)

    else:
        st.error("Please fill in all the fields before submitting.")

    API_URL = "http://api:4000/u/UserAddCar"
    data = {"fuel_type": fuel_type, "fuel_used": fuel_used}
    car_response = requests.post(API_URL, json=data, timeout=300)

    PRED_URL = "http://api:4000/u/UserPrediction/"
    pred_response = requests.get(PRED_URL, timeout=10)
    responseJSON = pred_response.json()
    finalCarbon = responseJSON["result"]

    with st.container(border=True):
        st.write(
            "### Estimated Carbon Footprint \n #####",
            round(finalCarbon * 1000000, 2),
            " kgs of CO2 equivalent",
        )
        st.write(
            "##### Your Carbon Footprint is ",
            round(finalCarbon / country_response, 2),
            " times the average person in ",
            country_name,
        )

        if (
            (car_response.status_code == 201 or car_response.status_code == 200)
            and (res_response.status_code == 201 or res_response.status_code == 200)
            and (pred_response.status_code == 201 or pred_response.status_code == 200)
        ):
            st.success("Successfully Predicted!")
