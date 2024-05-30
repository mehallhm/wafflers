import streamlit as st

def App():
    st.title('Welcome to Carbon Connect!')
    st.header('Choose your persona below')

    if st.button("General User"):
      st.switch_page("pages/01_userhome.py")
    if st.button("Enterprise"):
      st.switch_page("pages/02_enterprisehome.py")
    if st.button("NGO"):
      st.switch_page("pages/03_NGOhome.py")
      

App()