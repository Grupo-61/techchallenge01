import pandas as pd

# guarda anos df
anos= []

# aba produção
def obtemDataOffProducao(aba, ano): 
    df= pd.read_csv("api/data/data_offline/producao/" + aba + ".csv", sep=";")
    
    # obtem anos df
    for anos_df in df:
        anos.append(anos_df)

    if str(ano) in anos:
        json= df[['produto', str(ano)]].to_json(orient='records', force_ascii=False, indent=4)

        # trato json
        json= json.replace("\n", "").replace("\"", "")
        json= json.replace("-", "0.00").replace("nd", "0.00") 
        json= json.replace(str(ano) + ":", "Quantidade (L.): ") 
        
        return json, 200 # Ok
    
    return {"error": f"A conexão com o site da Embrapa não ocorreu com sucesso. Não há dados offline disponíveis para o ano {ano}."}, 404 # Not Found

# aba processamento
def obtemDataOffProcessamento(aba, ano):
    df= pd.read_csv("api/data/data_offline/processamento/" + aba + ".csv", sep=";", encoding='unicode_escape')

    # obtem anos df
    for anos_df in df:
        anos.append(anos_df)

    if str(ano) in anos:
        json= df[['cultivar', str(ano)]].to_json(orient='records', force_ascii=False, indent=4)

        # trato json
        json= json.replace("\n", "").replace("\"", "")
        json= json.replace("-", "0.00").replace("nd", "0.00") 
        json= json.replace(str(ano) + ":", "Quantidade (Kg): ")
        
        return json, 200 # Ok
    
    return {"error": f"A conexão com o site da Embrapa não ocorreu com sucesso. Não há dados offline disponíveis para o ano {ano}."}, 404 # Not Found

# aba comercialização
def obtemDataOffComercializacao(aba, ano):  
    df= pd.read_csv("data/data_offline/comercializacao/" + aba + ".csv", sep=";")

    # obtem anos df
    for anos_df in df:
        anos.append(anos_df)

    if str(ano) in anos:
        json= df[['produto', str(ano)]].to_json(orient='records', force_ascii=False, indent=4) 

        # trato json
        json= json.replace("\n", "").replace("\"", "")
        json= json.replace("-", "0.00").replace("nd", "0.00") 
        json= json.replace(str(ano) + ":", "Quantidade (L.):") 
        
        return json, 200 # Ok
    
    return {"error": f"A conexão com o site da Embrapa não ocorreu com sucesso. Não há dados offline disponíveis para o ano {ano}."}, 404 # Not Found

# aba importação
def obtemDataOffImportacao(aba, ano):  
    df= pd.read_csv("data/data_offline/importacao/" + aba + ".csv", sep=";")

    # obtem anos df
    for anos_df in df:
        anos.append(anos_df)

    if str(ano) in anos:
        json= df[['Países', str(ano), str(float(ano) + 0.1)]].to_json(orient='records', force_ascii=False, indent=4)

        # trato json
        json= json.replace("\n", "").replace("\"", "") 
        json= json.replace("-", "0").replace("nd", "0") 
        json= json.replace(str(ano) + ":", "Quantidade (Kg): ") 
        json= json.replace(str(float(ano) + 0.1) + ":", "Valor (US$): ")
        
        return json, 200 # Ok
    
    return {"error": f"A conexão com o site da Embrapa não ocorreu com sucesso. Não há dados offline disponíveis para o ano {ano}."}, 404 # Not Found

# aba exportação
def obtemDataOffExportacao(aba, ano):  
    df= pd.read_csv("data/data_offline/exportacao/" + aba + ".csv", sep=";")

    # obtem anos df
    for anos_df in df:
        anos.append(anos_df)

    if str(ano) in anos:
        json= df[['Países', str(ano), str(float(ano) + 0.1)]].to_json(orient='records', force_ascii=False, indent=4)

        # trato json
        json= json.replace("\n", "").replace("\"", "") 
        json= json.replace("-", "0").replace("nd", "0") 
        json= json.replace(str(ano) + ":", "Quantidade (Kg): ") 
        json= json.replace(str(float(ano) + 0.1) + ":", "Valor (US$): ")
        
        return json, 200 # Ok
    
    return {"error": f"A conexão com o site da Embrapa não ocorreu com sucesso. Não há dados offline disponíveis para o ano {ano}."}, 404 # Not Found