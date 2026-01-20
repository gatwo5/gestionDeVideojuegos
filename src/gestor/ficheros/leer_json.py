from src.gestor.catalogo import catalogo
from os import strerror
import json

def leer_catalogo_json(nombre_fichero):
    try:
        with open(f"src/gestor/ficheros/leer_ficheros/{nombre_fichero}.json", "r") as fichero:
            datos = json.load(fichero) # Convierte json en una lista de diccionarios

            # Recorrer todos los videojuegos del catálogo
            for fila in datos:
                catalogo.append({ # Añadir al catálogo cada uno
                    "titulo": fila["titulo"],
                    "anio": int(fila["anio"]),
                    "genero": fila["genero"]
                })

            print("Archivo leído correctamente.")
    except IOError as e:
        print("Error durante la operación de archivo: ", strerror(e.errno))
        exit(e.errno)