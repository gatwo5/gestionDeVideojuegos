def gestionar_conjuntos():
    print("\n=== ETAPA 4: CONJUNTOS ===")

    generos = {"Acción", "Aventura", "Rol", "Estrategia", "Deportes"}
    print("Géneros iniciales:", generos)

    generos.add("Simulación")
    generos.discard("Estrategia")
    print("Después de cambios:", generos)

    favorito = input("\n¿Cuál es tu género favorito? ").strip().capitalize()
    if favorito in generos:
        print(f"Sí, tienes juegos del género '{favorito}'.")
    else:
        print(f"No tienes juegos del género '{favorito}'.")

    amigo = {"Acción", "Plataformas", "Rol"}
    print("\nGéneros de tu amigo:", amigo)

    print("\nUnión:", generos | amigo)
    print("Intersección:", generos & amigo)
    print("Diferencia (tus géneros que él no tiene):", generos - amigo)


if __name__ == "__main__":
    gestionar_conjuntos()
