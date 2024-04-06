from flask import Blueprint, jsonify, request
from helpers.userHelpers import saveUser, enable_user
import base64

oauthControllerBp = Blueprint('oauth', __name__, url_prefix='/oauth')

@oauthControllerBp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        data = request.get_json()
        response = saveUser(data)
        hash_identity = base64.b64encode(str(response).encode()).decode()

        return jsonify({
            'enableuser' : request.url_root+'oauth/enable/'+hash_identity
        })
    return jsonify({'msg' : f'Registrar usuario {request.url_root}'})

@oauthControllerBp.route('/enable/<user_id_hash>')
def enable(user_id_hash): 
    id = base64.b64decode(user_id_hash).decode()
    response = enable_user(id)
    return jsonify({'msg' : response})