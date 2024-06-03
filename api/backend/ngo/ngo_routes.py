from flask import Blueprint, request, jsonify, make_response, current_app
import json
from backend.db_connection import db

ngo = Blueprint('ngo', __name__)

@ngo.route('/NGOadd', methods=['POST'])
def add_new_NGO():
    current_app.logger.info('ngo_routes.py: POST /NGOadd')
    
    recieved_data = request.json
    current_app.logger.info(recieved_data)

    name = recieved_data['name']
    website = recieved_data['website']
    email = recieved_data['email']

    query = 'INSERT INTO NGO (website, name, contact) VALUES (%s, %s, %s)'

    data = (name, website, email)
    current_app.logger.info(query)
    current_app.logger.info(data)
    cursor = db.get_db().cursor()
    cursor.execute(query, data)
    db.get_db().commit()

    new_id = cursor.lastrowid
    
    selected_tags = recieved_data.get('tags', []) 
    if selected_tags:
        insert_query = 'INSERT INTO NGOTags (ngo_id, tag_id) VALUES (%s, %s)'
        # for each tag gets the tag_id from the emission tags table, :)
        # also inserts into NGO tags
        for tag_name in selected_tags:
            tag_query = 'SELECT id FROM EmissionTags WHERE description = %s'
            cursor.execute(tag_query, (tag_name,))
            tag_row = cursor.fetchone()
            tag_id = tag_row[0]
            cursor.execute(insert_query, (new_id, tag_id))
            db.get_db().commit()

    return 'Success'





@ngo.route('/ngotags', methods=['GET'])
def get_ngotags():
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # use cursor to query the database for a list of products
    cursor.execute('SELECT * FROM NGOTags')

    # grab the column headers from the returned data
    column_headers = [x[0] for x in cursor.description]

    # create an empty dictionary object to use in 
    # putting column headers together with data
    json_data = []

    # fetch all the data from the cursor
    theData = cursor.fetchall()

    # for each of the rows, zip the data elements together with
    # the column headers. 
    for row in theData:
        json_data.append(dict(zip(column_headers, row)))

    return jsonify(json_data)

@ngo.route('/tags', methods=['GET'])
def get_ngodata():
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # use cursor to query the database for a list of products
    cursor.execute('SELECT * FROM EmissionTags')

    # grab the column headers from the returned data
    column_headers = [x[0] for x in cursor.description]

    # create an empty dictionary object to use in 
    # putting column headers together with data
    json_data = []

    # fetch all the data from the cursor
    theData = cursor.fetchall()

    # for each of the rows, zip the data elements together with
    # the column headers. 
    for row in theData:
        json_data.append(dict(zip(column_headers, row)))

    return jsonify(json_data)