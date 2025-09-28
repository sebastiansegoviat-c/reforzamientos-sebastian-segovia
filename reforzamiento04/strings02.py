"""
Crear un programa que cuente cuántas veces aparece cada vocal en la
oración. Ignorar mayúsculas/minúsculas
Input: “Programación en Python”
Output:
a: 2
e: 1
i: 1
o: 2
u: 0
Métodos útiles: lower() y count()
"""

frase = input("Ingresa una frase: ")

lista = frase.lower()

print("La vocal 'a' aparece: {} veces".format(lista.count('a')))
print("La vocal 'e' aparece: {} veces".format(lista.count('e')))
print("La vocal 'i' aparece: {} veces".format(lista.count('i')))
print("La vocal 'o' aparece: {} veces".format(lista.count('o')))
print("La vocal 'u' aparece: {} veces".format(lista.count('u')))
