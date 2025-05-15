import pandas as pd
from obtem_dados_offline import obtemDataOffImportacao

aba= "uvas_passas"
df= pd.read_csv("data_offline/importacao/" + aba + ".csv", sep="\t")
df.to_csv("data_offline/importacao/" + aba + "_2.csv", sep=";")
json= obtemDataOffImportacao("vinhos_mesa", "2023")
print(json)