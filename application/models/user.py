from application import db
from application.lib.jwt.jwt_helper import (jwt_encode)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(200))
    password = db.Column(db.String(500))
    name = db.Column(db.String(100))
    backnumber = db.Column(db.Integer)
    photourl = db.Column(db.String(2000))
    info = db.Column(db.String(1000))
    createdTime = db.Column(db.DateTime, default=db.func.now())
    def get_token_string(self):
        data = {
            "email" : self.email,
            "id" : self.id
        }
        return jwt_encode(data)


