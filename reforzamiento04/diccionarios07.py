"""
Realizar un programa donde se ingresarán por consola los nombres de los
alumnos (indicar previamente la cantidad de alumnos a ingresar) de un curso y
las notas de c/u. Guardarás la información en un diccionario donde las claves
serán los nombres de c/u de estos alumnos y sus valores serán las notas de
esto alumnos.
Finalmente mostrarás los alumnos con sus notas en un mensaje similar a
“Pedro tiene la nota de 15” y también la media de todas las notas.
"""

print("A continuación ingresaras el nombre de 5 alumnos")
datos = {}

alumno1 = input("Ingrese el nombre del alumno 1: ")
nota1 = int(input("Ingrese el nota del alumno 1: "))
datos[alumno1] = nota1

alumno2 = input("Ingrese el nombre del alumno 2: ")
nota2 = int(input("Ingrese el nota del alumno 2: "))
datos[alumno2] = nota2

alumno3 = input("Ingrese el nombre del alumno 3: ")
nota3 = int(input("Ingrese el nota del alumno 3: "))
datos[alumno3] = nota3

alumno4 = input("Ingrese el nombre del alumno 4: ")
nota4 = int(input("Ingrese el nota del alumno 4:"))
datos[alumno4] = nota4

alumno5 = input("Ingrese el nombre del alumno 5: ")
nota5 = int(input("Ingrese el nota del alumno 5: "))
datos[alumno5] = nota5

print("_________________________________________________________")
print("Las notas son las siguientes:")
for nombres, notas in datos.items():
    print(nombres, "=", notas)

print("_________________________________________________________")
media = sum(datos.values()) / len(datos.keys())
print("El media es: ", media)

