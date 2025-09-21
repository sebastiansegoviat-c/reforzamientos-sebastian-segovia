"""Tienes una lista con 5 nombres de estudiantes. Crear un programa que te
pedirá ingresar el nombre de un estudiante, la cuál será eliminada de lista
inicial en caso que no exista en la lista mostrar un mensaje donde indique
que no se encuentre en la lista y luego esta será agregada a la lista.
Finalmente mostrar la lista actualizada en consola."""

lista1 = []
lista1.extend(["José", "María", "Daniel", "Luz", "Carlos"])
print("La lista de estudiantes es: {}".format(lista1))

est = str(input("Ingrese el nombre del estudiante que quiere agregar: "))
if est in lista1:
    lista1.remove(est)
    print("La lista actualizada es: {}".format(lista1))
else:
    lista1.append(est)
    print("El estudiante no se encuentra en la lista. Será agregado.")
    print("La lista actualizada es: {}".format(lista1))
