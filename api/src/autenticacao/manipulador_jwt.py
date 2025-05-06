import jwt
import datetime
from dotenv import load_dotenv
import os

load_dotenv()

CHAVE_SECRETA = os.getenv("JWT_SECRET_KEY")

def criar_token(usuario):
    payload = {
        "usuario": usuario,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    }
    token = jwt.encode(payload, CHAVE_SECRETA, algorithm="HS256")
    return token

def verificar_token(token):
    try:
        payload = jwt.decode(token, CHAVE_SECRETA, algorithms=["HS256"])
        return payload
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None
