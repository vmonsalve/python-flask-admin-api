from datetime import datetime, timedelta
from dotenv import load_dotenv
import jwt
import pytz
import os

load_dotenv()

secret_key = os.getenv('JWT_SECRET_KEY')

def generate_security_jwt(user):
    time_zone = pytz.timezone('America/Santiago')
    ahora = datetime.now(tz=time_zone)
    payload = {
        'iat': ahora,
        'exp': ahora + timedelta(minutes=3),
        'username': user.username,
        'email': user.email
    }
    return jwt.encode(payload, secret_key, algorithm='HS256')

def verify_token(headers):
    if 'Authorization' in headers.keys():
        autorizations = headers['Authorization']
        encoded_token = autorizations.split(" ")[1]
        try:
            payload = jwt.decode(encoded_token, secret_key, algorithms=['HS256'])
            return True
        except (jwt.ExpiredSignatureError, jwt.ImmatureSignatureError):
            return False
    return False