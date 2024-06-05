import streamlit as st
from modules.nav import SideBarLinks


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
    electricityUsage = 0.0000036 * 12 * st.number_input("How much electricity do your household use per month (kWh)?", 0.0, None, 6320.0)
    st.write("I use approximately ", round(electricityUsage) , "terajoules per year.")

    electricityUsage = 0.0000036 * 12 * st.number_input("How much electricity do your household use per month (kWh)?", 0.0, None, 6320.0)
    st.write("I use approximately ", round(electricityUsage) , "terajoules per year.")


carNumber = st.slider("How many cars do you currently have?", 0, 130, 25)
st.write("I have ", carNumber , "cars")

