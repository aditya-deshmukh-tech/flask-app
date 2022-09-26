from . import db
from flask import jsonify
from ..models.user import User

class UserDao():

    def add_to_db(self,data):
        try:
            user = User().from_json(data)
            db.session.add(user)
            db.session.commit()
        except Exception as e:
            return {"err": str(e)}
    
    def get_all(self):
        try:
            users = User.query.all()
            return jsonify([user.to_json() for user in users])
        except Exception as e:
            return {"err" : str(e)}
