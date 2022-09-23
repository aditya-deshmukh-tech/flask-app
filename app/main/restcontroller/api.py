from flask import Blueprint, jsonify

api = Blueprint('api',__name__)

@api.route("/new")
def hello():
    return jsonify({"name": "flask-developer"})