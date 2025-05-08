import requests, json
from bs4 import BeautifulSoup
import pandas as pd
import logging
from api.src.scraper.obtem_dados_offline import obtemDataOffProducao, obtemDataOffProcessamento, obtemDataOffComercializacao, obtemDataOffImportacao, obtemDataOffExportacao
from api.src.scraper.urls import obtemUrls

# Configuração do logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
console_handler.setFormatter(formatter)

logger.addHandler(console_handler)


# Obtem dados url
  
def obtemDados(url): 
    logger.info(f"Obtendo dados da URL: {url}")

    try:
        response= requests.get(url)

        # verifica se requisição bem-sucedida
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        logging.error(f"Erro ao acessar a URL {url}: {e}")
        return pd.DataFrame(), 500

    # retorna erro conexao
    if response.status_code != 200:
        return pd.DataFrame(), response.status_code

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

    # converte os dados em um Dataframe do pandas
    return pd.DataFrame(data[1:], columns=data[0]), response.status_code 

# obtem Json Produção

def obtemJsonProducao(ano):
    
    # obtenho url dos dados
    urls = obtemUrls("Producao", ano)

    data = {}

    # itero sobre as urls da aba Produção
    for aba in urls:       
        url= urls[aba][0]   # obtenho a url        
        df, status_code= obtemDados(url) # obtenho dos dados da url

        # conexão ok
        if status_code == 200:
            
            # obtem dados online
            if df.iloc[:,1].max() > 0:

                # trato json
                json = df.to_json(orient='records', force_ascii=False, indent=4).replace("\n", "").replace("\"", "") 
                json= json.replace("-", "0").replace("nd", "0")
                data[aba] = json # guardo json para cada aba 

            else:
                data[aba]= {"error": f"A conexão com o site da Embrapa ocorreu com sucesso, porém não foram encontrados dados para o ano {ano}."}

        # conexão nok
        else:            
            json, _ = obtemDataOffProducao(aba, ano)    
            data[aba] = json # guardo json para cada aba         
            
    return data

# Obtem Json Processamento

def obtemJsonProcessamento(ano):

    # obtenho url dos dados
    urls = obtemUrls("Processamento", ano)

    data = {}

    # itero sobre as urls da aba processamento
    for aba in urls:       
        url = urls[aba][0]   # obtenho a url        
        df, status_code= obtemDados(url) # obtenho dos dados da url

        # conexão ok
        if status_code == 200:
            
            # obtem dados online
            if df.iloc[:,1].max() > 0:

                # trato json
                json = df.to_json(orient='records', force_ascii=False, indent=4).replace("\n", "").replace("\"", "") 
                json= json.replace("-", "0").replace("nd", "0")
                data[aba] = json # guardo json para cada aba 

            else:
                data[aba]= {"error": f"A conexão com o site da Embrapa ocorreu com sucesso, porém não foram encontrados dados para o ano {ano}."}

        # conexão nok        
        else:            
            json, _ = obtemDataOffProcessamento(aba, ano)    
            data[aba] = json # guardo json para cada aba 
            
    return data

# obtem Json Comercialização

def obtemJsonComercializacao(ano):

    # obtenho url dos dados
    urls = obtemUrls("Comercializacao", ano)

    data = {}

    # itero sobre as urls da aba Comercializacao
    for aba in urls:       
        url = urls[aba][0]   # obtenho a url        
        df, status_code= obtemDados(url) # obtenho dos dados da url

        # conexão ok
        if status_code == 200:
            
            # obtem dados online
            if df.iloc[:,1].max() > 0:

                # trato json
                json = df.to_json(orient='records', force_ascii=False, indent=4).replace("\n", "").replace("\"", "") 
                json= json.replace("-", "0").replace("nd", "0")
                data[aba] = json # guardo json para cada aba 

            else:
                data[aba]= {"error": f"A conexão com o site da Embrapa ocorreu com sucesso, porém não foram encontrados dados para o ano {ano}."}

        # conexão nok
        else:            
            json, _ = obtemDataOffComercializacao(aba, ano)    
            data[aba] = json # guardo json para cada aba 
            
    return data

# Obtem Json Importação

def obtemJsonImportacao(ano):

    # obtenho url dos dados
    urls = obtemUrls("Importacao", ano)

    data = {}

    # itero sobre as urls da aba Importacao
    for aba in urls:       
        url = urls[aba][0]   # obtenho a url        
        df, status_code= obtemDados(url) # obtenho dos dados da url

        # conexão ok
        if status_code == 200:
            
            # obtem dados online
            if df.iloc[:,1].max() > 0:

                # trato json
                json = df.to_json(orient='records', force_ascii=False, indent=4).replace("\n", "").replace("\"", "") 
                json= json.replace("-", "0").replace("nd", "0")
                data[aba] = json # guardo json para cada aba 

            else:
                data[aba]= {"error": f"A conexão com o site da Embrapa ocorreu com sucesso, porém não foram encontrados dados para o ano {ano}."}

        # conexão nok
        else:            
            json, _ = obtemDataOffImportacao(aba, ano)    
            data[aba] = json # guardo json para cada aba 
            
    return data

# Obtem Json Exportação

def obtemJsonExportacao(ano):

    # obtenho url dos dados
    urls = obtemUrls("Exportacao", ano)    

    data = {}

    # itero sobre as urls da aba Exportação
    for aba in urls:       
        url = urls[aba][0]   # obtenho a url        
        df, status_code= obtemDados(url) # obtenho dos dados da url

        # conexão ok
        if status_code == 200:
            
            # obtem dados online
            if df.iloc[:,1].max() > 0:

                # trato json
                json = df.to_json(orient='records', force_ascii=False, indent=4).replace("\n", "").replace("\"", "") 
                json= json.replace("-", "0").replace("nd", "0")
                data[aba] = json # guardo json para cada aba 

            else:
                data[aba]= {"error": f"A conexão com o site da Embrapa ocorreu com sucesso, porém não foram encontrados dados para o ano {ano}."}

        # conexão nok
        else:            
            json, _ = obtemDataOffExportacao(aba, ano)    
            data[aba] = json # guardo json para cada aba 
             
    return data