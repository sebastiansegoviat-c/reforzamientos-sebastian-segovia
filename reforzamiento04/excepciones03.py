"""
Crear una función funciona_indice(persona, indice) y dentro la respectiva
excepción para el siguiente bloque de código para que tu programa no se
bloquee y además imprime un mensaje al usuario: “El índice “nombre_indice”
ingresado no existe en el diccionario”, tipo de datos, etc que más pueden
incurrir para este caso (los datos se pedirán por consola):

persona= {'nombre':'Xavier', 'apellido':'Rodriguez', 'dni':'63325345'}
persona['profesion'] #El índice en este caso no existe

Usar la función al menos 2 veces incluyendo un caso de error
"""

datos = {}

def funcion_indice(persona, indice):
    if persona in datos:
        datos[persona] = nuevo_valor
        return True
    else:
        return False

while True:
    try:
        datos['nombre'] = input('Ingresa tu nombre: ')
        datos['apellido'] = input('Ingresa tu apellido: ')
        datos['dni'] = int(input('Ingresa tu DNI: '))

        indice = input('Ingresa el dato que quieres modificar: ')
        nuevo_valor = input('Ingresa el nuevo valor: ')

        if funcion_indice(indice, nuevo_valor):
            print(f"Diccionario actualizado: {datos}")
            break
        else:
            print("El dato no existe, intente de nuevo")
            print("______________________________________________________________")
    except ValueError:
        print("Error, dato no valido")



