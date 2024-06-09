# Home navigation page for 3 user personas
import streamlit as st
from modules.nav import side_bar_links

st.set_page_config(layout="wide")

st.session_state["authenticated"] = False
side_bar_links()

def App():
    """
    Initiates the Streamlit App
    """
    st.title("Welcome to Carbon Connect!")
    st.header("Act as...")

    st.write("")

    # icons designed by freepik

    col1, col2, col3, col4, col5, col6 = st.columns(6)
    with col1:
        if st.button("Natalie Allard"):
            st.session_state["authenticated"] = True
            st.session_state["role"] = "General User"
            st.session_state["first_name"] = "Natalie"
            st.switch_page("pages/01_userhome.py")
        inner_col1, inner_col2, inner_col3, inner_col4, inner_col5, inner_col6, \
        inner_col7, inner_col8, inner_col9, inner_col10, inner_col11, inner_col12 = st.columns(12)
        with inner_col2:
            st.image("assets/profile-user.png", width=85)
        

    with col3:
        if st.button("EcoForward Enterprises"):
            st.session_state["authenticated"] = True
            st.session_state["role"] = "Enterprise"
            st.session_state["first_name"] = "EcoForward"
            st.switch_page("pages/10_enterprisehome.py")
        inner_col1, inner_col2, inner_col3, inner_col4, inner_col5, inner_col6, \
        inner_col7, inner_col8, inner_col9, inner_col10, inner_col11, inner_col12 = st.columns(12)
        with inner_col2:
            st.image("assets/suitcase.png", width=85)

    with col5:
        if st.button("EcoUnity Europe"):
            st.session_state["authenticated"] = True
            st.session_state["role"] = "NGO"
            st.session_state["first_name"] = "EcoUnity"
            st.switch_page("pages/20_NGOhome.py")
        inner_col1, inner_col2, inner_col3, inner_col4, inner_col5, inner_col6, \
        inner_col7, inner_col8, inner_col9, inner_col10, inner_col11, inner_col12 = st.columns(12)
        with inner_col2:
            st.image("assets/NGOicon.png", width=85)


App()
