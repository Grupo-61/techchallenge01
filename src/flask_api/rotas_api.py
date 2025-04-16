from ..scraper.webscraping import obtemDados, obtemJsonProducao, obtemJsonProcessamento, obtemJsonComercializacao, obtemJsonImportacao, obtemJsonExportacao
from flask import Blueprint


# Definir o Blueprint
rotas_bp = Blueprint('rotas', __name__)


# producao ok
@rotas_bp.route("/producao/ano=<ano>", methods=['GET'])
def producao(ano):
    return obtemJsonProducao(ano)

# processamento
@rotas_bp.route("/processamento/ano=<ano>", methods=['GET'])
def processamento(ano):
    return obtemJsonProcessamento(ano)

# comercializacao ok
@rotas_bp.route("/comercializacao/ano=<ano>", methods=['GET'])
def comercializacao(ano):
    return obtemJsonComercializacao(ano)

# importacao
@rotas_bp.route("/importacao/ano=<ano>", methods=['GET'])
def importacao(ano):
    return obtemJsonImportacao(ano)

# exportacao
@rotas_bp.route("/exportacao/ano=<ano>", methods=['GET'])
def exportacao(ano):
    return obtemJsonExportacao(ano)