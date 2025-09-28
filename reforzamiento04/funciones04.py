"""
Pedir al usuario que ingrese un nombre y apellidos el cual será usada
por un parámetro para una función que se creará e indicará cuantas letras
tiene el nombre solamente. Usar la función un mínimo de dos veces para dos
personas e indicar quien tiene el nombre con mayor número de caracteres
(condicional)
"""

nombre_1 = input("Ingresa tu nombre: ")
nombre_2 = input("Ingresa otro nombre: ")

def sumatoria_1(nombre_1):
    contador_1 = 0
    for letras in range(len(nombre_1)):
        if nombre_1[letras] != " ":
            contador_1 = contador_1 + 1
    return(contador_1)

def sumatoria_2(nombre_2):
    contador_2 = 0
    for letras in range(len(nombre_2)):
        if nombre_2[letras] != " ":
            contador_2 = contador_2 + 1
    return(contador_2)

resultado_1 = sumatoria_1(nombre_1)
resultado_2 = sumatoria_2(nombre_2)

if resultado_1 > resultado_2:
    print(f"{nombre_1} tiene una mayor cantidad de letras con: {resultado_1} letras")
elif resultado_1 < resultado_2:
    print(f"{nombre_2} tiene una mayor cantidad de letras con: {resultado_2} letras")
else:
    print("Los dos nombres tienen igual cantidad de letras")




