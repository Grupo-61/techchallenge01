from flask import Flask
from flask_caching import Cache
from .rotas_api import rotas_bp

from .swagger.config import api
from .swagger.rotas_api_doc import ns_producao

# Inicializar a aplicação Flask
cache = Cache()

def create_app():
    app = Flask(__name__)
    
    # Configurações do cache
    config = {
        "DEBUG": True,
        "CACHE_TYPE": "SimpleCache",
        "CACHE_DEFAULT_TIMEOUT": 300,
    }
    app.config.from_mapping(config)
    cache.init_app(app)

    # Registrar blueprints
    app.register_blueprint(rotas_bp)

    api.init_app(app)
    api.add_namespace(ns_producao)

    app.debug = True  # Ativar o modo de depuração para desenvolvimento


    return app