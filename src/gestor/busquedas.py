from src.gestor.catalogo import catalogo

# - -- Buscar por título exacto -- - #
def buscar_por_titulo(titulo):
    result = None

    for x in catalogo.values():
        if x["titulo"].lower() == titulo.lower():
            result = x

    print(result)

# - -- Buscar por fragmento en el título -- - #
def buscar_parcial(trozo):
    result = []

    for x in catalogo.values():
        if trozo.lower() in x["titulo"].lower():
            result.append(x)

    print(result)

# - -- Buscar por género -- - #
def buscar_por_genero(genero_buscar):
    result = []

    for x in catalogo.values():
        for genero in x["genero"]:
            if genero.lower() == genero_buscar.lower():
                result.append(x)

    print(result)

# - -- Buscar por rango de años -- - #
def buscar_por_rango_anios(min, max):
    result = []

    for x in catalogo.values():
        anio = x["anio"]
        if min <= anio <= max:
            result.append(x)

    print(result)