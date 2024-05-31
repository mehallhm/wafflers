import streamlit as st
from modules.nav import SideBarLinks

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

st.write("# About this app")


st.markdown (
    """
    This app is being built as an exemplar for Northeastern University's 
    Summer 2024 Dialogue of Civilization Program titled *Data and 
    Software in International Government and Politics*.  The program is bein
    led by Dr. Mark Fontenot and Dr. Eric Gerber from the Khoury College of
    Computer Sciences.  

    The goal of this project is to allow different user personas to calculate
    and see their emission data. It provides different emission related tools 
    to promote a greener world. 

    Stay tuned for more information and features to come!
    """
        )
