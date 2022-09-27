from flask import Blueprint, jsonify, request
from ..dbservice.userdao import UserDao

api = Blueprint('api',__name__)

@api.route("/all")
def get_all_users():
    return UserDao().get_all()

@api.route("/get/<id>")
def get_one(id):
    return UserDao().get_by_username(id)


@api.route("/new", methods=["POST"])
def add_new():
    data = request.get_json()
    UserDao().add_to_db(data)
    return "added"

@api.route("/update", methods=["PUT"])
def update_one():
    data = request.get_json()
    return UserDao().update_by_username(data)

@api.route("/delete/<id>", methods=["DELETE"])
def delete_one(id):
    return UserDao().delete_by_username(id)
    