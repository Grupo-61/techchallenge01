from flask_restx import Resource, Namespace
from .config import api

ns_producao = Namespace('producao', description='Produção')

@ns_producao.route('/producao/ano=<int:ano>')
class ProducaoResource(Resource):
    @ns_producao.doc('/producao')
    def get(self):
        """Obtém a lista de users"""
        return {
        "status_code":200,
        "msg": "Sucesso",
        "data": [
            {
                "id": 1,
                "name": "John Doe",
                "email": "email@email.com.br"}]
    }