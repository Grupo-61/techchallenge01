from flask import Blueprint, request, jsonify
from .manipulador_jwt import criar_token

autenticacao_bp = Blueprint('autenticacao', __name__)

# Pode ser movido para .env
USUARIO_FIXO = {
    "usuario": "admin",
    "senha": "123456"
}

@autenticacao_bp.route("/login", methods=["POST"])
def login():
    dados = request.get_json()

    if not dados or "usuario" not in dados or "senha" not in dados:
        return jsonify({"mensagem": "Usuário e senha são obrigatórios"}), 400

    if dados["usuario"] == USUARIO_FIXO["usuario"] and dados["senha"] == USUARIO_FIXO["senha"]:
        token = criar_token(dados["usuario"])
        return jsonify({"token": token})

    return jsonify({"mensagem": "Usuário ou senha inválidos"}), 401
