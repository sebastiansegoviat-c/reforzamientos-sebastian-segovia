"""
Tiene una lista de invitados que llegaron a una boda de acuerdo a su orden
de llegada:
guests = [“Ana”, “Katherine”, “Pedro”, “Luis”, “Raúl”, “Fiorella”, “Miguel”]
Se requiere reorganizar esta lista.
Primero los que tienen número impar y en el orden que fueron llegando
Segundo las personas que tienen número par de letras
Input: [“Ana”, “Pedro”, “Raúl”, “Fiorella”, “Katherine”, “Miguel”, “Luis”]
Output: [“Ana”, “Pedro”, ”Katherine”, “Raúl”, “Fiorella”, “Miguel”, “Luis”]
"""
from itertools import pairwise

lista1 = []
lista1.extend(["Ana", "Katherine", "Pedro", "Luis", "Raúl", "Fiorella", "Miguel"])
lista2 = lista1.copy()

lista1[0] = "Katherine"
lista1[1] = "Luis"
lista1[2] = "Fiorella"
lista1[3] = "Ana"
lista1[4] = "Pedro"
lista1[5] = "Raúl"

lista2[1] = "Pedro"
lista2[2] = "Raúl"
lista2[3] = "Miguel"
lista2[4] = "Katherine"
lista2[5] = "Luis"
lista2[6] = "Fiorella"

print("La lista actualizada es: {}".format(lista1))
print("La lista actualizada es: {}".format(lista2))
