"""
Nombre: Albert Alexis Contreras Mendoza
Fecha: 24 de Octubre del 2024
Descripción: Bucle while

Sintaxis
    while condicion:
        # Código mientas la condición sea verdadera

"""
"""
print("- - - Imprimir numero - - -")
num_a = int(input("Ingresa un número: "))
i = 1
print(f"Los números del 1 al {num_a} son:")
while i <= num_a:
    print(i,end = " ")
    i=i+1
print("\nFin de la impresión")
"""

print("- - - Imprimir números pares - - -")
num = int(input("Ingresa un número: "))
i = 0
print(f"Los números pares del 0 al {num} son: ")
while i <= num:
    if i % 2 == 0:
        print(i,end = " ")
    i=i+1
print("\nFin de la impresión")
