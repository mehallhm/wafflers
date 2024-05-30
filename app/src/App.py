import streamlit as st

def App():
    
    st.title('Welcome to Carbon Connect!')
    st.header('Choose your persona below')

    st.write('')

    # icons designed by freepik

    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("General User"):
          st.switch_page("pages/01_userhome.py")
        st.image('https://cdn-icons-png.freepik.com/256/552/552848.png?ga=GA1.1.1507691374.1717099387', width = 100)

    with col2:
        if st.button("Enterprise"):
          st.switch_page("pages/02_enterprisehome.py")
        st.image('https://cdn-icons-png.freepik.com/256/834/834504.png?ga=GA1.1.1507691374.1717099387', width = 100)

    with col3:
        if st.button("NGO"):
          st.switch_page("pages/03_NGOhome.py")
        st.image('https://cdn-icons-png.freepik.com/256/3101/3101045.png?ga=GA1.1.1507691374.1717099387', width = 100)


App()