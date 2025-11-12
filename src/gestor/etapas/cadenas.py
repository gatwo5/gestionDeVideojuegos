from tuplas import videojuegos    # Importa la lista de tuplas (título, año, género)
from listas import lista          # Importa la lista simple de videojuegos

# Función para limpiar el texto
def limpiar(texto):
    return texto.strip().lower()

nombre = input("Escribe el nombre de un videojuego: ")# Pide al usuario el nombre del videojuego
busqueda = limpiar(nombre)  # Normaliza el texto introducido
encontrado = None  # Variable para guardar el resultado de la búsqueda

# Recorre la lista de tuplas y busca coincidencias
for titulo, anio, genero in videojuegos:
    if limpiar(titulo) == busqueda:  # Compara el título
        encontrado = (titulo, anio, genero)  # Guarda el videojuego encontrado


if encontrado:# Si lo encuentra, muestra la información
    titulo, anio, genero = encontrado
    print(f"Título: {titulo} | Género: {genero} | Año: {anio}")
else:  # Si no existe
    print("No se encontró ese videojuego en la lista.")

