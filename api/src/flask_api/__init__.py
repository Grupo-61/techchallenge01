from flask import Flask
from flask_caching import Cache
from .rotas_api import rotas_bp
from ..autenticacao.rotas_autenticacao import autenticacao_bp

# Importe outros blueprints conforme necessário

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
    app.register_blueprint(autenticacao_bp, url_prefix="/auth")

    app.debug = True  # Ativar o modo de depuração para desenvolvimento

    return app