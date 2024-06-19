from flask import Flask
from models.base import db 
from models.user import User
from models.role import Role
from models.user_role import UserRole
from controller.userController import userControllerBp
from controller.oauthController import oauthControllerBp
from controller.roleController import roleControllerBp
app = Flask(__name__)

app.register_blueprint(userControllerBp)
app.register_blueprint(oauthControllerBp)
app.register_blueprint(roleControllerBp)

def create_tables():
    with db:
        db.create_tables([User, Role, UserRole]) 

if __name__ == '__main__':
    create_tables()
    app.run(debug=True, port=1337)