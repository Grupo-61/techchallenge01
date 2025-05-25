from api.src.scraper.webscraping import obtemJsonPaginas
from flask import Blueprint
from api.src.autenticacao.decoradores import token_obrigatorio
import json
from flasgger import swag_from

# Definir o Blueprint
rotas_bp = Blueprint('rotas', __name__)

# producao ok
@rotas_bp.route("/producao/ano=<int:ano>", methods=['GET'])
@swag_from('../../apidocs/producao_doc.yml')
@token_obrigatorio
def producao(ano):
    return obtemJsonPaginas("Producao", "producao", ano)

# processamento
@rotas_bp.route("/processamento/ano=<int:ano>", methods=['GET'])
@swag_from("../../apidocs/processamento_doc.yml")
@token_obrigatorio
def processamento(ano):
    return obtemJsonPaginas("Processamento", "processamento", ano)

# comercializacao ok
@rotas_bp.route("/comercializacao/ano=<int:ano>", methods=['GET'])
@swag_from("../../apidocs/comercializacao_doc.yml")
@token_obrigatorio
def comercializacao(ano):
    return obtemJsonPaginas("Comercializacao", "comercializacao", ano)

# importacao
@rotas_bp.route("/importacao/ano=<int:ano>", methods=['GET'])
@swag_from("../../apidocs/importacao_doc.yml")
@token_obrigatorio
def importacao(ano):
    return obtemJsonPaginas("Importacao", "importacao", ano)

# exportacao
@rotas_bp.route("/exportacao/ano=<int:ano>", methods=['GET'])
@swag_from("../../apidocs/exportacao_doc.yml")
@token_obrigatorio
def exportacao(ano):
    return obtemJsonPaginas("Exportacao", "exportacao", ano)


@rotas_bp.route("/<entidade>/todos", methods=['GET'])
@swag_from("../../apidocs/entidade_doc.yml")
@token_obrigatorio
def dados(entidade):
    # Use lógica para escolher a função correta com base na entidade
    funcoes = {
        "producao": {
            "url": "Producao",
            "rota": "producao",
            "funcao": obtemJsonPaginas
        },
        "processamento": {
            "url": "Processamento",
            "rota": "processamento",
            "funcao": obtemJsonPaginas
        },
        "comercializacao": {
            "url": "Comercializacao",
            "rota": "comercializacao",
            "funcao": obtemJsonPaginas
        },
        "importacao": {
            "url": "Importacao",
            "rota": "importacao",
            "funcao": obtemJsonPaginas
        },
        "exportacao": {
            "url": "Exportacao",
            "rota": "exportacao",
            "funcao": obtemJsonPaginas
        },
    }
    funcao = funcoes.get(entidade, lambda x: {"erro": "Entidade inválida"})
    todos = []

    funcao_url = funcao.get("url", None)
    funcao_rota = funcao.get("rota", None)
    funcao_funcao = funcao.get("funcao", None)

    for i in range(1970, 2024):
        todos.extend([json.loads(funcao_funcao(funcao_url, funcao_rota, i))])

    return json.dumps(todos, ensure_ascii=False)