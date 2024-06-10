# this page defines routes needed for the user entity 
from flask import Blueprint, request, jsonify, make_response, current_app
import json
from backend.db_connection import db
from backend.ml_models.model_alpha import predict, train

user = Blueprint("user", __name__)


@user.route("/UserPrediction/", methods=["GET"])
def predict_value():
    '''Connection to ML: Predicts Carbon Footprint'''
    cursor = db.get_db().cursor()

    select_heating_query = """
        SELECT heating FROM ResData WHERE user_id = 1 ORDER BY id DESC LIMIT 1;
    """
    cursor.execute(select_heating_query)
    heating = cursor.fetchone()[0]
    current_app.logger.info("THIS IS HEATING", heating)

    select_car_query = """
        SELECT fuel_used FROM Cars WHERE user_id = 1 ORDER BY id DESC LIMIT 1;
    """
    cursor.execute(select_car_query)
    fuel_used = cursor.fetchone()[0]
    current_app.logger.info(select_car_query)

    select_beta_query = """
        SELECT user_values FROM Beta_User ORDER BY id DESC LIMIT 1;
        """

    cursor.execute(select_beta_query)
    beta_val = cursor.fetchone()[0].split(", ")
    current_app.logger.info(select_beta_query)

    if beta_val is None:
        current_app.logger.info(f"Beta Value not Found: {beta_val}")
        return jsonify({"error": "BV not found"}), 404

    feats = [heating, fuel_used]
    return_val = predict(feats, beta_val)
    return_dict = {"result": return_val}

    the_response = make_response(jsonify(return_dict))
    the_response.status_code = 200
    the_response.mimetype = "application/json"
    return the_response


# Get all the cars history for this user
@user.route("/CountryCarbon", methods=["GET"])
def get_country_carbon():
    """returns the carbon of the user's country"""
    cursor = db.get_db().cursor()
    cursor.execute(
        "SELECT Country.* FROM Country JOIN User ON User.country_id = Country.id WHERE User.id = 1"
    )
    column_headers = [x[0] for x in cursor.description]

    json_data = []
    returned_data = cursor.fetchall()
    for row in returned_data:
        json_data.append(dict(zip(column_headers, row)))
    return jsonify(json_data)


# Get all the residential history for this user
@user.route("/UserCountry", methods=["PUT"])
def add_country():
    '''Updates Country Data for this user'''
    current_app.logger.info("user_routes.py: PUT /UserCountry")

    recieved_data = request.json
    current_app.logger.info(recieved_data)

    country_id = recieved_data["country_id"]

    query = "UPDATE User SET country_id = %s WHERE id = 1"

    data = country_id
    cursor = db.get_db().cursor()
    cursor.execute(query, data)
    db.get_db().commit()
    return "success"


# Get all the cars history for this user
@user.route("/UserCars", methods=["GET"])
def get_cars():
    '''Returns car data for this user'''
    cursor = db.get_db().cursor()

    cursor.execute("SELECT * FROM Cars WHERE Cars.user_id = 1")

    column_headers = [x[0] for x in cursor.description]

    json_data = []

    returned_data = cursor.fetchall()

    for row in returned_data:
        json_data.append(dict(zip(column_headers, row)))

    return jsonify(json_data)


# Adds car survey data
@user.route("/UserAddCar", methods=["POST"])
def add_car():
    '''Adds car survey data to the database'''
    current_app.logger.info("user_routes.py: POST /UserAddCar")

    received_data = request.json
    current_app.logger.info(received_data)

    fuel_type = received_data["fuel_type"]
    fuel_used = received_data["fuel_used"]

    query = "INSERT INTO Cars (emission_tags, user_id, fuel_type, \
            fuel_used) VALUES ('car', 1, %s, %s)"

    data = (fuel_type, fuel_used)
    cursor = db.get_db().cursor()
    cursor.execute(query, data)
    db.get_db().commit()
    return "success"

# Adds car survey data
@user.route("/UserAddCarbon", methods=["PUT"])
def add_carbon():
    '''Adds predicted carbon data to the database'''
    current_app.logger.info("user_routes.py: PUT /UserAddCarbon") 

    received_data = request.json
    current_app.logger.info(received_data)
    
    emission_result = received_data["emission_result"]

    query = "UPDATE User SET emission_result = %s WHERE id = 1"

    data = (emission_result)
    cursor = db.get_db().cursor()
    cursor.execute(query, data)
    db.get_db().commit()
    return "success"

# Get all the residential history for this user
@user.route("/UserResidential", methods=["GET"])
def get_residential():
    '''Returns residential data for this user'''
    cursor = db.get_db().cursor()

    cursor.execute("SELECT * FROM ResData WHERE ResData.user_id = 1")

    column_headers = [x[0] for x in cursor.description]

    json_data = []

    returned_data = cursor.fetchall()

    for row in returned_data:
        json_data.append(dict(zip(column_headers, row)))

    return jsonify(json_data)


# adding survey residential data
@user.route("/UserAddRes", methods=["POST"])
def add_residential():
    '''Adds residential survey data to the database'''
    current_app.logger.info("user_routes.py: POST /UserAddRes")

    received_data = request.json
    current_app.logger.info(received_data)

    elec_usage = received_data["elec_usage"]
    heating = received_data["heating"]
    water_heating = received_data["water_heating"]
    cooking_gas = received_data["cooking_gas"]

    query = "INSERT INTO ResData (emission_tags, elec_usage, heating, water_heating, \
            cooking_gas, user_id) VALUES ('residential', %s, %s, %s, %s, 1)"

    data = (elec_usage, heating, water_heating, cooking_gas)
    cursor = db.get_db().cursor()
    cursor.execute(query, data)
    db.get_db().commit()
    return "success"


@user.route("/UserCarbon", methods=["GET"])
def get_carbon():
    """Get all the carbon history for this user"""
    cursor = db.get_db().cursor()
    cursor.execute("SELECT emission_result FROM User WHERE id = 1")

    column_headers = [x[0] for x in cursor.description]
    json_data = []
    returned_data = cursor.fetchall()

    for row in returned_data:
        json_data.append(dict(zip(column_headers, row)))
    current_app.logger.info("CARBONHISTORY: ", json_data)
    return jsonify(json_data)


# Get all the public transport history for this user
@user.route("/UserTransport", methods=["GET"])
def get_transport():
    '''Get all the public transport history for this user'''
    cursor = db.get_db().cursor()
    cursor.execute("SELECT * FROM PublicTransport WHERE PublicTransport.user_id = 1")

    column_headers = [x[0] for x in cursor.description]
    json_data = []
    returned_data = cursor.fetchall()

    for row in returned_data:
        json_data.append(dict(zip(column_headers, row)))
    return jsonify(json_data)


@user.route("/UserBio", methods=["GET"])
def get_bio ():
    '''Get the bio for this user'''
    cursor = db.get_db().cursor()

    cursor.execute("SELECT bio FROM User WHERE id = 1")
    bio = cursor.fetchone()[0]

    return jsonify({"bio": bio})

@user.route("/UserAll", methods=["GET"])
def get_all_user_data():
    '''Get all for this user'''
    cursor = db.get_db().cursor()

    cursor.execute("SELECT * FROM User WHERE id = 1 ORDER BY survey_id DESC LIMIT 1")
    user = cursor.fetchone()

    return jsonify({"user": user})

# Updates match consent and bio for user
@user.route("/UserUpdateInfo", methods=["PUT"])
def update_user():
    '''Update user info (consent and bio)'''
    current_app.logger.info("user.routes.py: PUT /UserUpdateInfo")

    received_data = request.json
    current_app.logger.info(received_data)

    user_bio = received_data["bio"]
    current_app.logger.info("BIO: ", user_bio)
    match_consent = received_data["consent"]

    query = "UPDATE User SET match_consent = %s, bio = %s WHERE id = 1"

    data = (match_consent, user_bio)
    cursor = db.get_db().cursor()
    cursor.execute(query, data)
    db.get_db().commit()
    return "Success"


# get this user's tags
@user.route("/tags", methods=["GET"])
def get_usertags():
    '''Get all the tags for this user'''
    cursor = db.get_db().cursor()
    cursor.execute(
        """
       SELECT description
       FROM EmissionTags
       WHERE EmissionTags.id IN (
           SELECT tag_id
           FROM UserTags
           WHERE UserTags.user_id = 1
           ORDER BY survey_id
           LIMIT 1;
       );
   """
    )

    column_headers = [x[0] for x in cursor.description]
    json_data = []
    the_data = cursor.fetchall()
    for row in the_data:
        json_data.append(dict(zip(column_headers, row)))

    return jsonify(json_data)


# deletes selected tag for this user
@user.route("/TagDelete", methods=["DELETE"])
def delete_tags():
    '''Deletes a tag from the user's tags'''
    current_app.logger.info("DELETE /user/TagDelete route")

    info = request.json
    tag_description = info.get("tag")

    cursor = db.get_db().cursor()
    select_query = """
        SELECT id FROM EmissionTags WHERE description = %s;
        """
    cursor.execute(select_query, (tag_description,))
    tag_row = cursor.fetchone()
    current_app.logger.info(select_query)

    if tag_row is None:
        current_app.logger.info(f"Tag not found: {tag_description}")
        return jsonify({"error": "Tag not found"}), 404

    tag_id = tag_row[0]

    delete_query = """
    DELETE FROM UserTags WHERE user_id = 1 AND tag_id = %s;
    """
    cursor.execute(delete_query, (tag_id,))
    db.get_db().commit()

    current_app.logger.info(
        f"Successfully deleted tag: {tag_description} for User ID: 1"
    )
    return "Success"


# adds selected tag for this user
@user.route("/TagAdd", methods=["POST"])
def add_tags():
    '''Adds a tag to the user's tags'''
    current_app.logger.info("POST /user/TagAdd route")

    info = request.json
    tag_description = info.get("tag")

    cursor = db.get_db().cursor()

    select_query = """
   SELECT
       ET.id AS tag_id
   FROM
       EmissionTags ET
   WHERE
       ET.description = %s
   """
    cursor.execute(select_query, (tag_description,))
    tag_row = cursor.fetchone()

    if tag_row is None:
        return jsonify({"error": "Tag not found"}), 404

    new_tag_id = tag_row[0]

    insert_query = "INSERT INTO UserTags (user_id, tag_id) VALUES (1, %s)"
    cursor.execute(insert_query, (new_tag_id,))
    db.get_db().commit()

    return jsonify({"message": "Success"}), 200
