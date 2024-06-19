from peewee import IntegrityError
from models.user import User
from jsonschema import validate, ValidationError
import bcrypt


def validate_json_schema_register(data):
    schema = {
        "type": "object",
        "properties": {
            "email": {"type": "string"},
            "username" :{"type": "string"},
            "password": {"type": "string"}
        },
        "required": ["email", "password"]
    }
    try:
        validate(instance=data, schema=schema)
        return True
    except ValidationError as e:
        return False

def saveUser(data):
    try:
        new_user = User(
                username=data.get('username'),
                email=data.get('email'),
                password=data.get('password'),
                state=False
        )
        new_user.encript_password()
        new_user.save()

        return new_user.id
    except IntegrityError as e:
        return e
    
def enable_user(id):
    try:
        User.update(state=True).where(User.id == id).execute()
        return 'Usuario activado correctamente'
    except IntegrityError as e:
        return e
    
def get_user(email):
    user = User.get((User.email == email) & (User.state == True))
    return user

def validate_json_schema_login(data):
    schema = {
        "type": "object",
        "properties": {
            "email": {"type": "string"},
            "password": {"type": "string"}
        },
        "required": ["email", "password"]
    }

    try:
        validate(instance=data, schema=schema)
        return True
    except ValidationError as e:
        return False

def validate_data(data):
    if (data.get('email') == "") or (data.get('password') == ""):
        return False
    else:
        return True
    
def check_user(data):
    user = User.get((User.email == data.get('email')) & (User.state == True))
    if not user:
         return False
    else:
        if bcrypt.checkpw(data.get('password').encode('utf-8'), user.password.encode('utf-8')):
            return user
        else:
            return False