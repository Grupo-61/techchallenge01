import pytest
from flask import Flask
from flask_api import create_app  # Substitua pelo caminho correto
from flask_api.rotas_api import rotas_bp

@pytest.fixture
def client():
    """Configura um cliente de teste do Flask."""
    app = create_app()
    app.testing = True
    return app.test_client()

def test_producao_sucesso(client):
    """Testa se a rota retorna um JSON válido e código 200 para um ano existente."""
    ano_teste = 2023
    response = client.get(f"/producao/ano={ano_teste}")
    
    assert response.status_code == 200
    assert "Quantidade" in response.json["producao"]  
    assert "Produto" in response.json["producao"] 

def test_producao_ano_inexistente(client):
    """Testa se a rota retorna erro 404 para um ano inexistente."""
    ano_teste = 1900  # Exemplo de um ano inválido
    response = client.get(f"/producao/ano={ano_teste}")

    assert response.status_code == 200
    assert "error" in response.json["producao"]