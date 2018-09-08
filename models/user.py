from db import db
from flask_login import UserMixin

class UserModel(UserMixin, db.Model):
    __tablename__='Users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    name = db.Column(db.String(80), nullable=False)
    surname = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    hash = db.Column(db.String(80), nullable=False)
    datetimestamp = db.Column(db.String(20), nullable=False)

    def __init__(self, username, name, surname, email, hash, datetimestamp):
        self.username = username
        self.name = name
        self.surname = surname
        self.email = email
        self.hash = hash
        self.datetimestamp = datetimestamp

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
