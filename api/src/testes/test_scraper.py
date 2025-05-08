import pytest
import pandas as pd
import requests
from unittest.mock import patch, Mock
from scraper.webscraping import obtemDados, obtemDataOffImportacao

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
                <tr><td>Dado1</td><td>10.0</td></tr>
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
        assert not df.empty
        assert list(df.columns) == ["Coluna1", "Coluna2"]
        assert df.iloc[0].to_list() == ["Dado1", 100.0]

def test_obtemDados_erro_requisicao():
    """Testa o caso de erro na requisição (exemplo: URL inválida)."""
    with patch("requests.get", side_effect=requests.exceptions.RequestException):
        df, status_code = obtemDados("http://fakeurl.com")
        
        assert df.empty
        assert status_code == 500

def test_obtemDados_status_code_erro(mock_response):
    """Testa o caso de código de status diferente de 200."""
    mock_response.status_code = 404
    with patch("requests.get", return_value=mock_response):
        df, status_code = obtemDados("http://fakeurl.com")
        
        assert df.empty
        assert status_code == 404


@pytest.fixture
def mock_dataframe():
    """Cria um DataFrame simulado para os testes."""
    data = {
        'Países': ['Brasil', 'Argentina'],
        '2024': [1000, 2000],
        '2024.1': [5000, 8000]
    }
    return pd.DataFrame(data)

@patch("pandas.read_csv")
def test_obtemDataOffImportacao_sucesso(mock_read_csv, mock_dataframe):
    """Testa a função para um ano presente no DataFrame."""
    mock_read_csv.return_value = mock_dataframe

    json_result, status_code = obtemDataOffImportacao("test_aba", 2024)

    assert status_code == 200
    assert "Quantidade (Kg)" in json_result
    assert "Valor (US$)" in json_result

@patch("pandas.read_csv")
def test_obtemDataOffImportacao_ano_inexistente(mock_read_csv, mock_dataframe):
    """Testa a função para um ano que não está no DataFrame."""
    mock_read_csv.return_value = mock_dataframe

    json_result, status_code = obtemDataOffImportacao("test_aba", 2023)

    assert status_code == 404
    assert "error" in json_result