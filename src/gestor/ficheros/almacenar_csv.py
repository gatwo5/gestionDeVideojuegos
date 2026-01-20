from src.gestor.catalogo import catalogo
from os import strerror
import csv

def guardar_catalogo_csv(nombre_fichero):
    cabeceras = ["titulo", "anio", "genero"]

    try:
        with open(f"src/gestor/ficheros/escribir_ficheros/{nombre_fichero}.csv", "w") as fichero:
            writer = csv.DictWriter(fichero, fieldnames=cabeceras, delimiter="|")
            writer.writeheader()
            writer.writerows(catalogo)
            print("Archivo generado correctamente.")
    except IOError as e:
        print("Error durante la operacion de archivos: ", strerror(e.errno))
        exit(e.errno)