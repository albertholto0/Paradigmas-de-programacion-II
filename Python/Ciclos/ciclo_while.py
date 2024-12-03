"""
Nombre: Albert Alexis Contreras Mendoza
Fecha: 24 de Octubre del 2024
Descripción: Bucle while
    El ciclo while es una estructura de control fundamental en la programación que permite repetir un bloque de código mientras una determinada condición se evalúe como verdadera.

    Sintaxis:
    while condicion:
        # Código a ejecutar mientras la condición sea verdadera.

    # Nota: No hay llaves, sino que se deja un espacio.
"""
"""
# Ejemplo de uso del ciclo while. Imprimir los números del 1 hasta un número solicitado por consola.
print("- - - Imprimir numero - - -")
num_a = int(input("Ingresa un número: ")) # Se solicita un número al usuario.
i = 1
print(f"Los números del 1 al {num_a} son:")
while i <= num_a:
    print(i,end = " ") # El "end =" controla el carácter que se imprime al final de la función print()
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
