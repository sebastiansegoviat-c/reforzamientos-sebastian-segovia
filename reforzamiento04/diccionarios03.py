"""
Convertir tu diccionario a una lista y mostrar en consola el tipo de datos
final que tienes.
"""

datos = {'nombre': 'Sebastian', 'edad': 19, 'salario': 2000}
datos['dni'] = 60572565
del datos['edad']

datos_lista = list(datos.values())
print("El tipo de datos son para: Nombre: {}, Salario: {} y DNI: {}".format(type(datos_lista[0]), type(datos_lista[1]), type(datos_lista[2])))