import streamlit as st
from modules.nav import SideBarLinks

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

st.write("# NGO tools") 

# make a page so that NGOs can edit their tags 

st.button("Edit NGO Information")
if st.button("Edit NGO Information"):
    @ngo.route('/editinfo', methods=['PUT'])
    def update_ngo():
        current_app.logger.info('PUT /ngo route')
         NGO_name = NGOInfo['name']
         # current_app.logger.info(cust_info)
         Website_link = NGOInfo['website']
        Contact_email = NGOInfo['email']
        selected_tags = NGOInfo['tags']
        query = 'UPDATE NGOINFO SET first_name = %s, last_name = %s, company = %s where id = %s'
        data = (name, website, email, tags)
        cursor = db.get_db().cursor()
        r = cursor.execute(query, data)
        db.get_db().commit()
        return 'ngo information updated!'
