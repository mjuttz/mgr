from flask_restful import Resource
from flask import request, render_template, make_response
from flask_login import login_required, LoginManager, current_user
import os

from models.locker import DepositLockerModel
from models.user import UserModel
from qrcode import QrCode
from yagmailsend import send

class DepositLocker(Resource):
    @login_required
    def get(self):
        return make_response(render_template('booking.html'),200)

    def post(self):
        username = current_user.username
        qr = QrCode(username)
        hash = qr.hash
        email = current_user.email
        datetime_start = request.form['time_start']+' '+request.form['date_start']
        datetime_end = request.form['time_end']+' '+request.form['date_end']

        qr.create_qr()

        try:
            send(username,email)
        except:
            return{"message": "A non-existent email address has been provided."}, 400
        finally:
            os.remove(username+'.png')

        DepositLockerModel(username,email,hash, datetime_start, datetime_end).save_to_db()
        return {'message': 'Deposit locker has been booked succesfully'}, 201
