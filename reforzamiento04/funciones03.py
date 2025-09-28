"""
Crear una función que sume los dígitos del número ingresado y muestre
por consola la suma de todos estos dígitos.
"""
while True:
    try:
        numero = int(input("Ingrese un número: "))
        break
    except ValueError:
        print("Introduzca valores aceptable")


def sumatoria(numero):

    suma = 0
    num_str = str(numero)
    for digito in num_str:
        suma = suma + int(digito)
    return suma

resultado = sumatoria(numero)
print("El resultado es: ", resultado)