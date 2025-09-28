"""
Agrega un nuevo key llamado “dni” con su respectivo valor y luego mostrar
el valor del salario y DNI en consola. También elimina el key edad de tu
diccionario, incluyendo su valor. Mostrar finalmente el diccionario
actualizado.
"""

datos = {'nombre': 'Sebastian', 'edad': 19, 'salario': 2000}
datos['dni'] = 60572565
del datos['edad']
print("Datos mostrados: {} como su número de DNI y {} soles como su salario".format(datos['dni'], datos['salario']))

print("La lista actualizada es:")
print("Nombre: {} \nDNI: {} \nsalario: {} soles".format(datos['nombre'], datos['dni'], datos['salario']))