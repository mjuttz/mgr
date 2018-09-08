from flask_login import LoginManager
from models.user import UserModel

login_manager = LoginManager()

@login_manager.user_loader
def load_user(user_id):
     return UserModel.query.get(int(user_id))
