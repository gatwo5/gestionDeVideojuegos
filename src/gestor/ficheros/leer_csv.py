import csv
from src.gestor.catalogo import catalogo
from os import strerror


def leer_catalogo_csv(nombre_fichero):
    try:
        with open(f"src/gestor/ficheros/leer_ficheros/{nombre_fichero}.csv", "r") as fichero:
            reader = csv.DictReader(fichero, delimiter="|")

            catalogo.clear()  # vaciamos el catálogo antes de cargar

            for fila in reader:
                catalogo.append({
                    "titulo": fila["titulo"],
                    "anio": int(fila["anio"]),
                    "genero": fila["genero"]
                })

            print("Archivo leído correctamente")

    except IOError as e:
        print("Error durante la operacion de archivos:", strerror(e.errno))
        exit(e.errno)

