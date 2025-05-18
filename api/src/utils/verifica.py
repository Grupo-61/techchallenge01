def validar_dados(dados):
    """
    Esta função é usada par identificar os anos que possuem dados válidos.
    """

    chave_total = None
    for chave, valor in dados.items():
        if valor == "Total":
            chave_total = chave
            break

    if not chave_total:
        return False

    
    for chave, valor in dados.items():
        if chave == chave_total:
            continue  

        if valor not in [0, 0.0, "-", "0", "0.0"]:
            return False

    return True  # Retorna True os valores forem zerados
