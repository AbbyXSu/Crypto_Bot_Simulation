from application import db

class Reports(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    revenue = db.Column(db.String(500), nullable=False)
    expense = db.Column(db.String(500), nullable=False)
    PLtype = db.Column(db.String(500), nullable=False)
    income = db.Column(db.String(500), nullable=False)
    efficiency_ratio = db.Column(db.String(500), nullable=False)