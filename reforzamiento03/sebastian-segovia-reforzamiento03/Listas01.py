"""Escribir un programa donde ingresarás el tamaño de la lista mediante consola,
este tamaño servirá para ingresar una cantidad X de nombres de alumnos.
Ingresarás los nombres mediante consola también.
Se quiere mostrar finalmente el tamaño de la lista y todos los nombres de la
lista que fueron ingresados."""

nombres = []
cantidad = int(input("Ingresa una cantidad de alumnos desde 1 a 10: "))

if cantidad > 0:
    nombre1 = input("Agrega el nombre del alumno 1: ")
    nombres.append(nombre1)
if cantidad > 1:
    nombre2 = input("Agrega el nombre del alumno 2: ")
    nombres.append(nombre2)
if cantidad > 2:
    nombre3 = input("Agrega el nombre del alumno 3: ")
    nombres.append(nombre3)
if cantidad > 3:
    nombre4 = input("Agrega el nombre del alumno 4: ")
    nombres.append(nombre4)
if cantidad > 4:
    nombre5 = input("Agrega el nombre del alumno 5: ")
    nombres.append(nombre5)
if cantidad > 5:
    nombre6 = input("Agrega el nombre del alumno 6: ")
    nombres.append(nombre6)
if cantidad > 6:
    nombre7 = input("Agrega el nombre del alumno 7: ")
    nombres.append(nombre7)
if cantidad > 7:
    nombre8 = input("Agrega el nombre del alumno 8: ")
    nombres.append(nombre8)
if cantidad > 8:
    nombre9 = input("Agrega el nombre del alumno 9: ")
    nombres.append(nombre9)
if cantidad > 9:
    nombre10 = input("Agrega el nombre del alumno 10: ")
    nombres.append(nombre10)

print("Los alumnos son: {}".format(nombres))
print("El tamaño de la lista es de: {}".format(len(nombres)))


