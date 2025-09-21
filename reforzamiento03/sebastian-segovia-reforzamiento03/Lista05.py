"""
Ingresar por consola el tamaño de una lista, luego empezarás a ingresar los
datos mediante consola también (5 compañías relacionadas con al mundo de TI)
y harás una copia donde adrede agregarás nombres que estarán repetidos
(mediante consola) para que finalmente muestres otra lista donde
solo se mostrará los nombres no repetidos y también te mostrará la lista inicial
"""

lista1 = []
cantidad = int(input("Ingrese la cantidad de datos: "))

if cantidad > 0:
    var1 = input("Agregue el nombre de una empresa relacionada al mundo de TI: ")
    lista1.append(var1)
if cantidad > 1:
    var2 = input("Aguegue el nombre de otra empresa relacionada al mundo de TI: ")
    lista1.append(var2)
if cantidad > 2:
    var3 = input("Aguegue el nombre de otra empresa relacionada al mundo de TI: ")
    lista1.append(var3)
if cantidad > 3:
    var3 = input("Aguegue el nombre de otra empresa relacionada al mundo de TI: ")
    lista1.append(var3)
if cantidad > 4:
    var4 = input("Aguegue el nombre de otra empresa relacionada al mundo de TI: ")
    lista1.append(var4)
print("Los valores de la lista son: {}".format(lista1))

lista2 = list.copy(lista1)
var5 = input("Aguegue el nombre de otra empresa relacionada al mundo de TI: ")
lista2.append(var5)

var6 = input("Aguegue el nombre de otra empresa relacionada al mundo de TI: ")
lista2.append(var6)

var7 = input("Aguegue el nombre de otra empresa relacionada al mundo de TI: ")
lista2.append(var7)

var8 = input("Aguegue el nombre de otra empresa relacionada al mundo de TI: ")
lista2.append(var8)

var9 = input("Aguegue el nombre de otra empresa relacionada al mundo de TI: ")
lista2.append(var9)

lista3 = set(lista2)
print("Los valores de la primera lista son: {}".format(lista1))
print("Los valores de la segunda lista son: {}".format(lista3))