"""
Nombre: Albert Alexis Contreras Mendoza
Fecha: 23 de octubre del 2024
Descripción: Este programa determina un descuento en compras en "La cona"
"""
print("+ - - LA CONA - - +")
print("+- Descuentos por ser miembros de La cona -+")
cantidad = float(input("Ingresa la cantidad comprada: "))
membresia = input("¿Cuenta con la membresía? ")

hayMembresia = membresia.lower() == "si"

if hayMembresia:
    if cantidad >= 1000:
        print("Tu descuento es del 8%")
        print(f"El total es de: $ {cantidad * 0.92}")
    else:
        print("Tu descuento es de 5%")
        print(f"El total es de: $ {cantidad * 0.95}")
else:
    print("Se te invita a ser miembro de la tienda para obtener un descuento de hasta el 8%")
    print(f"El total es de: $ {cantidad}")




