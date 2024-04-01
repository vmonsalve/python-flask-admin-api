from flask import Blueprint, jsonify, request
from helpers.userHelpers import saveUser

oauthControllerBp = Blueprint('oauth', __name__, url_prefix='/oauth')

@oauthControllerBp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        data = request.get_json()
        response = saveUser(data)
        return jsonify({'msg' : response})
    return jsonify({'msg' : f'Registrar usuario {request.url_root}'})

@oauthControllerBp.route('/enable/<int:user_id_hash>')
def enable(user_id_hash):

    pass