from tuplas import videojuegos

nom = input(print("introduce el nombre de un videojuego"))

# Normalizamos el texto (quitamos espacios y pasamos a minúsculas)
nombre = nom.strip().lower()
# Variable para saber si se encontró
encontrado = False

# Recorremos la lista de tuplas
for titulo, genero, anio in videojuegos:
    # Normalizamos también el título de la lista
    if titulo.lower() == nombre:
        print(f"Título: {titulo} | Género: {genero} | Año: {anio}")
        encontrado = True
        break

# Si no se encontró
if not encontrado:
    print("El videojuego no se encuentra en la lista.")