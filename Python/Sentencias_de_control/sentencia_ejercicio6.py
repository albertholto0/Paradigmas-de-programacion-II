"""
Nombre: Albert Alexis Contreras Mendoza
Fecha: 23 de octubre del 2024
Descripción: Este programa mostrará los detalles del tour turístico Ecoturixtlán.
"""

precio_adulto = 200  # Precio por cada adulto
precio_nino = 100    # Precio por cada niño

print("+ - - TOUR TURÍSTICO ECOTURIXTLÁN - - +")

nombre = input("Ingresa nombre del cliente: ")
num_adultos = int(input("Ingresa el número de adultos: "))
num_ninos = int(input("Ingresa el número de niños: "))
dia = input("Ingresa el dia de la semana: ").lower()

# Determina el descuento si la visita es lunes, martes o jueves.
if dia == "lunes" or dia == "martes" or dia == "jueves":
    descuento = 0.90  # Descuento del 10%
else:
    descuento = 1     # Sin descuento

# Calcula y muestra el costo total del tour con el descuento, si aplica.
print(f"Gracias por tu visita {nombre} este día {dia}. COSTO TOTAL: ${(num_adultos * precio_adulto + num_ninos * precio_nino) * descuento}")
