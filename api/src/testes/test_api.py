import pytest
from unittest.mock import patch
import os
from api.src.flask_api import create_app

@pytest.fixture
def client():
    """Configura um cliente de teste do Flask."""
    app = create_app()
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

@pytest.fixture
def auth_headers(client):
    """Mocka as credenciais e gera um token de login."""
    with patch.dict(os.environ, {"USUARIO_FIXO_USERNAME": "admin", "USUARIO_FIXO_SENHA": "123456"}):
        login_response = client.post("/auth/login", json={"usuario": "admin", "senha": "123456"})
        
        assert login_response.status_code == 200  # Confirma que login está funcionando
        token = login_response.get_json().get("token")
        return {"Authorization": f"Bearer {token}"}  # Retorna um cabeçalho válido para autenticação

def test_producao_sucesso(client, auth_headers):
    """Testa acesso bem-sucedido à rota com autenticação."""
    response = client.get("/producao/ano=2025", headers=auth_headers)
    assert response.status_code == 200

def test_producao_sem_token(client):
    """Testa acesso sem autenticação (deve falhar)."""
    response = client.get("/producao/ano=2025")
    assert response.status_code == 401

def test_producao_token_invalido(client):
    """Testa acesso com token inválido."""
    headers = {"Authorization": "Bearer token_invalido"}
    response = client.get("/producao/ano=2025", headers=headers)
    assert response.status_code == 401