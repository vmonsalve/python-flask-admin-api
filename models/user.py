from peewee import CharField, BooleanField
from .base import BaseModel
import bcrypt

class User(BaseModel):
    username = CharField()
    email = CharField()
    salt = CharField()
    password = CharField()
    state = BooleanField()

    def generate_salt(self):
        self.salt = bcrypt.gensalt()

    def encript_password(self):
        if not self.salt:
            self.generate_salt()
        password = self.password.encode()
        pass_hashed = bcrypt.hashpw(password, self.salt)
        self.password = pass_hashed.decode('utf-8')