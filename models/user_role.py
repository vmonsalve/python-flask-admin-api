from peewee import Model, ForeignKeyField
from .base import db
from .user import User
from .role import Role

class UserRole(Model):
    user = ForeignKeyField(User)
    role = ForeignKeyField(Role)

    class Meta:
        database = db
