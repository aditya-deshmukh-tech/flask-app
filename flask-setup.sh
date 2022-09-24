mkdir app
touch requirements.txt

cat <<EOF > wsgi.py
from app.main import create_app


if __name__ == '__main__':
    app = create_app('dev')
    app.app_context().push()
    app.run()
else:
    gunicorn_app = create_app('prod')
EOF
cd app
touch __init__.py
mkdir main
mkdir test
cd main

cat <<EOF > __init__.py
from flask import Flask
from .dbservice import db

from .config import config_by_name



def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    db.init_app(app)


    return app
EOF

cat <<EOF > config.py
import os

# uncomment the line below for postgres database url from environment variable
# postgres_local_base = os.environ['DATABASE_URL']

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_precious_secret_key')
    DEBUG = False


class DevelopmentConfig(Config):
    # uncomment the line below to use postgres
    # SQLALCHEMY_DATABASE_URI = postgres_local_base
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'flask_boilerplate_main.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'flask_boilerplate_test.db')
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = False
    # uncomment the line below to use postgres
    # SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')


config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)

key = Config.SECRET_KEY
EOF

mkdir dbservice
cd dbservice

cat <<EOF > __init__.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
EOF
cd ..
cd ..
cd test
touch __init__.py
cd ..
cd ..
echo "application setup complete"
