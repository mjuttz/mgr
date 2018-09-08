from flask_restful import Resource
from flask import request, render_template, make_response, redirect
from flask_login import  login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
import time
from datetime import datetime

from models.user import UserModel
from qrcode import QrCode
from yagmailsend import send

class UserRegister(Resource):
    def get(self):
        return make_response(render_template('register.html'), 200)

    def post(self):
        username = request.form['username']
        name = request.form['name']
        surname = request.form['surname']
        email = request.form['email']
        password = request.form['password']
        datetimestamp = str(datetime.fromtimestamp(time.time()).strftime('%H:%M:%S %d-%m-%Y'))

        #try:
        #    send(username,email)
        #except:
        #    return{"message": "A non-existent email address has been provided."}, 400

        try:
            UserModel(username,name,surname,email,generate_password_hash(password),
                datetimestamp).save_to_db()
        except:
            return {"message": "An error occured saving the user to the database"}, 500
        return {"message": "User registered succesfully"}, 201

class UserLogIn(Resource):
    def get(self):
        return make_response(render_template('login.html'), 200)

    def post(self):
        username = request.form['username']
        password = request.form['password']
        user = UserModel.query.filter_by(username=username).first()

        if user and check_password_hash(user.hash, password):
            login_user(user)
            return redirect('/book')
        return {'message': 'login failure'}, 401

class UserLogOut(Resource):
    @login_required
    def get(self):
        logout_user()
        return {'message': 'User has been logged out'}, 200

class MainPage(Resource):
    def get(self):
        return make_response(render_template('home.html'), 200)

    def post(self):
        return {'message': 'wszystko ok'}
