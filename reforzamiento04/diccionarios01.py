"""
Crea correctamente un diccionario con los campos de: nombre, edad, salario
y edad.
Convierte tu diccionario finalmente a una lista y muestra el resultado en la
terminal.
"""

datos = {'nombre': 'Sebastian', 'edad': 19, 'salario': 2000}
datos_lista = list(datos.values())
print("Los datos son: Nombre: {}, Edad: {} años, Salario: {} soles".format(datos_lista[0], datos_lista[1], datos_lista[2]))

