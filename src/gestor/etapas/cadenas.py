from etapas.tuplas import videojuegos  # Importamos la listas y tuplas

# Función para limpiar el texto introducido
def limpiar(texto):
    return texto.strip().lower()

nombre = input("Escribe el nombre de un videojuego: ")  # Pide al usuario un nombre
busqueda = limpiar(nombre)  # Normaliza el texto ingresado

encontrado = None

for titulo, anio, genero in videojuegos:# Recorre la lista de videojuegos
    if limpiar(titulo) == busqueda:  # Compara el título normalizado con la búsqueda
        encontrado = (titulo, anio, genero) 

# Después del bucle, compruebo si encontro algo
if encontrado:
    titulo, anio, genero = encontrado
    print(f"Título: {titulo} | Género: {genero} | Año: {anio}")  # Muestra el videojuego
else:
    print("No se encontró ese videojuego en la lista.")  # Mensaje si no existe
