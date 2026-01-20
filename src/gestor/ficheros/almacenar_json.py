from src.gestor.catalogo import catalogo
from os import strerror
import json


def guardar_catalogo_json(nombre_fichero):
    try:
        with open(f"src/gestor/ficheros/escribir_ficheros/{nombre_fichero}.json", "w", encoding="utf-8") as fichero:
            json.dump(catalogo, fichero, ensure_ascii=False, indent=4)

        print("Archivo JSON generado correctamente.")

    except IOError as e:
        print("Error durante la operacion de archivos: ", strerror(e.errno))
        exit(e.errno)