"""
Crear un diccionario con 6 departamentos del país.
- Borrar cualquier departamento, usando la palabra reservada del.
- Actualizar el penúltimo departamento por otro.

- Comprobar que no existe este departamento borrado dentro del
diccionario.
"""

departamentos = {'dep1': 'Ancash', 'dep2': "Lima", 'dep3': 'Junin', 'dep4': 'Cajamarca', 'dep5': 'Ayacucho', 'dep6': 'Huancavelica'}
print("La lista contiene los siguientes departamentos: {}".format(list(departamentos.values())))

eliminar = input('Eliminar departamento por su clave: ')

if eliminar in departamentos:
    del departamentos[eliminar]
    print("La lista actualizada es: {}".format(departamentos))
else:
    print("Ese departamento no existe en la lista")

