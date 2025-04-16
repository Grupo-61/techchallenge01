# producao
def obtemUrls(menu, ano):

    if menu == "Producao":
        return {
            # aba : url
            "producao" : ["http://vitibrasil.cnpuv.embrapa.br/index.php?ano=" + str(ano) + "&opcao=opt_02"]
        }

    if menu == "Processamento":
        return {
            # aba : url
            "viniferas" : ["http://vitibrasil.cnpuv.embrapa.br/index.php?ano=" + str(ano) + "&opcao=opt_03&subopcao=subopt_01"],
            "americanas_hibridas" : ["http://vitibrasil.cnpuv.embrapa.br/index.php?ano=" + str(ano) + "&opcao=opt_03&subopcao=subopt_02"],
            "uvas_mesa" : ["http://vitibrasil.cnpuv.embrapa.br/index.php?ano=" + str(ano) + "&opcao=opt_03&subopcao=subopt_03"],
            "sem_classificacao" : ["http://vitibrasil.cnpuv.embrapa.br/index.php?ano=" + str(ano) + "&opcao=opt_03&subopcao=subopt_04"] 
        }

    if menu == "Comercializacao":
        return {
        # aba : url
        "producao" : ["http://vitibrasil.cnpuv.embrapa.br/index.php?ano=" + str(ano) + "&opcao=opt_04"]
    }

    if menu == "Importacao":
        return {
        # aba : url
        "vinhos_mesa" : ["http://vitibrasil.cnpuv.embrapa.br/index.php?ano=" + str(ano) + "&opcao=opt_05&subopcao=subopt_01"],
	    "espumantes" : ["http://vitibrasil.cnpuv.embrapa.br/index.php?ano=" + str(ano) + "&opcao=opt_05&subopcao=subopt_02"],
	    "uvas_frescas" : ["http://vitibrasil.cnpuv.embrapa.br/index.php?ano=" + str(ano) + "&opcao=opt_05&subopcao=subopt_03"],
	    "uvas_passas" : ["http://vitibrasil.cnpuv.embrapa.br/index.php?ano=" + str(ano) + "&opcao=opt_05&subopcao=subopt_04"],
	    "suco_uva" : ["http://vitibrasil.cnpuv.embrapa.br/index.php?ano=" + str(ano) + "&opcao=opt_05&subopcao=subopt_05"]
    }

    if menu == "Exportacao":
        return {
        # aba : url
        "vinhos_mesa" : ["http://vitibrasil.cnpuv.embrapa.br/index.php?ano=" + str(ano) + "&opcao=opt_06&subopcao=subopt_01"],
		"espumantes" : ["http://vitibrasil.cnpuv.embrapa.br/index.php?ano=" + str(ano) + "&opcao=opt_06&subopcao=subopt_02"],
		"uvas_frescas" : ["http://vitibrasil.cnpuv.embrapa.br/index.php?ano=" + str(ano) + "&opcao=opt_06&subopcao=subopt_03"],
		"suco_uva" : ["http://vitibrasil.cnpuv.embrapa.br/index.php?ano=" + str(ano) + "&opcao=opt_06&subopcao=subopt_04"]
    }


