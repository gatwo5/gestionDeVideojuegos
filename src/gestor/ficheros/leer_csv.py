import csv
from src.gestor.catalogo import catalogo
from os import strerror
import ast  


def leer_catalogo_csv(nombre_fichero):
    try:
        with open(
            f"src/gestor/ficheros/leer_ficheros/{nombre_fichero}.csv",
            "r",
            encoding="utf-8"
        ) as fichero:
            reader = csv.DictReader(fichero, delimiter="|")

            catalogo.clear()

            for fila in reader:
                clave = fila["titulo"].strip().lower()

                catalogo[clave] = {
                    "titulo": fila["titulo"].strip(),
                    "anio": int(fila["anio"]),
                    "genero": ast.literal_eval(fila["genero"])  
                }

            print("Archivo leído correctamente.")

    except IOError as e:
        print("Error durante la operacion de archivos: ", strerror(e.errno))
        exit(e.errno)
