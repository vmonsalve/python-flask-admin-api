from flask import Blueprint, jsonify
from models.user import User

userControllerBp = Blueprint('users', __name__, url_prefix='/user')

@userControllerBp.route('/')
def index():
    users = User.select()
    usersAll = [{'username': user.username, 'email': user.email} for user in users]
    return jsonify(usersAll)