"""
Ingresar el nombre de tu carrera dentro de los valores que tienes en tu
diccionario.
- Mostrar en consola los valores de tu carrera y nombre agregándolos a
una variable c/u
"""

datos = {'nombre': 'Sebastian', 'edad': 19, 'salario': 2000}
datos['carrera'] = "Farmacia y Bioquímica"

nombre = datos['nombre']
carrera = datos['carrera']
print("Tu nombre es {} y tu carrera profesional es {}".format(nombre, carrera))