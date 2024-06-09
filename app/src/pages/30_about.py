# About page detailing extra info on Carbon Connect
import streamlit as st
from modules.nav import side_bar_links

# Show appropriate sidebar links for the role of the currently logged in user
side_bar_links()

st.write("# About this app")


st.markdown(
    """
    This app is being built as an exemplar for Northeastern University's 
    Summer 2024 Dialogue of Civilization Program titled *Data and 
    Software in International Government and Politics*. 

    The goal of this project is to allow different user personas to calculate
    and see their emission data. It provides different emission related tools 
    to promote a greener world. 

    Check out our blog for feature changes and fun!

    - The Wafflers: Aahil, Anjola, Justin, Michael
    """
)
