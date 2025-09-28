"""
Crear una función llamada division_segura(a, b) que recibirá dos
números e intentará devolver la división de a entre b
Si b es cero, debe capturar la excepción y mostrar mensaje “Error: no puedes
dividir entre cero”
Si ambos valores son válidos deben imprimir el resultado Independientemente
del resultado, debe imprimir “Operación finalizada” al final
- Usar try, except, finally

- Valida que los datos ingresados sean numéricos de lo contrario mostrar
“Error: Entrada no numérica”
- Usarás la función al menos 3 veces incluyendo un caso de error
"""

def division_segura(a, b):
    division = a / b
    return division

while True:
    resultado = "No hay resultado"
    try:
        a = int(input("Ingrese un número: "))
        b = int(input("Ingrese otro número: "))
        print("____________________________________________________________________")

        resultado = division_segura(a, b)
        break

    except ZeroDivisionError:
        print("Error: no puedes dividir entre cero.")
    except ValueError:
        print("Error: Entrada no numérica")
    finally:
        print(f"Operación finalizada: {resultado}")
        print("____________________________________________________________________")