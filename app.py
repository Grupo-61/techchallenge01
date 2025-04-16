from flask import Flask, jsonify
from flask_caching import Cache
from src.flask_api import register_routes

# define configurações do cache
config = {
    "DEBUG": True,                  # some Flask specific configs
    "CACHE_TYPE": "SimpleCache",    # Flask-Caching related configs
    "CACHE_DEFAULT_TIMEOUT": 300    # timeout padrao
}

app = Flask(__name__)
app.config.from_mapping(config)
cache = Cache(app)

# Registra todas as rotas
register_routes(app, cache)

if __name__ == "__main__":
    app.run()