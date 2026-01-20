from src.gestor import busquedas, catalogo, estadisticas, utils_texto
from src.gestor.ficheros import almacenar_csv, almacenar_json, leer_csv, leer_json

eleccion = 0
while eleccion < 1 or eleccion > 7:
    utils_texto.imprimir_menu()
    eleccion = int(input())
    match (eleccion):
        case 1:
            eleccion = int(input("1: Total de juegos\n2:Total por genero"))
            match (eleccion):
                case 1:
                    estadisticas.total_juegos()
                case 2:
                    estadisticas.cont_por_genero()
        case 2:
            clave = input("Introduce la clave del juego a buscar: ")
            catalogo.leer(clave)
        case 3:
            eleccion = int(
                input(
                    "1: Buscar por titulo\n2:Buscar por titulo parcial\n3:Buscar por genero\n4:Buscar por rango de años"
                )
            )
            match (eleccion):
                case 1:
                    titulo = input("Introduce el titulo: ")
                    busquedas.buscar_por_titulo(titulo)

                case 2:
                    trozo = input("Introduce un fragmento del titulo: ")
                    busquedas.buscar_parcial(trozo)

                case 3:
                    genero = input("Introduce el genero: ")
                    busquedas.buscar_por_genero(genero)

                case 4:
                    minimo = int(input("Introduce el año mínimo: "))
                    maximo = int(input("Introduce el año máximo: "))
                    if minimo > maximo:
                        minimo, maximo = maximo, minimo
                    busquedas.buscar_por_rango_anios(minimo, maximo)

                case _:
                    print("Opción de búsqueda no válida.")
        case 4:
            clave = input("Introduce la clave: ")
            titulo = input("Introduce el titulo: ")
            anio = int(input("Introduce el año: "))
            genero = input("Introduce el genero: ")
            catalogo.crear(clave, titulo, anio, genero)
        case 5:
            clave = input("Introduce la clave del juego a actualizar: ")
            titulo = input("Introduce el titulo: ")
            anio = int(input("Introduce el año: "))
            genero = input("Introduce el genero: ")
            catalogo.actualizar(clave, titulo, anio, genero)
        case 6:
            clave = input("Introduce la clave del juego a eliminar")
            catalogo.eliminar(clave)
        case 7:
            nombre_fichero = input("Introduce el nombre del fichero: ")
            eleccion = int(
                input(
                    "1: Almacenar en CSV\n2:Leer desde CSV\n3:Almacenar en JSON\n4:Leer desde JSON "
                ))
            
            match(eleccion):
                case 1:
                    almacenar_csv.guardar_catalogo_csv(nombre_fichero)
                case 2:
                    leer_csv.leer_catalogo_csv(nombre_fichero)
                case 3:
                    almacenar_json.guardar_catalogo_json(nombre_fichero)
                case 4:
                    leer_json.leer_catalogo_json(nombre_fichero)
        case _:
            print("Introduce una opción válida")

    eleccion = int(input("Desea contiunar? 0: Si | 1: No: "))