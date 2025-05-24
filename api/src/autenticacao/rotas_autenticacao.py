from flask import Blueprint, request, jsonify
from api.src.autenticacao.manipulador_jwt import criar_token
from dotenv import load_dotenv
import os

load_dotenv()

CHAVE_SECRETA = os.getenv("JWT_SECRET_KEY")

autenticacao_bp = Blueprint('autenticacao', __name__)

USUARIO_FIXO = {
    "usuario": os.environ.get("USUARIO_FIXO_USERNAME"),
    "senha": os.environ.get("USUARIO_FIXO_SENHA")
}

@autenticacao_bp.route("/login", methods=["POST"])
def login():
    dados = request.get_json()

    print(f"Dados recebidos: {dados}")

    if not dados or "usuario" not in dados or "senha" not in dados:
        return jsonify({"mensagem": "Usuário e senha são obrigatórios"}), 400

    if dados["usuario"] == USUARIO_FIXO["usuario"] and dados["senha"] == USUARIO_FIXO["senha"]:
        token = criar_token(dados["usuario"])
        return jsonify({"token": token})

    return jsonify({"mensagem": "Usuário ou senha inválidos"}), 401
