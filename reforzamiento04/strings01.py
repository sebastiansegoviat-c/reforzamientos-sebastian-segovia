"""
Dada una frase u oración encontrar que palabra es la que tiene más
caracteres y cuántos caracteres tiene
Input: “La programación en Python es poderosa”
Output: “programación” – 12 caracteres
"""

frase = input("Ingresa una frase: ")

palabras = frase.split()

palabra_larga = palabras[0]
for palabra in palabras:
    if len(palabra) > len(palabra_larga):
        palabra_larga = palabra

print("La palabra más larga es: {} con {} caracteres".format(palabra_larga, len(palabra_larga)))