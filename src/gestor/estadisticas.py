from catalogo import catalogo

# - -- Total de videojuegos -- - #
def total_juegos():
    total = len(catalogo)
    print(total)

# - -- Conteo por género -- - #
def cont_por_genero():
    cont = {}

    for x in catalogo.values():
        for genero in x["genero"]:
            if genero in cont:
                cont[genero] += 1
            else:
                cont[genero] = 1

    print(cont)