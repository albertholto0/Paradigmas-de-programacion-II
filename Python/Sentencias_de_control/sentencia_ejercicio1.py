"""
Nombre: Albert Alexis Contreras Mendoza
Fecha: 23 de octubre del 2024
Descripción: Programa que determina cual de los dos números es el menor
"""

print("- - - ¿Cuál de los dos números es menor? - - -")
a = float(input("Ingrese número a: "))
b = float(input("Ingrese número b: "))

if a > b:
    print(f"El número {b} es menor que {a}.")
elif a < b:
    print(f"El número {a} es menor que {b}.")
elif a == b:
    print("Ambos números son iguales.")