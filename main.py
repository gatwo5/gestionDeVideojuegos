from src.gestor import busquedas, catalogo, estadisticas, utils_texto

eleccion = 0
while eleccion < 1 or eleccion > 6:
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
                    titulo = input("Introduce el titulo")
                case 2:
                    pass
                case 3:
                    pass
                case 4:
                    pass
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
        case _:
            print("Introduce una opción válida")

    eleccion = int(input("Desea contiunar? 0: Si | 1: No: "))