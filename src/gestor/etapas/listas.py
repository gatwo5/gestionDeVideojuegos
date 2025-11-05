lista = ["God of War", "Super Mario", "Free fire", "Call of duty", "Fortnite"]
print("lista inicial: ",lista)

lista.append("Nuevo_videoJuego")#añade al final de lista
print("despues de añadir al final de la lista: ",lista)

lista.insert(2, "Doom")#añade en la posición 2
print("añadido Doom en posicion 2: ",lista)

lista.remove("Call of duty")#borra Call of duty, si existe. sino existe va dar error
print("borrado call of duty: ", lista)

print("muestra la lista alfabeticamente: ")
lista.sort()# ordena la lista por orden alfabético
print(lista)