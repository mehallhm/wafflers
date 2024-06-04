from flask import Blueprint, request, jsonify, make_response, current_app
import json
from backend.db_connection import db

user = Blueprint('user', __name__)

# Get all the cars history for this user
@user.route('/UserCars', methods=['GET'])
def get_cars():
    cursor = db.get_db().cursor()

    cursor.execute('SELECT * FROM Cars WHERE Cars.user_id = 1')

    column_headers = [x[0] for x in cursor.description]

    json_data = []

    theData = cursor.fetchall()

    for row in theData:
        json_data.append(dict(zip(column_headers, row)))

    return jsonify(json_data)

# Get all the residential history for this user
@user.route('/UserResidential', methods=['GET'])
def get_residential():
    cursor = db.get_db().cursor()

    cursor.execute('SELECT * FROM ResData WHERE ResData.user_id = 1')

    column_headers = [x[0] for x in cursor.description]

    json_data = []

    theData = cursor.fetchall()

    for row in theData:
        json_data.append(dict(zip(column_headers, row)))

    return jsonify(json_data)

# Get all the flight history for this user
@user.route('/UserFlights', methods=['GET'])
def get_flights():
    cursor = db.get_db().cursor()

    cursor.execute('SELECT * FROM Flight WHERE Flight.user_id = 1')

    column_headers = [x[0] for x in cursor.description]

    json_data = []

    theData = cursor.fetchall()

    for row in theData:
        json_data.append(dict(zip(column_headers, row)))

    return jsonify(json_data)

# Get all the public transport history for this user
@user.route('/UserTransport', methods=['GET'])
def get_transport():
    cursor = db.get_db().cursor()

    cursor.execute('SELECT * FROM PublicTransport WHERE PublicTransport.user_id = 1')

    column_headers = [x[0] for x in cursor.description]

    json_data = []

    theData = cursor.fetchall()

    for row in theData:
        json_data.append(dict(zip(column_headers, row)))

    return jsonify(json_data)