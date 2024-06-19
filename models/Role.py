from peewee import CharField, BooleanField
from .base import BaseModel

class Role(BaseModel):
    role = CharField()
    description = CharField()
    state = BooleanField()
