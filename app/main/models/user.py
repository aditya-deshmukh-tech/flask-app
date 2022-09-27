from ..dbservice import db

class User(db.Model):
    __tablename__='users'
    username = db.Column(db.String(100),primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    adhar_id = db.Column(db.String(100), unique=True)


    def to_json(self):
        return {
            'username' : self.username,
            'first_name' : self.first_name,
            'last_name' : self.last_name,
            'adhar_id' : self.adhar_id
        }
    
    def from_json(self, data):
        self.adhar_id = data["adhar_id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.username = data["username"]
        return self

