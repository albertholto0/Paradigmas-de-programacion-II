"""
Nombre: Albert Alexis Contreras Mendoza
Fecha: 23 de octubre del 2024
Descripción: Programa que determina cual de los dos números es el menor
"""

print("- - - ¿Cuál de los dos números es menor? - - -")
a = float(input("Ingrese número a: "))
b = float(input("Ingrese número b: "))

# Compara los dos números para determinar cuál es el menor
if a > b:
    # Si 'a' es mayor que 'b', entonces 'b' es el menor
    print(f"El número {b} es menor que {a}.")
elif a < b:
    # Si 'a' es menor que 'b', entonces 'a' es el menor
    print(f"El número {a} es menor que {b}.")
else:
    # Si 'a' es igual a 'b', indica que ambos números son iguales
    print("Ambos números son iguales.")