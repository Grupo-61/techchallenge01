import pytest
import requests
from unittest.mock import patch, Mock
from api.src.scraper.webscraping import obtemDados

@pytest.fixture
def mock_response():
    """Cria uma resposta simulada para os testes."""
    response = Mock()
    response.status_code = 200
    response.text = """
    <html>
        <body>
            <table class="tb_base tb_dados">
                <tr><th>Coluna1</th><th>Coluna2</th></tr>
                <tr><td>Dado1</td><td>Dado2</td></tr>
            </table>
        </body>
    </html>
    """
    return response

def test_obtemDados_sucesso(mock_response):
    """Testa o caso de sucesso ao obter dados da URL."""
    with patch("requests.get", return_value=mock_response):
        df, status_code = obtemDados("http://fakeurl.com")
        
        assert status_code == 200
        assert list(df.columns) == ["Coluna1", "Coluna2"]
        assert df.iloc[0].to_list() == ["Dado1", "Dado2"]

def test_obtemDados_erro_requisicao():
    """Testa o caso de erro na requisição (exemplo: URL inválida)."""
    with patch("requests.get", side_effect=requests.exceptions.RequestException):
        df, status_code = obtemDados("http://fakeurl.com")
        
        assert status_code == 500

def test_obtemDados_status_code_erro(mock_response):
    """Testa o caso de código de status diferente de 200."""
    mock_response.status_code = 404
    with patch("requests.get", return_value=mock_response):
        df, status_code = obtemDados("http://fakeurl.com")
        
        assert df.empty
        assert status_code == 404