import json
import os
from api.src.utils.logger import Logger

log = Logger() 


def salvar_arquivo_json(dados, tipo, ano, aba):

    nome_arquivo = f"{tipo}_{ano}_{aba}.json"
    caminho_diretorio = f"dados/dados_offline/{tipo}/"
    caminho_arquivo = f"{caminho_diretorio}{nome_arquivo}"

    log.info(f"Salvando arquivo {caminho_arquivo} offline")

    # Cria o diretório se não existir
    os.makedirs(caminho_diretorio, exist_ok=True)

    try:
        if not os.path.exists(caminho_arquivo):
            with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
                json.dump(dados, arquivo, ensure_ascii=False)
        log.info(f"Arquivo {nome_arquivo} salvo com sucesso.")
        
    except Exception as e:
        log.error(f"Erro ao salvar o arquivo {nome_arquivo}: {e}")

def obtem_dados_offline(tipo, ano, aba):

    nome_arquivo = f"{tipo}_{ano}_{aba}.json"
    caminho_arquivo = f"api/dados/dados_offline/{tipo}/{nome_arquivo}"

    log.info(f"Recuperando arquivo {caminho_arquivo} offline.")
    
    if not os.path.exists(caminho_arquivo):
        log.error(f"O arquivo {nome_arquivo} não foi encontrado.")
        return {"error": f"Não foi posssível retornar dados para essa data. Tentar novamente mais tarde."}

    # Ler o arquivo JSON
    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
        dados = json.load(arquivo)
    
    return json.loads(dados)