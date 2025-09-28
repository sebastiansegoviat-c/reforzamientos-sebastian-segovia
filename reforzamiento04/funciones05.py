"""
Crear una función que aceptará por parámetro dos valores que serán
ingresados por el usuario, una lista donde los valores serán llenados por el
usuario también y un segundo parámetro que eliminará de la lista que fue
ingresada a la función, finalmente el output de la función será la lista
actualizada sin el valor que se sacará de la lista. Mostrar también la lista
original y el número que fue eliminado.
"""

lista_1 = []
valor_1 = int(input("Ingrese un valor numérico: "))
valor_2 = int(input("Ingrese otro valor: "))
valor_3 = int(input("Ingrese otro valor: "))
valor_4 = int(input("Ingrese otro valor: "))
valor_5 = int(input("Ingrese otro valor: "))

lista_1.extend([valor_1, valor_2, valor_3, valor_4, valor_5])
lista_2 = lista_1.copy()

del_element = int(input("Ingrese un elemento numérico que quiera eliminar: "))

def lista(lista_1, del_element):
    for elemento in lista_1:
        if elemento == del_element:
            lista_1.remove(elemento)
    return lista_1

resultado = lista(lista_1, del_element)

print(f"La lista original es: {lista_2}")
print(f"La lista actualizada es: {resultado}")

