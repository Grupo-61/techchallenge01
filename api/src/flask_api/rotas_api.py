from ..scraper.webscraping import obtemDados, obtemJsonProducao, obtemJsonProcessamento, obtemJsonComercializacao, obtemJsonImportacao, obtemJsonExportacao
from flask import Blueprint
from ..autenticacao.decoradores import token_obrigatorio
from flasgger import swag_from

# Definir o Blueprint
rotas_bp = Blueprint('rotas', __name__)

# producao ok
@rotas_bp.route("/producao/ano=<int:ano>", methods=['GET'])
@swag_from('../../apidocs/producao_doc.yml')
@token_obrigatorio
def producao(ano):
    return obtemJsonProducao(ano)

# processamento ok
@rotas_bp.route("/processamento/ano=<int:ano>", methods=['GET'])
@swag_from("../../apidocs/processamento_doc.yml")
def processamento(ano):
    return obtemJsonProcessamento(ano)

# comercializacao ok
@rotas_bp.route("/comercializacao/ano=<int:ano>", methods=['GET'])
@swag_from("../../apidocs/comercializacao_doc.yml")
def comercializacao(ano):
    return obtemJsonComercializacao(ano)

# importacao ok
@rotas_bp.route("/importacao/ano=<int:ano>", methods=['GET'])
@swag_from("../../apidocs/importacao_doc.yml")
def importacao(ano):
    return obtemJsonImportacao(ano)

# exportacao ok
@rotas_bp.route("/exportacao/ano=<int:ano>", methods=['GET'])
@swag_from("../../apidocs/exportacao_doc.yml")
def exportacao(ano):
    return obtemJsonExportacao(ano)

# entidade (todas)
@rotas_bp.route("/<entidade>/todos", methods=['GET'])
@swag_from("../../apidocs/entidade_doc.yml")
def dados(entidade):
    # Use lógica para escolher a função correta com base na entidade
    funcoes = {
        "producao": obtemJsonProducao,
        "processamento": obtemJsonProcessamento,
        "comercializacao": obtemJsonComercializacao,
        "importacao": obtemJsonImportacao,
        "exportacao": obtemJsonExportacao,
    }
    funcao = funcoes.get(entidade, lambda x: {"erro": "Entidade inválida"})
    todos = {}
    for i in range(1970, 2024):
        todos[f"ano_{i}"] = funcao(i)

    return todos