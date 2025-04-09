import pandas as pd

## aba produção
#def obtemDataOffProducao(aba, ano):  
#    if aba == "producao":
#        df= pd.read_csv("data_offline/" + aba + ".csv", sep=";")
#        return df[['produto', str(ano)]].to_json(orient='records', indent=4), 200   
#    
#    return 404 # Not Found

# aba produção
def obtemDataOffProducao(aba, ano):  
    df= pd.read_csv("data_offline/producao/" + aba + ".csv", sep=";")

    if len(df[str(ano)].unique()) > 0:

        # producao
        if aba == "producao":
            return df[['produto', str(ano)]].to_json(orient='records', indent=4), 200   
    
    return 404 # Not Found

# aba processamento
def obtemDataOffProcessamento(aba, ano):  
    df= pd.read_csv("data_offline/processamento/" + aba + ".csv", sep=";", encoding='unicode_escape')
    #print(df.head())

    if len(df[str(ano)].unique()) > 0:
        
        # viniferas
        if aba == "viniferas":
            return df[['cultivar', str(ano)]].to_json(orient='records', indent=4), 200
        
        # americanas hibridas
        if aba == "americanas_hibridas":
            return df[['cultivar', str(ano)]].to_json(orient='records', indent=4), 200
        
        # uvas_mesa
        if aba == "uvas_mesa":
            return df[['cultivar', str(ano)]].to_json(orient='records', indent=4), 200
        
        # uvas_mesa
        if aba == "sem_classificacao":
            return df[['cultivar', str(ano)]].to_json(orient='records', indent=4), 200
        
    return 404 # Not Found

# aba comercialização
def obtemDataOffComercializacao(aba, ano):  
    df= pd.read_csv("data_offline/comercializacao/" + aba + ".csv", sep=";")

    if len(df[str(ano)].unique()) > 0:

        # producao
        if aba == "producao":
            return df[['produto', str(ano)]].to_json(orient='records', indent=4), 200   
    
    return 404 # Not Found
    
#data= obtemDataOffComercializacao("producao", 2023)
#print(data)
