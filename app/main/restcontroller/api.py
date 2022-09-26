from crypt import methods
from flask import Blueprint, jsonify, request
from ..dbservice.userdao import UserDao

api = Blueprint('api',__name__)

@api.route("/all")
def get_all_users():
    return UserDao().get_all()

@api.route("/new", methods=["POST"])
def add_new():
    data = request.get_json()
    UserDao().add_to_db(data)
    return "added"