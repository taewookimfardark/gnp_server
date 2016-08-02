from application import db

class Match(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tag = db.Column(db.String(100))
    against = db.Column(db.String(100))
    where = db.Column(db.String(200))
    when = db.Column(db.String(100))
    matchinfo = db.Column(db.String(200))
    score_gnp = db.Column(db.Integer)
    score_enemy = db.Column(db.Integer)
    finish = db.Column(db.Boolean, default=False)
    win = db.Column(db.Boolean, default=False)
    createdTime = db.Column(db.DateTime, default=db.func.now())

