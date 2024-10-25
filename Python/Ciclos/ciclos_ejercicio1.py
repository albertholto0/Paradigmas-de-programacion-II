"""
Nombre: Albert Alexis Contreras Mendoza
Fecha: 24 de Octubre del 2024
Descripción: Ejercicio 1 del ciclo while
"""

print("+ - - - Programa que calcula la suma acumulativa - - - +")
num = int(input("Ingresa el número final: "))
i = 0
acumulador = 0
while i <= num:
    acumulador += i
    i += 1
print(f"La suma de 0 hasta el {num} es de: {acumulador}")
