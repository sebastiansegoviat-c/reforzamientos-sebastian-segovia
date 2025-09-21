#Crea un programa que tome un número decimal (con 6 número en la parte decimal)
# e imprima ese número con: 1 decimal, 2 decimales y 4 decimales

num = float(input("Ingresa un numero con 6 decimales: "))

print("El número con 1 decimal es: {}".format(f"{num:.1f}"))
print("El número con 2 decimales es: {}".format(f"{num:.2f}"))
print("El número con 4 decimales es: {}".format(f"{num:.4f}"))