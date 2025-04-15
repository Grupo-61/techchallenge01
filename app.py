from flask import Flask, jsonify
from flask_caching import Cache
from webscraping import obtemDados, obtemJsonProducao, obtemJsonProcessamento, obtemJsonComercializacao, obtemJsonImportacao, obtemJsonExportacao

# define configurações do cache
config = {
    "DEBUG": True,                  # some Flask specific configs
    "CACHE_TYPE": "SimpleCache",    # Flask-Caching related configs
    "CACHE_DEFAULT_TIMEOUT": 300    # timeout padrao
}

app = Flask(__name__)
app.config.from_mapping(config)
cache = Cache(app)

# producao ok
@app.route("/producao/ano=<ano>", methods=['GET'])
@cache.cached()
def producao(ano):
    return obtemJsonProducao(ano)

# processamento
@app.route("/processamento/ano=<ano>", methods=['GET'])
@cache.cached()
def processamento(ano):
    return obtemJsonProcessamento(ano)

# comercializacao ok
@app.route("/comercializacao/ano=<ano>", methods=['GET'])
@cache.cached()
def comercializacao(ano):
    return obtemJsonComercializacao(ano)

# importacao
@app.route("/importacao/ano=<ano>", methods=['GET'])
@cache.cached()
def importacao(ano):
    return obtemJsonImportacao(ano)

# exportacao
@app.route("/exportacao/ano=<ano>", methods=['GET'])
@cache.cached()
def exportacao(ano):
    return obtemJsonExportacao(ano)