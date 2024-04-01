from flask import Flask
from models.base import db 
from models.user import User
from controller.userController import userControllerBp
from controller.oauthController import oauthControllerBp
app = Flask(__name__)

app.register_blueprint(userControllerBp)
app.register_blueprint(oauthControllerBp)

def create_tables():
    with db:
        db.create_tables([User]) 

if __name__ == '__main__':
    create_tables()
    app.run(debug=True)