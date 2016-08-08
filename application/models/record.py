from application import db
from user import User
from match import Match

class PlayerRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship(
        'User', foreign_keys=[userid],
        backref=db.backref(
            'user_list',
            cascade='all, delete-orphan',
            lazy='dynamic'
        )
    )
    games = db.Column(db.Integer)
    points = db.Column(db.Integer)
    rebounds = db.Column(db.Integer)
    assists = db.Column(db.Integer)

class MatchRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship(
        'User', foreign_keys=[userid],
        backref=db.backref(
            'room_list',
            cascade='all, delete-orphan',
            lazy='dynamic'
        )
    )
    matchid = db.Column(db.Integer, db.ForeignKey('match.id'))
    match = db.relationship(
        'Match', foreign_keys=[matchid],
        backref=db.backref(
            'match_list',
            cascade='all, delete-orphan',
            lazy='dynamic'
        )
    )
    point = db.Column(db.Integer)
    rebound = db.Column(db.Integer)
    assist = db.Column(db.Integer)