import json
from flask import Blueprint, request, jsonify, current_app
from backend.db_connection import db
from backend.ml_models.db_vector_helpers import stack_matrices, string_to_sparse_matrix
from backend.ml_models.model_beta import predict
import numpy as np


ngo = Blueprint("ngo", __name__)
current_id = 1


# All the NGO Data for use in the tfidf model
@ngo.route("/NGOMatch/<int:user_id>", methods=["GET"])
def get_ngo_match(user_id):
    """
    Gets the NGOs that match to a particular user. Returns
    """
    matching_num = request.args.get("q")

    cursor = db.get_db().cursor()
    cursor.execute("SELECT name, website, bio, vectorized_bio FROM NGO")
    column_headers = [x[0] for x in cursor.description]
    json_data = []
    returned_data = cursor.fetchall()

    # Pull user bio from db
    bio_query = "SELECT User.bio FROM User WHERE User.id = %s"
    cursor.execute(bio_query, user_id)
    bio = cursor.fetchone()[0]

    for row in returned_data:
        json_data.append(dict(zip(column_headers, row)))

    names = []
    vecs = []
    for item in json_data:
        names.append(
            {
                "name": item["name"],
                "website": item["website"],
                "bio": item["bio"][:200] + "...",
            }
        )
        vecs.append(item["vectorized_bio"])

    # Get the idf and vocab from db, parse into vec using `string_to_sparse_matrix`
    idf_query = "SELECT idf FROM TFIDF_Encoding ORDER BY id DESC LIMIT 1"
    cursor.execute(idf_query)
    idf_element = cursor.fetchone()[0]

    vocabulary_query = "SELECT vocabulary FROM TFIDF_Encoding ORDER BY id DESC LIMIT 1"
    cursor.execute(vocabulary_query)
    vocabulary_element = cursor.fetchone()[0]

    idf = np.fromstring(idf_element[1:-1], dtype=np.float64, sep=",")
    vocabulary = json.loads(vocabulary_element)

    csr = [string_to_sparse_matrix(v) for v in vecs]
    tfidf = stack_matrices(csr)

    orgs, _ = predict(idf, vocabulary, tfidf, names, bio)

    return jsonify(orgs[: int(matching_num)])


# Gets my ngo data
@ngo.route("/ngomine", methods=["GET"])
def get_mine():
    cursor = db.get_db().cursor()

    cursor.execute("SELECT * FROM NGO WHERE id = 1")

    column_headers = [x[0] for x in cursor.description]

    json_data = []

    theData = cursor.fetchall()

    for row in theData:
        json_data.append(dict(zip(column_headers, row)))

    return jsonify(json_data)


# updates an ngo to the NGO table given filled out data
@ngo.route("/NGOupdate", methods=["PUT"])
def add_new_NGO():
    current_app.logger.info("ngo_routes.py: POST /NGOadd")

    recieved_data = request.json
    current_app.logger.info(recieved_data)

    name = recieved_data["name"]
    website = recieved_data["website"]
    email = recieved_data["email"]

    query = "UPDATE NGO SET website = %s, name = %s, contact = %s WHERE id = 1"

    data = (name, website, email)
    cursor = db.get_db().cursor()
    cursor.execute(query, data)
    db.get_db().commit()

    # new_id = cursor.lastrowid

    # selected_tags = recieved_data.get('tags', [])
    # if selected_tags:
    #     insert_query = 'INSERT INTO NGOTags (ngo_id, tag_id) VALUES (%s, %s)'
    #     # for each tag gets the tag_id from the emission tags table, :)
    #     # also inserts into NGO tags
    #     for tag_name in selected_tags:
    #         tag_query = 'SELECT id FROM EmissionTags WHERE description = %s'
    #         cursor.execute(tag_query, (tag_name,))
    #         tag_row = cursor.fetchone()
    #         tag_id = tag_row[0]
    #         cursor.execute(insert_query, (new_id, tag_id))
    #         db.get_db().commit()

    return "Success"


@ngo.route("/tags", methods=["GET"])
def get_tags():
    # get a cursor object from the database
    cursor = db.get_db().cursor()
    cursor.execute(
        """
       SELECT description
       FROM EmissionTags
       WHERE EmissionTags.id IN (
           SELECT tag_id
           FROM NGOTags
           WHERE NGOTags.ngo_id = 1
       );
   """
    )

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


# get all of the matching Enterprises based on tags
@ngo.route("/EnterpriseMatch", methods=["GET"])
def get_matches():
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    cursor.execute(
        """
   SELECT DISTINCT Enterprises.name, EmissionTags.description
   FROM Enterprises
   JOIN EntTags ON Enterprises.id = EntTags.enterprise_survey_id
   JOIN EmissionTags ON EntTags.tag_id = EmissionTags.id
   WHERE EmissionTags.id IN (
       SELECT tag_id
       FROM EntTags
       WHERE EntTags.enterprise_survey_id = 1
   );
"""
    )

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


@ngo.route("/NGOadd", methods=["POST"])
def add_tags():
    current_app.logger.info("POST /ngo/tags route")

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

    insert_query = "INSERT INTO NGOTags (ngo_id, tag_id) VALUES (1, %s)"
    cursor.execute(insert_query, (new_tag_id,))
    db.get_db().commit()

    return jsonify({"message": "Success"}), 200


@ngo.route("/TagDelete", methods=["DELETE"])
def delete_tags():
    current_app.logger.info("DELETE /ngo/tags route")

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
    DELETE FROM NGOTags WHERE ngo_id = 1 AND tag_id = %s;
    """
    cursor.execute(delete_query, (tag_id,))
    db.get_db().commit()

    current_app.logger.info(f"Successfully deleted tag: {tag_description} for NGO")
    return "Success"


# get all of the matching users based on tags
@ngo.route("/UserMatch", methods=["GET"])
def get_usermatches():
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    cursor.execute(
        """
    SELECT DISTINCT User.name, User.email FROM User
    WHERE User.id IN
    (SELECT DISTINCT UserTags.user_id
        FROM UserTags
        WHERE UserTags.tag_id IN (
            SELECT tag_id
            FROM NGOTags
            WHERE NGOTags.ngo_id = 1
        )) AND User.match_consent = true;
"""
    )

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
