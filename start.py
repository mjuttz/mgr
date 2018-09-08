from flask import Flask
from flask_restful import Resource, Api
from flask_login import LoginManager
from db import db
from lm import login_manager

from resources.user import UserRegister, MainPage
from resources.user import UserLogIn
from resources.locker import DepositLocker
from resources.user import UserLogOut

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'dev'
api = Api(app)
login_manager.init_app(app)

db.init_app(app)
with app.test_request_context():
    db.create_all()

api.add_resource(UserRegister, '/register')
api.add_resource(UserLogIn, '/login')
api.add_resource(DepositLocker, '/book')
api.add_resource(UserLogOut, '/logout')
api.add_resource(MainPage, '/home')

if __name__ == '__main__':
    app.run(debug=True, port=4999)
