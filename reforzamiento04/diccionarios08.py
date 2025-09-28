"""
Crear una agenda basada en un diccionario donde los key serán los nombres
de las personas y sus “values” serán los números de teléfono de c/u.
Ingresarás por consola el nombre y el número de cada persona que serán
registrados en la agenda.
El programa también te permitirá buscar por nombre en el diccionario en caso
no exista mostrar un mensaje de “No se encuentra registrado en la agenda”
"""

agenda = {}

for val in range(0, 5):
    nombre = input(f"Ingresar nombre {val+1}: ")
    telefono = input(f"Ingresar el telefono {val+1}: ")
    agenda[nombre] = telefono

print("La agenda es ha sido actualizada")
print("________________________________________________________________________")

while True:
    value = input("Ingresar el nombre para obtener su número: ")
    if value not in agenda:
        print("El nombre no existe")
    else:
        print("El número es: ", agenda[value])
        break