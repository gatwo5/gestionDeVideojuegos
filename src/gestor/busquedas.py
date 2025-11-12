catalogo = {
    "zelda": {"titulo": "The Legend of Zelda", "anio": 1986, "genero": {"Acción"}},
    "mario": {"titulo": "Super Mario Odyssey", "anio": 2017, "genero": {"Acción"}},
    "plantavszombie": {"titulo": "Plantas vs Zombies", "anio": 2009, "genero": {"Estrategia"}},
    "stardew": {"titulo": "Stardew Valley", "anio": 2016, "genero": {"Rol"}},
}
# ===== CRUD ====== #
# - -- Create -- - #
# Como un constructor

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


## Pruebas
buscar_por_titulo('The Legend of Zelda')
buscar_parcial('Mario')
buscar_por_genero('Acción')
buscar_por_rango_anios(2000, 2020)