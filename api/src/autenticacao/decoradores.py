from functools import wraps
from flask import request, jsonify
from api.src.autenticacao.manipulador_jwt import verificar_token

def token_obrigatorio(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token = None
        if "Authorization" in request.headers:
            partes = request.headers["Authorization"].split(" ")
            if len(partes) == 2 and partes[0] == "Bearer":
                token = partes[1]

        if not token:
            return jsonify({"mensagem": "Token não fornecido"}), 401

        dados = verificar_token(token)
        if not dados:
            return jsonify({"mensagem": "Token inválido ou expirado"}), 401

        return f(*args, **kwargs)

    return decorator
