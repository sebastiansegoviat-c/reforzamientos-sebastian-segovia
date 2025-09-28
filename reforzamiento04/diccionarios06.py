"""
Ingresar por consola 4 números mediante consola, crear un diccionario
donde los ‘key’ serán los números indicados y los valores serán los cubos de
las estos keys. Mostrar finalmente este diccionario.
"""

num_1 = int(input("Ingresar un numero: "))
num_2 = int(input("Ingresar otro numero: "))
num_3 = int(input("Ingresar otro numero: "))
num_4 = int(input("Ingresar otro numero: "))

diccionario = {}
diccionario[num_1] = num_1 ** 3
diccionario[num_2] = num_2 ** 3
diccionario[num_3] = num_3 ** 3
diccionario[num_4] = num_4 ** 3

print("Los valores de tu diccionario son: {}, {}, {} y {}".format(diccionario[num_1], diccionario[num_2], diccionario[num_3], diccionario[num_4]))