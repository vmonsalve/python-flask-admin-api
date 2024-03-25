from models.user import User


user = User('Vicente Monsalve', 'vicente.monsalve@gmail.com', 'vmonsalve', 1)

pass_encrypt = user.encript_password()

print(pass_encrypt)