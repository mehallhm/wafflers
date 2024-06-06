from flask import Blueprint, request, jsonify, make_response, current_app
import json
from backend.db_connection import db
from backend.ml_models.model_alpha import predict, train

user = Blueprint('user', __name__)

@user.route('/UserPrediction/', methods=['GET'])
def predict_value():
    cursor = db.get_db().cursor()
    
    select_heating_query = '''
        SELECT heating FROM ResData;
    '''
    cursor.execute(select_heating_query)
    heating = cursor.fetchone()[0]
    current_app.logger.info("THIS IS HEATING", heating)
    
    # select_water_query = '''
    #     SELECT water_heating FROM ResData WHERE user_id = 1;
    # '''
    # cursor.execute(select_water_query)
    # water_heating = cursor.fetchone()[0]
    # current_app.logger.info(select_water_query)
    
    # select_cooking_query = '''
    #     SELECT cooking_gas FROM ResData WHERE user_id = 1;
    # '''
    # cursor.execute(select_cooking_query)
    # cooking_gas = cursor.fetchone()[0]
    # current_app.logger.info(select_cooking_query)
    
    select_car_query = '''
        SELECT fuel_used FROM Cars WHERE user_id = 1;
    '''
    cursor.execute(select_car_query)
    fuel_used = cursor.fetchone()[0]
    current_app.logger.info(select_car_query)
    
    select_beta_query = '''
        SELECT user_values FROM Beta_User ORDER BY id DESC LIMIT 1;
        '''
    
    cursor.execute(select_beta_query)
    betaValue = cursor.fetchone()[0].split(', ')
    current_app.logger.info(select_beta_query)
    
    if betaValue is None:
        current_app.logger.info(f'Beta Value not Found: {betaValue}')
        return jsonify({"error": "BV not found"}), 404
    
    feats = [heating, fuel_used]
    returnVal = predict(feats, betaValue)
    return_dict = {'result': returnVal}

    the_response = make_response(jsonify(return_dict))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    
    betavals = train()
    current_app.logger.info("betavals: ", betavals)
    return the_response



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