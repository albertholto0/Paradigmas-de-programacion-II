"""
Nombre: Albert Alexis Contreras Mendoza
Fecha: 24 de Octubre del 2024
Descripción: Ejercicio 2 de bucles
"""

print("+ - - Programa que calcula la suma acumulativa entre 2 números - - +")
num_a = int(input("Ingresa número inicial: "))
num_b = int(input("Ingresa número final: "))
acumulador = 0
i = num_a

while i <= num_b:
    acumulador += i
    i += 1
print(f"La suma de {num_a} hasta {num_b} es de: {acumulador}")