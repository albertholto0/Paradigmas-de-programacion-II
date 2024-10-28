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

# Imprimir el encabezado para la segunda sección
print("- - - Imprimir números pares - - -")
num = int(input("Ingresa un número: "))
# Inicializar el contador para los números pares
i = 0
print(f"Los números pares del 0 al {num} son: ")
# Bucle while que itera desde 0 hasta el número ingresado
while i <= num:
    if i % 2 == 0:  # Verificar si el número es par
        print(i, end=" ")  # Imprimir el número par en la misma línea
    i = i + 1  # Incrementar el contador para el siguiente número
print("\nFin de la impresión")  # Mensaje indicando el final de la impresión
