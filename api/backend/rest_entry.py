import logging

logging.basicConfig(level=logging.DEBUG)

import os

from flask import Flask
from backend.db_connection import db
from backend.enterprises.enterprises_routes import enterprises
from backend.ngo.ngo_routes import ngo
from backend.user.user_routes import user
from dotenv import load_dotenv


def create_app():
    app = Flask(__name__)

    # Load environment variables
    load_dotenv()
    testvar = os.getenv("TEST_VAR")
    app.logger.info(f"testvar is {testvar}")

    # secret key that will be used for securely signing the session
    # cookie and can be used for any other security related needs by
    # extensions or your application
    # app.config['SECRET_KEY'] = 'someCrazyS3cR3T!Key.!'
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

    # # these are for the DB object to be able to connect to MySQL.
    # app.config['MYSQL_DATABASE_USER'] = 'root'
    app.config["MYSQL_DATABASE_USER"] = os.getenv("DB_USER")
    app.config["MYSQL_DATABASE_PASSWORD"] = os.getenv("MYSQL_ROOT_PASSWORD")
    app.config["MYSQL_DATABASE_HOST"] = os.getenv("DB_HOST")
    app.config["MYSQL_DATABASE_PORT"] = int(os.getenv("DB_PORT"))
    app.config["MYSQL_DATABASE_DB"] = os.getenv(
        "DB_NAME"
    )  # Change this to your DB name

    # Initialize the database object with the settings above.
    db.init_app(app)

    # Add the default route
    # Can be accessed from a web browser
    # http://ip_address:port/
    # Example: localhost:8001
    @app.route("/")
    def welcome():
        return "<h1>Welcome to the Summer 2024 Belgium DoC Boilerplate App</h1>"

    # Example route for testing streamlit
    app.logger.info("current_app(): registering blueprints with app object.")
    # Register the routes from each Blueprint with the app object
    # and give a url prefix to each
    app.register_blueprint(enterprises, url_prefix="/e")
    app.register_blueprint(ngo, url_prefix="/n")
    app.register_blueprint(user, url_prefix="/u")

    # Don't forget to return the app object
    return app
