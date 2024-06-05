import streamlit as st
from modules.nav import SideBarLinks
import streamlit_survey as ss
survey = ss.StreamlitSurvey()

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

st.write("# User survey")

survey.text_input("Text input:", id="Q1")
st.write("## What country in Europe are you from?")
survey.selectbox("Selection box:", options=["Albania", "Andorra", "Armenia", "Austria", "Azerbaijan"])


carNumber = st.slider("How many cars do you currently have?", 0, 130, 25)
st.write("I have ", carNumber , "cars")