"""
Nombre: Albert Alexis Contreras Mendoza
Fecha: 23 de octubre del 2024
Descripción: Programa que determina la estación del año
"""

print("+ - - - Estaciones del año - - - +")
estacion = ""
num_mes = int(input("Ingresa el número de mes: "))

if num_mes >= 3 and num_mes <= 5:
    estacion = "Primavera"
elif num_mes >= 6 and num_mes <= 8:
    estacion = "Verano"
elif num_mes >= 9 and num_mes <= 11:
    estacion = "Otoño"
elif num_mes >= 1 and num_mes <= 2 or num_mes == 12:
    estacion = "Invierno"
else: estacion = "Error. Ingrese un més valido!!!"

print(f"La estación es: {estacion}")