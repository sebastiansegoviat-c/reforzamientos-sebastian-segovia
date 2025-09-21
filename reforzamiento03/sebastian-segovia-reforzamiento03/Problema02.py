#Crea un programa que calcule el Índice de Masa Corporal (IMC) de una persona.
#En el mensaje también indicar el nombre de la persona indicando su IMC también

while True:
    try:
        nombre = str(input("Ingresa tu nombre: "))
        peso = float(input("Ingresa tu peso en kilogramos: "))
        altura = float(input("Ingresa tu altura en metros: "))

        imc = peso / (altura * altura)
        print("{}, tu IMC es de: {}".format(nombre, f"{imc:.1f}"))
    except ValueError:
        print("El valor ingresado no es un numero")
