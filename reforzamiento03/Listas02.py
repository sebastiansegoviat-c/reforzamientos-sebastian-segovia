"""Crear un programa en Python donde tendrás una lista con 6 departamentos,
el programa te pedirá ingresar 2 departamentos el cual el segundo
departamento que ingreses sustituirá al primero de la lista."""

listad = []
listad.extend(["Tacna", "Ancash", "Lima", "Arequipa", "San Martín", "Junin"])
print("La lista de departamentos contiene a: {}".format(listad))

dep1 = str(input("Agrega un primer departamento: "))
dep2 = str(input("Agrega un segundo departamento: "))

listad[0] = dep2
listad.append(dep1)

print("La lista actualizada contiene a: {}".format(listad))