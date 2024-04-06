from peewee import IntegrityError
from models.user import User

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