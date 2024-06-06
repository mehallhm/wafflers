########################################################
# Sample customers blueprint of endpoints
# Remove this file if you are not using it in your project
########################################################

from flask import Blueprint, request, jsonify, make_response, current_app
import json
from backend.db_connection import db


enterprises = Blueprint('enterprises', __name__)

# get all of the enterprise tags from database
@enterprises.route('/tags', methods=['GET'])
def get_tags():
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    cursor.execute('''
    SELECT description 
    FROM EmissionTags 
    WHERE EmissionTags.id IN (
        SELECT tag_id 
        FROM EntTags 
        WHERE EntTags.enterprise_id = 1
    );
''')
    
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


# get all of the matching NGO's based on tags
@enterprises.route('/NGOMatch', methods=['GET'])
def get_matches():
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    cursor.execute('''
    SELECT NGO.name, EmissionTags.description
    FROM NGO
    JOIN NGOTags ON NGO.id = NGOTags.ngo_id
    JOIN EmissionTags ON NGOTags.tag_id = EmissionTags.id
    WHERE EmissionTags.id IN (
        SELECT tag_id
        FROM EntTags
        WHERE EntTags.enterprise_id = 1
    );
''')
    
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


# get my emissions, my country's, and avg other companies in same country emissions
@enterprises.route('/EntCompare', methods=['GET'])
def get_comparison():
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    cursor.execute('''
        SELECT AVG(Enterprises.emission_result) AS 'Average Emission (by Country)',
               Country.name                     AS 'Country',
               (SELECT e2.emission_result
                FROM Enterprises e2
                WHERE e2.id = 1)                AS 'Your Emissions'
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


# Get all the supply chain history for this enterprise
@enterprises.route('/EntSupplyChain', methods=['GET'])
def get_supplychain():
    cursor = db.get_db().cursor()

    cursor.execute('SELECT * FROM SupplyChain WHERE SupplyChain.enterprise_id = 1')

    column_headers = [x[0] for x in cursor.description]

    json_data = []

    theData = cursor.fetchall()

    for row in theData:
        json_data.append(dict(zip(column_headers, row)))

    return jsonify(json_data)

# Get all the operating cost history for this enterprise
@enterprises.route('/EntCosts', methods=['GET'])
def get_costs():
    cursor = db.get_db().cursor()

    cursor.execute('SELECT * FROM operatingEmission WHERE operatingEmission.enterprise_id = 1')

    column_headers = [x[0] for x in cursor.description]

    json_data = []

    theData = cursor.fetchall()

    for row in theData:
        json_data.append(dict(zip(column_headers, row)))

    return jsonify(json_data)

# Get all the flights history for this enterprise
@enterprises.route('/EntFlights', methods=['GET'])
def get_flights():
    cursor = db.get_db().cursor()

    cursor.execute('SELECT * FROM Flight WHERE Flight.enterprise_id = 1')

    column_headers = [x[0] for x in cursor.description]

    json_data = []

    theData = cursor.fetchall()

    for row in theData:
        json_data.append(dict(zip(column_headers, row)))

    return jsonify(json_data)