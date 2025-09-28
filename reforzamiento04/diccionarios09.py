"""
Una empresa desea gestionar las facturas pendientes que tiene por pagar,
para esto se creará un diccionario donde tendrá por key el número de factura
“00054” y su value será el coste de la factura. El programa tendrá la opción
de pedir nueva factura (por consola) que se agregará al diccionario. Cada vez
que el área de contabilidad pague una factura se pedirá el número de factura
que fue cancelada, si existe mostrar un mensaje donde indicará “La factura
ya está cancelada” caso contrario “El número de factura no existe”. Considerar
que cada vez que se realice algún pago o ingreso de una nueva factura se mostrará
inmediatamente al diccionario actualizado.
"""

facturas = {"00054": 2500}

cantidad = int(input("¿Cuantas facturas quieres agregar?:"))
print("_______________________________________________________________")

while len(facturas.keys()) <= cantidad:
    valores = 0
    for valores in range(cantidad):
        numero = input(f"Ingrese el numero de la factura {valores+1}:")
        precio = input(f"Ingrese el precio de la factura {valores+1}:")
        facturas[numero] = float(precio)
        print("La lista ha sido actualizada:", facturas)
        print("_______________________________________________________________")
    break

while True:
    cantidad_2 = int(input("¡Cuantas facturas quieres cancelar?:"))
    print("_______________________________________________________________")
    if cantidad_2 > len(facturas.keys()):
        print("El valor no existe")
    else:
        break
while True:
    valores = 0
    for valores in range(cantidad_2):
        print("_______________________________________________________________")
        numero = input(f"Ingrese el número de la factura que desea cancelar:")
        if numero not in facturas.keys():
            print("El númreo de factura no existe")
        else:
            del(facturas[numero])

        if len(facturas.keys()) != 0:
            print("La factura ya ha sido cancelada:", facturas)

        else:
            print("_______________________________________________________________")
            print("Todas las facturas han sido canceladas")
    break




