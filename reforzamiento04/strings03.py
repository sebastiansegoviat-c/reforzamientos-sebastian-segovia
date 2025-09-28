"""
Pide al usuario que ingrese una frase y una palabra, obtén si la palabra está
dentro de la oración sin importar si está en mayúsculas o minúsculas.
En caso que aparezca, indica la posición del primer carácter en donde
empieza
Input: frase = “Python y sus enormes ventajas”, palabra = “Python”
Output: “Python aparece en la posición 0”
Métodos útiles: lower() y find()
"""

var1 = input("Ingresa una frase: ")
var2 = input("Ingresa una palabra: ")

frase = var1.lower()
palabra = var2.lower()
posición = frase.find(palabra)

if palabra in frase:
    print("'{}' aparece en la posición {}".format(palabra, posición))








