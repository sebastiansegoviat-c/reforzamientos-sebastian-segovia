#Escribe un programa que reciba dos flotantes, luego estos pasarán a ser convertidos
#en enteros. Indique si el primero es múltiplo del segundo. Usar mod para la verificación
#si el residuo es 0

while True:
    try:
        num1 = float(input("Ingresa un numero: "))
        num2 = float(input("Ingresa otro numero: "))

        num_int1 = int(num1)
        num_int2 = int(num2)

        if num_int1 % num_int2 == 0:
            print("{} es multiplo de {}".format(num_int1, num_int2))
        else:
            print("{} no es multiplo de {}".format(num_int1, num_int2))
    except ValueError:
        print("El valor ingresado no es un numero")
