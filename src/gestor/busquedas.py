catalogo = {
    "zelda": {"titulo": "The Legend of Zelda", "anio": 1986, "genero": {"Acción"} },
    "mario": {"titulo": "Super Mario Odyssey", "anio": 2017, "genero": {"Acción"} },
    "plantavszombie": {"titulo": "Plantas vs Zombies", "anio": 2009, "genero": {"Estrategia"} },
    "stardew": {"titulo": "Stardew Valley", "anio": 2016, "genero": {"Rol"} },
}
# Exacta por título [devuelve 1 videojuego exacto]
def buscar_por_titulo(titulo):
    # Crear lista vacía para guardar resultados
    result = None

    # Recorrer todo el catalogo y devuelve el dicho videojuego con todos los datos (por eso .value)
    for x in catalogo.values(): # catalogo.value() devuelve una lista de todos los valores (diccionarios internos)
        if x["titulo"].lower() == titulo.lower():
            result = x
    
    print(result)

# Parcial (contenga un fragmento en el título) [Devuelve varios]
def buscar_parcial(trozo):
    result = []

    for x in catalogo.values():
        # Obtener título
        titulo = x["titulo"]

        # Comprobar si trozo está dentro del título
        if trozo.lower() in titulo.lower():
            # Si coincide, lo añadimos a la lista de resultados
            result.append(x)

    # Si lista result NO está vacía
    if result:
      print("Videojuego encontrado: ")
      for x in result:
       print(x["titulo"], x["anio"], x["genero"])
    else:
      print("No encontrado")

    # Devuelve lista de juegos con coincidencias
    print(result)

# Por género o rango de años [Devuelve varios]
def buscar_por_genero(genero_buscar):
    result = []
    for x in catalogo.values():
        # genero = x["genero"] -> Al ser por ejemplo {"Acción"}, entonces no es una cadena, no posible usar esto
        for genero in x["genero"]:
            if genero.lower() == genero_buscar.lower():
                result.append(x)

    print(result)

def buscar_por_rango_anios(min, max):
    result = []
    for x in catalogo.values():
        anio = x["anio"]
        if min <= anio <= max:
            result.append(x)

    print(result)
