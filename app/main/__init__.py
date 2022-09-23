from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .restcontroller.api import api

from .config import config_by_name

db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.register_blueprint(api)
    app.config.from_object(config_by_name[config_name])
    db.init_app(app)

    return app
