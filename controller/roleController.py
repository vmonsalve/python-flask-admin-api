from flask import Blueprint, jsonify, request
from models.role import Role
from helpers.roleHelpers import saveRole
from helpers.securityHelpers import verify_token


roleControllerBp = Blueprint('roles', __name__, url_prefix='/admin/roles')

@roleControllerBp.route('/')
def index():
    isAccess = verify_token(request.headers)
    if isAccess:
        roles = Role.select()
        if not roles:
            return jsonify({'msg': 'no hay datos para mostrar'}), 200
        rolesAll = [{'role': role.role, 'descripcion': role.description, 'estado': role.state} for role in roles]
        return jsonify(rolesAll), 200
    return jsonify({'msg': 'Unauthorized'}), 401

@roleControllerBp.route('/create', methods=['POST'])
def create():
    isAccess = verify_token(request.headers)
    if isAccess:
        if request.method == 'POST':
            role = saveRole(request.get_json())
            return jsonify({'msg': f'Role {role.role} guardado'}), 200
    return jsonify({'msg': 'Unauthorized'}), 401