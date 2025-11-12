catalogo = {
    "zelda": {"titulo": "The Legend of Zelda", "anio": 1986, "genero": {"Acción"}},
    "mario": {"titulo": "Super Mario Odyssey", "anio": 2017, "genero": {"Acción"}},
    "plantavszombie": {"titulo": "Plantas vs Zombies", "anio": 2009, "genero": {"Estrategia"}},
    "stardew": {"titulo": "Stardew Valley", "anio": 2016, "genero": {"Rol"}},
}
# ===== CRUD ====== #
# - -- Create -- - #
# Como un constructor

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


## Pruebas
total_juegos()
cont_por_genero()