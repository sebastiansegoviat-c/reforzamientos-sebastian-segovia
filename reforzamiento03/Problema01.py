#Escribe un programa que convierta cierta cantidad de soles a
#dólares, usando un tipo de cambio que se proporciona en el
#programa.
#Estos valores estarán dentro de sus variables respectivamente.
#La salida mostrará tres cambios que hagas respectivamente de
#tres montos a convertir.

while True:
    try:
        soles1 = int(input("Introduzca una primera cantidad en soles: "))
        soles2 = int(input("Introduzca una segunda cantidad en soles: "))
        soles3 = int(input("Introduzca una tercera cantidad en soles: "))
        dolares1 = soles1 * 0.29
        dolares2 = soles2 * 0.29
        dolares3 = soles3 * 0.29
        print("La primera cantidad de soles en dolares es de: ${}".format(f"{dolares1:.2f}"))
        print("La segunda cantidad de soles en dolares es de: ${}".format(f"{dolares2:.2f}"))
        print("La tercera cantidad de soles en dolares es de: ${}".format(f"{dolares3:.2f}"))

    except ValueError:
        print("El valor ingresado no es un numero")
