"""
Crear una función saluda_fecha(nombre, dia, mes, anio) que contendrá una
excepción para el siguiente bloque de código y tu programa no se bloquee.
Además, imprime un mensaje al usuario la causa y/o solución (Pedir
nombre, día, mes, año por consola):
Nombre: No debe recibir un dato numérico, sino decírselo al usuario Día, mes
y año: No debe recibir un dato string, sino decírselo al usuario

cadena = "Hello NOMBRE, hoy estamos DÍA de MES del AÑO"
# Hello Leonardo, hoy estamos 04 de agosto del 2025

Independientemente del resultado, debe imprimir “Operación
finalizada” al final
- Usar try, except, finally
Usar la función al menos 3 veces, incluyendo casos de error
"""

def saluda_fecha(nombre, dia, mes, año):
    cadena = f"Hello {nombre}, hoy es {dia} de {mes} del {año}"
    return cadena

while True:
    try:
        nombre = input("Ingresa tu nombre: ")
        dia = int(input("Ingresa el dia: "))
        mes = input("Ingresa el mes: ")
        año = int(input("Ingresa el año: "))

        resultado = saluda_fecha(nombre, dia, mes, año)
        print(resultado)
        break
    except ValueError:
        print("El valor ingresado no es numérico")



