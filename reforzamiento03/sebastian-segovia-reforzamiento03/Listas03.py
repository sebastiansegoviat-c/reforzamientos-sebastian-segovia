"""
Crea una lista vacía, luego ingresa sus valores (10 valores numéricos) y
finalmente muestra la suma y la media de los números ingresado insertados en
la terminal
"""

lista1 = []
num1 = int(input("Ingresa un numero: "))
lista1.append(num1)
num2 = int(input("Ingresa un numero: "))
lista1.append(num2)
num3 = int(input("Ingresa un numero: "))
lista1.append(num3)
num4 = int(input("Ingresa un numero: "))
lista1.append(num4)
num5 = int(input("Ingresa un numero: "))
lista1.append(num5)
num6 = int(input("Ingresa un numero: "))
lista1.append(num6)
num7 = int(input("Ingresa un numero: "))
lista1.append(num7)
num8 = int(input("Ingresa un numero: "))
lista1.append(num8)
num9 = int(input("Ingresa un numero: "))
lista1.append(num9)
num10 = int(input("Ingresa un numero: "))
lista1.append(num10)

suma = num1 + num2 + num3 + num4 + num5 + num6 + num7 + num8 + num9 + num10
print("La suma de los valores es: {}".format(suma))
media = suma / len(lista1)
print("La media de los valores es: {}".format(f"{media:.2f}"))