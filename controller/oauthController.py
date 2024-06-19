from flask import Blueprint, jsonify, request
from helpers.userHelpers import saveUser, enable_user, check_user, validate_json_schema_login, validate_data
from helpers.securityHelpers import generate_security_jwt
import base64

oauthControllerBp = Blueprint('oauth', __name__, url_prefix='/oauth')

@oauthControllerBp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        data = request.get_json()
        response = saveUser(data)
        hash_identity = base64.b64encode(str(response).encode()).decode()
        return jsonify({
            'success' : request.url_root+'oauth/enable/'+hash_identity
        }), 200
    return jsonify({'msg' : f'Registrar usuario {request.url_root}'})

@oauthControllerBp.route('/enable/<user_id_hash>')
def enable(user_id_hash): 
    id = base64.b64decode(user_id_hash).decode()
    response = enable_user(id)
    return jsonify({'msg' : response})

@oauthControllerBp.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        if not request.is_json:
            return jsonify({'error': 'La solicitud debe ser JSON'}), 400
        
        data = request.get_json()

        if validate_json_schema_login(data) == False:
            return jsonify({'error': 'Solicitud enviada incorrecta'}), 400
        
        if validate_data(data) == False:
            return jsonify({'error': 'Campos vacios'}), 400
        
        if check_user(data) == False:
            return jsonify({'error': 'Usuario no existe o clave incorrecta'}), 400
        else:
            user = check_user(data)
            token = generate_security_jwt(user)
            return jsonify({'token' : token}), 200
    
@oauthControllerBp.route('/recuperarClave', methods=['POST'])
def recuperarClave():
    if request.method == 'POST':
        if not request.is_json:
            return jsonify({'error': 'La solicitud debe ser un json'})
    pass