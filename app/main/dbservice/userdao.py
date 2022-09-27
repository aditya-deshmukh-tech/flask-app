from . import db
from flask import jsonify
from ..models.user import User

class UserDao():

    def add_to_db(self,data):
        try:
            user = User().from_json(data)
            db.session.add(user)
            db.session.commit()
            return {"success" : "data added"}
        except Exception as e:
            return {"err": str(e.__cause__)}
    
    def get_all(self):
        try:
            users = User.query.all()
            return jsonify([user.to_json() for user in users])
        except Exception as e:
            return {"err" : str(e)}

    def get_by_username(self, username):
        try:
            user = User.query.filter_by(username=username).first()
            return jsonify(user.to_json())
        except Exception as e:
            return {"err" : str(e)}

    def update_by_username(self, data):
        try:
            user = User.query.filter_by(username=data["username"]).first()
            user.first_name = data["first_name"]
            user.last_name = data["last_name"]
            user.adhar_id = data["adhar_id"]
            db.session.commit()
            return {"success" : "data for username updated" }
        except Exception as e:
            return {"err" : str(e)}

    def delete_by_username(self, data):
        try:
            if User.query.filter_by(username=data).delete() != 0:
                db.session.commit()
                return {"success" : "deleted successfully"}
            else:
                raise Exception("no record found for id")
        except Exception as e:
            return {"err" : str(e)}
