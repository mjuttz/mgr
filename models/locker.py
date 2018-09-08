from db import db

class DepositLockerModel(db.Model):
    __tablename__='DepositLockers'

    locker_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), nullable=False)
    hash = db.Column(db.String(80), nullable=False)
    datetime_start = db.Column(db.String(20), nullable=False)
    datetime_end = db.Column(db.String(20), nullable=False)

    def __init__(self,username, email, hash, datetime_start, datetime_end):
        self.username = username
        self.email = email
        self.hash = hash
        self.datetime_start = datetime_start
        self.datetime_end = datetime_end

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
