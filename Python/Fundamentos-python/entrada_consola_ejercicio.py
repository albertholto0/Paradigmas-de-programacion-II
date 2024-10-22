"""
Nombre: Albert Alexis Contreras Mendoza
Fecha: 15 de octubre del 2024
Descripción: Ejercicio aplicando los conocimientos de la lección <<entrada consola>>

Escribe un programa de nombre Entrada_consola_ejercicio.py que realice lo siguiente:
a) Pida 2 números decimales por consola al usuario utilizando la función input.
b) Muestre los resultados de las operaciones básicas con esos números: suma, resta, multiplicación y división.
Nota: Asuma que el usuario siempre va a ingresar números y que el segundo número es diferente de cero.
"""

#Pide al usuario que ingrese un número decimal
num_a = float(input("Ingrese un número decimal: "))

#Pide al usuario que ingrese otro número decimal
num_b = float(input("Ingrese otro número decimal: "))

#Muestra los resultados de las operaciones básicas
#Se utiliza una f-string para incluir los valores en el mensaje.
print("- - - Operaciones básicas - - -")
print(f"El resultado de la SUMA de {num_a} + {num_b} = {num_a + num_b}")
print(f"El resultado de la RESTA de {num_a} - {num_b} = {num_a - num_b}")
print(f"El resultado de la MULTIPLICACIÓN de {num_a} * {num_b} = {num_a * num_b}")
print(f"El resultado de la DIVISIÓN de {num_a} / {num_b} = {num_a / num_b}")
