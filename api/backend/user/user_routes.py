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
@user.route('/UserAddCar', methods=['PUT'])
def add_car():
    current_app.logger.info('user_routes.py: PUT /UserAddCar')
    
    received_data = request.json
    current_app.logger.info(received_data)

    fuel_type = received_data['fuel_type']
    fuel_used = received_data['fuel_used']
    
    query = "UPDATE Cars SET emission_tags = 'car', fuel_type = %s, fuel_used = %s WHERE user_id = 1"

    data = (fuel_type, fuel_used)
    cursor = db.get_db().cursor()
    cursor.execute(query, data)
    db.get_db().commit()
    return "success"
    


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

# Get all the residential history for this user
@user.route('/UserAddRes', methods=['PUT'])
def add_residential():
    current_app.logger.info('user_routes.py: PUT /UserAddRes')
    
    received_data = request.json
    current_app.logger.info(received_data)

    elec_usage = received_data['elec_usage']
    heating = received_data['heating']
    water_heating = received_data['water_heating']
    cooking_gas = received_data['cooking_gas']
    
    query = "UPDATE ResData SET emission_tags = 'residential', elec_usage = %s, heating = %s, water_heating = %s, cooking_gas = %s WHERE user_id = 1"

    data = (elec_usage, heating, water_heating, cooking_gas)
    cursor = db.get_db().cursor()
    cursor.execute(query, data)
    db.get_db().commit()
    return "success"
    

# # Get all the residential history for this user
# @user.route('/UserCountry', methods=['PUT'])
# def add_country():
#     current_app.logger.info('user_routes.py: PUT /UserCountry')
    
#     recieved_data = request.json
#     current_app.logger.info(recieved_data)

#     name = recieved_data['name']
#     emissions = recieved_data['website']

#     query = 'UPDATE NGO SET website = %s, name = %s, contact = %s WHERE id = 1'

#     data = (name, website, email)
#     cursor = db.get_db().cursor()
#     cursor.execute(query, data)
#     db.get_db().commit()


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