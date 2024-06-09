# this page defines routes needed for the enterprise entity 
from flask import Blueprint, request, jsonify, make_response, current_app
import json
from backend.db_connection import db


enterprises = Blueprint('enterprises', __name__)

#Retrieves all enterprise tags from the database
@enterprises.route('/tags', methods=['GET'])
def get_tags():
    cursor = db.get_db().cursor()

    cursor.execute('''
    SELECT description 
    FROM EmissionTags 
    WHERE EmissionTags.id IN (
        SELECT tag_id 
        FROM EntTags 
        WHERE EntTags.enterprise_survey_id = 1
    );
''')
    
   
    column_headers = [x[0] for x in cursor.description]


    json_data = []

    theData = cursor.fetchall()

    for row in theData:
        json_data.append(dict(zip(column_headers, row)))

    return jsonify(json_data)


#Retrieves all enterprise tags from the database
@enterprises.route('/NGOMatch', methods=['GET'])
def get_matches():
   
    cursor = db.get_db().cursor()

    cursor.execute('''
    SELECT NGO.name, EmissionTags.description
    FROM NGO
    JOIN NGOTags ON NGO.id = NGOTags.ngo_id
    JOIN EmissionTags ON NGOTags.tag_id = EmissionTags.id
    WHERE EmissionTags.id IN (
        SELECT tag_id
        FROM EntTags
        WHERE EntTags.enterprise_survey_id = 1
    );
''')
    

    column_headers = [x[0] for x in cursor.description]

    json_data = []


    theData = cursor.fetchall()

   
    for row in theData:
        json_data.append(dict(zip(column_headers, row)))

    return jsonify(json_data)


# get my emissions, my country's, and avg other companies in same country emissions
@enterprises.route('/EntCompare', methods=['GET'])
def get_comparison():

    cursor = db.get_db().cursor()

    cursor.execute('''
        SELECT AVG(Enterprises.emission_result) AS 'AVG Emission (by Country in kilotonnes)',
               Country.name                     AS 'Country',
               (SELECT e2.emission_result
                FROM Enterprises e2
                WHERE e2.id = 1
                ORDER BY e2.survey_id DESC
                LIMIT 1)                AS 'Your Emissions (in kilotonnes)'
        FROM Enterprises
                 JOIN Country ON Enterprises.country_id = Country.id
        WHERE Country.name =
              (SELECT Country.name
               FROM Enterprises
                        JOIN Country ON Enterprises.country_id = Country.id
               WHERE Enterprises.id = 1
               LIMIT 1)
        GROUP BY Country.name;
    ''')
    
    
    column_headers = [x[0] for x in cursor.description]

    json_data = []

    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(column_headers, row)))

    return jsonify(json_data)

# adds new survey entry to make new emission_result for enterprise
@enterprises.route('/EntResult', methods=['POST'])
def add_entry():
    
    received_data = request.json
    current_app.logger.info(received_data)

    emission = received_data['emission']
    
    query = "INSERT INTO Enterprises (id, name, type, emission_result, country_id) VALUES (1, 'EcoForward Enterprises', 'Lighting', %s, 20)"

    data = (emission)
    cursor = db.get_db().cursor()
    cursor.execute(query, emission)
    db.get_db().commit()
    return "success"

#allows enterprises to delete tags that they no longer want to be associated with 
@enterprises.route("/TagDelete", methods=["DELETE"])
def delete_tags():

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
    DELETE FROM EntTags WHERE enterprise_survey_id = 1 AND tag_id = %s;
    """
    cursor.execute(delete_query, (tag_id,))
    db.get_db().commit()

    current_app.logger.info(
        f"Successfully deleted tag: {tag_description} for Enterprise"
    )
    return "Success"

#allows enterprises to add tags that they no longer want to be associated with 
@enterprises.route("/TagAdd", methods=["POST"])
def add_tags():

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

    insert_query = "INSERT INTO EntTags (enterprise_survey_id, tag_id) VALUES (1, %s)"
    cursor.execute(insert_query, (new_tag_id,))
    db.get_db().commit()

    return jsonify({"message": "Success"}), 200

#retrieves enterprise history and displays it to the user on  data entry at a time 
@enterprises.route('/EnterpriseHistory', methods=['GET'])
def get_history():
    cursor = db.get_db().cursor()

    cursor.execute('''
    SELECT emission_result AS emission_history
    FROM Enterprises
    WHERE Enterprises.id = 1
    ''')

    column_headers = [x[0] for x in cursor.description]


    json_data = []

    theData = cursor.fetchall()
    current_app.logger.info(theData)


    for row in theData:
        json_data.append(dict(zip(column_headers, row)))


    return jsonify(json_data)
