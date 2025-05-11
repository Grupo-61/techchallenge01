import requests
import json
from bs4 import BeautifulSoup
from api.src.scraper.urls import obtemUrls
from api.src.scraper.obtem_dados_offline import salvar_arquivo_json
from api.src.scraper.obtem_dados_offline import obtem_dados_offline
from api.src.utils.logger import Logger
from api.src.utils.verifica import validar_dados

log = Logger() 

def obtemDados(url): 
    log.info(f"Obtendo dados da URL: {url}")

    try:
        response= requests.get(url, timeout=30)

        # verifica se requisição bem-sucedida
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        mensagem_erro = {"mensagem": f"Erro ao acessar a URL {url}: {e}"}
        log.error(mensagem_erro)
        return mensagem_erro, 500

    # retorna erro conexao
    if response.status_code != 200:
        return {"mensagem": f"codigo de erro: {response.status_code}"}, response.status_code

    # parseia ao HTML da página usando o BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # encontra a tabela específica pela classe
    table = soup.find('table', {'class': 'tb_base tb_dados'})

    # extrai as linhas da tabela
    rows = table.find_all('tr')

    # controle cabecalho
    num_rows= 0

    # lista para armazenar os dados
    data = []

    # itera sobre as linhas e extrai o texto das células
    for row in rows:
        cells= row.find_all({'th', 'td'})
        cells_text= [cell.get_text(strip=True) for cell in cells]

        # cabecalho
        if num_rows == 0:
            data.append(cells_text)      
            num_rows= num_rows + 1      

        # dados
        else:
            cells_text[1]= float(cells_text[1].replace(".", "").replace("-", "0").replace("nd", "0"))
            #print(cells_text[1])
            data.append(cells_text)

    data_list = data[1:]
    columns = data[0]

    list_data = [dict(zip(columns, item)) for item in data_list]   

    return list_data, response.status_code


def obtemJsonPaginas(url, rota, ano):
    
    # obtenho url dos dados
    urls = obtemUrls(url, ano)
    data = {}

    # itero sobre as urls da aba Produção
    for aba in urls:       
        url= urls[aba][0]   # obtenho a url        
        list_data, status_code= obtemDados(url) # obtenho dos dados da url

        # conexão ok
        if status_code == 200:
            log.info(f"Consultando a URL {url}")

            # obtem dados online
            if len(list_data) > 0:
                if not validar_dados(list_data[-1]):
                    data[aba] = list_data # guardo json para cada aba                     
                    json_data = json.dumps({f"{rota}": {f"{ano}": {f"{aba}": list_data}}}, ensure_ascii=False)
                    salvar_arquivo_json(json_data, rota, ano, aba)
                else:
                    mensagem = f"Dados zerados para o ano {ano} na aba {aba}."
                    log.info(mensagem)
                    data = {"error": mensagem}
            else:
                data[aba] = {"error": f"A conexão com o site da Embrapa ocorreu com sucesso, porém não foram encontrados dados para o ano {ano}."}
        # conexão nok
        else:
            dados_recuperados = obtem_dados_offline(rota, ano, aba)  
            if rota in dados_recuperados:
                data[aba] = dados_recuperados[rota][f"{ano}"][aba]
            else:
                data[aba] = dados_recuperados
                log.error(f"Erro ao acessar a URL {url}: {dados_recuperados}")

    return json.dumps({f"{rota}": {f"{ano}": {f"{aba}": data}}}, ensure_ascii=False)