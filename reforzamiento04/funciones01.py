"""
Pedir dos números positivos mediante terminal al usuario. Mostrar
como salida el número cuya sumatoria de dígitos es el mayor y los números
cuya sumatoria de dígitos es menor que 10. Utilizar una o más funciones, según
sea conveniente.
"""

while True:
    num_1 = int(input("Ingresa un numero: "))
    num_2 = int(input("Ingresa otro numero: "))
    if num_1 > 0 and num_2 > 0:
        break
    else:
        print("No se puede ingresar un numero negativo.")

def sumatoria_1(num_1):
    sumatoria_1 = 0
    num_str_1 = str(num_1)

    for digito in num_str_1:
        sumatoria_1 = sumatoria_1 + int(digito)
    return sumatoria_1

def sumatoria_2(num_2):
    sumatoria_2 = 0
    num_str_2 = str(num_2)

    for digito in num_str_2:
        sumatoria_2 = sumatoria_2 + int(digito)
    return sumatoria_2

suma_1 = sumatoria_1(num_1)
suma_2 = sumatoria_2(num_2)

if suma_1 > suma_2:
    print(f"El número {num_1} tiene una suma de digitos de {suma_1}")
elif suma_2 > suma_1:
    print(f"El número {num_2} tiene una suma de digitos de {suma_2}")
else:
    print("Los números tienen igual sumatoria de digitos")

if suma_1 > 10:
    print(f"El número {num_1} tiene una suma de digitos mayor de 10")
if suma_2 > 10:
    print(f"El número {num_2} tiene una suma de digitos mayor de 10")
if suma_2 <= 10 and suma_1 <= 10:
    print(f"Tanto la sumatoria de digitos de {num_1} como de {num_2} es menor a 10")
