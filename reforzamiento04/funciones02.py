"""
Crea una función que al ingresar dos números por parámetro mostrará
todos los cuadrados de los números que hay entre ellos (Usar la función una
vez y mostrar el resultado por consola). Los números serán ingresados y
solicitados al usuario.
"""
while True:
    num_1 = int(input("Ingrese un número: "))
    num_2 = int(input("Ingrese un número mayor: "))
    if num_1 < num_2:
        inicio = num_1
        final = num_2
        break
    else:
        print("Ingrese valores validos")


def cuadrados(inicio, final):

    for numeros in range(inicio + 1, final):
        print(f"El cuadrado de {numeros} es: {numeros ** 2}")

    return cuadrados

resultado = cuadrados(inicio, final)

