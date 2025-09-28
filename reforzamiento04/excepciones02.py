"""
Crear una función y dentro la respectiva excepción o excepciones para el
siguiente bloque de código para que tu programa no se bloquee, ya que solo
aceptará datos tipos entero y además imprimir un mensaje al usuario la causa
y/o solución. También debe indicar el índice donde ingresarás este nuevo dato,
si el índice está fuera de rango indicárselo al usuario:
lista = [2, 6, 10, 4, 5, 23, 1]
lista[10]: No es posible ingresar el dato, índice fuera de rango
- Usarás dos tipos diferentes de excepciones (IndexError TypeError) y
- Usarás la función al menos 3 veces incluyendo un caso de error
"""

valores = [2, 4, 8, 16]
print(f"La lista inicial es {valores}")

while True:
    try:
        posicion = int(input("Ingresar la posición del número que quiere eliminar: "))
        valor = int(input("Ingresar un numero que quiere ingresar: "))

        def operacion(valor, posicion):
            valores.append(valor)
            del valores[posicion]
            return valores

        resultado = operacion(valor, posicion)

        print(f"La lista actualizada es: {resultado}")
        break
    except ValueError:
        print("El valor ingresado no es un numero")
        print("_______________________________________________________________________")
    except IndexError:
        print("La posición ingresada no es correcta")
        print("_______________________________________________________________________")



