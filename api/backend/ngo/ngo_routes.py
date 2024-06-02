from flask import Blueprint, request, jsonify, make_response, current_app
import json
from backend.db_connection import db

ngo = Blueprint('ngo', __name__)

@ngo.route('/NGOadd', methods=['POST'])
def add_new_NGO():
    
    recieved_data = request.json

    name = recieved_data['name']
    website = recieved_data['website']
    email = recieved_data['email']

    query = 'INSERT INTO NGO (website, name, contact) VALUES (%s, %s, %s)'

    data = (name, website, email)
    cursor = db.get_db().cursor()
    cursor.execute(query, data)
    db.get_db().commit()

    new_id = cursor.lastrowid
    return jsonify({'message': 'Success!', 'id': new_id}), 201
