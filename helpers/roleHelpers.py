from peewee import IntegrityError
from models.role import Role
from jsonschema import validate, ValidationError

def saveRole(data):
    try:
        new_role = Role(
                role=data['role'],
                description=data['description'],
                state=True
        )
        new_role.save()
        return new_role
    except IntegrityError as e:
        return e