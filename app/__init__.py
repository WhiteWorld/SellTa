import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.uuid import FlaskUUID
from config import config

db = SQLAlchemy()
flask_uuid = FlaskUUID()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)
    flask_uuid.init_app(app)
    return app
app = create_app(os.getenv('FLASK_CONFIG') or 'default')