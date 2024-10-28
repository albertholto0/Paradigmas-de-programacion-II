"""
Nombre: Albert Alexis Contreras Mendoza
Fecha: 23 de octubre del 2024
Descripción: Este programa determina si se permite el acceso al bar "La negra".
"""

print("+ - - ACCESO AL BAR 'LA NEGRA' - - +")
# Solicita la edad y el presupuesto del usuario.
edad = int(input("Ingresa tu edad: "))
presupuesto = int(input("Ingresa tu presupuesto: "))

if edad > 18 and presupuesto >= 250:
    # Verifica que el usuario sea mayor de 18 años y tenga al menos 250 de presupuesto.
    print("¡Bienvenido a tu mejor bar!")
else:
    # Le dice al usuario que no puede entrar si no cumple con los requisitos.
    print("Lo sentimos, ya estamos por cerrar")
