from peewee import IntegrityError
from models.user import User

def saveUser(data):
    try:
        new_user = User(
                username=data.get('username'),
                email=data.get('email'),
                password=data.get('password'),
                state=True
        )
        new_user.encript_password()
        new_user.save()

        return 'Guardado correctamente'
    except IntegrityError as e:
        return e