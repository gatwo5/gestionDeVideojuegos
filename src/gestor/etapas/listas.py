lista = ["God of War", "Super Mario", "Free fire", "Call of duty", "Fortnite"]
print("Lista inicial: ")
print(lista)
print()

lista.append("Nuevo_videoJuego")  # añade al final de lista
print("Después de añadir al final de la lista: ")
print(lista)
print()

lista.insert(2, "Doom")  # añade en la posición 2
print("Añadir Doom en posicion 2: ")
print(lista)
print()

lista.remove("Call of duty")  # borra Call of duty, si existe. sino existe va dar error
print("Borrar Call of duty: ")
print(lista)
print()

print("Mostrar la lista alfabeticamente: ")
lista.sort()  # ordena la lista por orden alfabético
print(lista)