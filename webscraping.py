import requests, json
from bs4 import BeautifulSoup
import pandas as pd
from obtemDadosOffline import obtemDataOffProducao, obtemDataOffProcessamento, obtemDataOffComercializacao, obtemDataOffImportacao, obtemDataOffExportacao
from urls import obtemUrls

# Obtem dados url
  
def obtemDados(url): 
    response= requests.get(url)

    # verifica se requisição bem-sucedida
    response.raise_for_status()

    # retorna erro conexao
    if response.status_code != 200:
        return pd.DataFrame(), response.status_code

    # parseia ao HTML da página usando o BeautifulSoup
    soup= BeautifulSoup(response.text, 'html.parser')

    # encontra a tabela específica pela classe
    table= soup.find('table', {'class': 'tb_base tb_dados'})

    # extrai as linhas da tabela
    rows= table.find_all('tr')

    # lista para armazenar os dados
    data= []

    # itera sobre as linhas e extrai o texto das células
    for row in rows:
        cells= row.find_all({'th', 'td'})
        cells_text= [cell.get_text(strip=True) for cell in cells]
        data.append(cells_text)

    # converte os dados em um Dataframe do pandas
    return pd.DataFrame(data[1:], columns=data[0]), response.status_code 

# obtem Json Produção

def obtemJsonProducao(ano):
    
    # obtenho url dos dados
    urls= obtemUrls("Producao", ano)

    data= {}

    # itero sobre as urls da aba Produção
    for aba in urls:       
        url= urls[aba][0]   # obtenho a url        
        df, status_code= obtemDados(url) # obtenho dos dados da url

        # obtem dados online
        if status_code == 200:     

            # trato dados
            json= df.to_json(orient='records', force_ascii=False, indent=4).replace("\n", "").replace("\"", "") 
            json= json.replace("-", "0.00").replace("nd", "0.00")
            data[aba]= json # guardo json para cada aba  

        # obtem dados offline
        else:            
            json, status_code= obtemDataOffProducao(aba, ano)    
            if status_code != 200:                
                return {"error": "dados não encontrados"}
            else:
                data[aba]= json # guardo json para cada aba  
            
    return data

# Obtem Json Processamento

def obtemJsonProcessamento(ano):

    # obtenho url dos dados
    urls= obtemUrls("Processamento", ano)

    data= {}

    # itero sobre as urls da aba processamento
    for aba in urls:       
        url= urls[aba][0]   # obtenho a url        
        df, status_code= obtemDados(url) # obtenho dos dados da url

        # obtem dados online
        if status_code == 200:            

            # trato dados
            json= df.to_json(orient='records', force_ascii=False, indent=4).replace("\n", "").replace("\"", "") 
            json= json.replace("-", "0").replace("nd", "0") 
            data[aba]= json # guardo json para cada aba        

        # obtem dados offline
        else:            
            json, status_code= obtemDataOffProcessamento(aba, ano)    
            if status_code != 200:                
                return {"error": "dados não encontrados"}
            else:
                data[aba]= json # guardo json para cada aba  
            
    return data

# obtem Json Comercialização

def obtemJsonComercializacao(ano):

    # obtenho url dos dados
    urls= obtemUrls("Processamento", ano)

    data= {}

    # itero sobre as urls da aba Comercializacao
    for aba in urls:       
        url= urls[aba][0]   # obtenho a url        
        df, status_code= obtemDados(url) # obtenho dos dados da url

        # obtem dados online
        if status_code == 200:            

            # trato dados
            json= df.to_json(orient='records', force_ascii=False, indent=4).replace("\n", "").replace("\"", "") 
            json= json.replace("-", "0").replace("nd", "0") 
            data[aba]= json # guardo json para cada aba     

        # obtem dados offline
        else:            
            json, status_code= obtemDataOffComercializacao(aba, ano)    
            if status_code != 200:                
                return {"error": "dados não encontrados"}
            else:
                data[aba]= json # guardo json para cada aba  
            
    return data

# Obtem Json Importação

def obtemJsonImportacao(ano):

    # obtenho url dos dados
    urls= obtemUrls("Importacao", ano)

    data= {}

    # itero sobre as urls da aba Importacao
    for aba in urls:       
        url= urls[aba][0]   # obtenho a url        
        df, status_code= obtemDados(url) # obtenho dos dados da url

        # obtem dados online
        if status_code == 200:            

            # trato dados
            json= df.to_json(orient='records', force_ascii=False, indent=4).replace("\n", "").replace("\"", "") 
            json= json.replace("-", "0").replace("nd", "0") 
            data[aba]= json # guardo json para cada aba     

        # obtem dados offline
        else:            
            json, status_code= obtemDataOffImportacao(aba, ano)    
            if status_code != 200:                
                return {"error": "dados não encontrados"}
            else:
                data[aba]= json # guardo json para cada aba  
            
    return data

# Obtem Json Exportação

def obtemJsonExportacao(ano):

    # obtenho url dos dados
    urls= obtemUrls("Exportacao", ano)    

    data= {}

    # itero sobre as urls da aba Exportação
    for aba in urls:       
        url= urls[aba][0]   # obtenho a url        
        df, status_code= obtemDados(url) # obtenho dos dados da url

        # obtem dados online
        if status_code == 200:            

            # trato dados
            json= df.to_json(orient='records', force_ascii=False, indent=4).replace("\n", "").replace("\"", "") 
            json= json.replace("-", "0").replace("nd", "0") 
            data[aba]= json # guardo json para cada aba     

        # obtem dados offline
        else:            
            json, status_code= obtemDataOffExportacao(aba, ano)    
            if status_code != 200:                
                return {"error": "dados não encontrados"}
            else:
                data[aba]= json # guardo json para cada aba  
            
    return data