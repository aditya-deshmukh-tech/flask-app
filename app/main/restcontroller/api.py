from flask import Blueprint, jsonify
from ..models.user import User

api = Blueprint('api',__name__)

@api.route("/all")
def get_all_users():
    users = User.query.all()
    return jsonify([user.to_json() for user in users])