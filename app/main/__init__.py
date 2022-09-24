from flask import Flask
from .restcontroller.api import api
from .dbservice import db

from .config import config_by_name



def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    db.init_app(app)
    app.register_blueprint(api)


    return app
