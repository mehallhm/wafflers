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
        WHERE EntTags.enterprise_id = (
            SELECT id 
            FROM Enterprises 
            ORDER BY id DESC 
            LIMIT 1
        )
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
        WHERE EntTags.enterprise_id = (
            SELECT id
            FROM Enterprises
            ORDER BY id DESC
            LIMIT 1
        )
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
    SELECT AVG(Enterprises.emission_result) AS avg_enterprise_emissions, Country.name AS your_country, (SELECT e2.emission_result
        FROM Enterprises e2
        ORDER BY e2.id DESC
        LIMIT 1) AS your_enterprise_emissions
    FROM Enterprises
    JOIN Country ON Enterprises.country_id = Country.id
    WHERE Country.name = (SELECT Country.name FROM Enterprises
    JOIN Country ON Enterprises.country_id = Country.id
    ORDER BY Enterprises.id DESC
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