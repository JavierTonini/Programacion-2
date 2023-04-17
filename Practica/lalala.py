
"""
Armar una lista que contenga el primer y el último elemento de la siguiente lista
Restricción: Utilizar el método append junto al indexado simple
"""

lista = ["ho", 3.1416, 42, 81, 6, "la"]

# COMPLETAR - INICIO
lista_primero_y_ultimo = []
lista_primero_y_ultimo.append(lista[0])
lista_primero_y_ultimo.append(lista[len(lista)-1])
print (lista_primero_y_ultimo)
# COMPLETAR - FIN

assert lista_primero_y_ultimo == ["ho", "la"]