"""
Nombre: Albert Alexis Contreras Mendoza
Fecha: 24 de Octubre del 2024
Descripción: Programa que imprime 4 tipos de pirámides
Escribe un programa de nombre Ciclos_ej5_piramide.py que realice lo siguiente:
Este programa imprime una pirámide de caracteres '*' de cuatro formas:

1) Creciente a la izquierda       2) Decreciente a la izquierda       3) Creciente centrada       4) Creciente a la derecha
*                                  ***                                 *                          *
**                                 **                                 ***                        **
***                                *                                 *****                      ***

en donde el usuario ingresa el número de filas. Para ello:
a) Solicite el número de filas de la pirámide.
b) Muestre los tres tipos de pirámides utilizando la lógica adecuada.
"""

while True:
    # Muestra el menú
    print("Selecciona el tipo de pirámide:")
    print("1. Pirámide creciente alineada a la izquierda")
    print("2. Pirámide decreciente alineada a la izquierda")
    print("3. Pirámide centrada")
    print("4. Pirámide creciente alineada a la derecha")
    print("0. Salir")

    opcion = int(input("Elige una opción: "))

    if opcion == 0:
        print("Saliendo del programa...")
        break

    if opcion == 1:
        m = int(input("Ingresa el número de filas para la pirámide: "))
        for i in range(1, m + 1):   # Itera desde el primer número hasta el último que se quiere incluir
            asteriscos = "*" * i    # Crea la cadena con "i" asteriscos
            print(asteriscos)       # Imprime la cadena, formando una línea de la pirámide
        print("")                   # Línea en blanco para separar las figuras

    elif opcion == 2:
        m = int(input("Ingresa el número de filas para la pirámide: "))
        for i in range(m, 0, -1):   # Itera desde n hasta 1, decrementando en 1
            asteriscos = "*" * i    # Crea una cadena con "i" asteriscos
            print(asteriscos)       # Imprime la cadena, formando una línea de la pirámide decreciente
        print("")                   # Línea en blanco para separar las figuras

    elif opcion == 3:
        m = int(input("Ingresa el número de filas para la pirámide: "))
        for i in range(1, m + 1):               # Itera desde el primer número hasta el último que se quiere incluir
            espacios = " " * (m - i)            # Crea una cadena con (n-i) espacios para centrar la línea
            asteriscos = "*" * (2 * i - 1)      # Crea una cadena con (2*i - 1) asteriscos, que aumenta en cada línea
            print(f"{espacios}{asteriscos}")    # Imprime los espacios seguidos de los asteriscos, dando forma a una pirámide simétrica
        print("")                               # Línea en blanco para separar las figuras

    elif opcion == 4:
        m = int(input("Ingresa el número de filas para la pirámide: "))
        for i in range(1, m + 1):               # Itera desde el primer número hasta el último que se quiere incluir
            espacios = " " * (m - i)            # Crea una cadena con (n-i) espacios para alinear la pirámide a la derecha
            asteriscos = "*" * i                # Crea una cadena con i asteriscos
            print(f"{espacios}{asteriscos}")    # Imprime los espacios seguidos de los asteriscos
        print("")                               # Línea en blanco para separar las figuras

    else:
        print("Opción no válida, intenta de nuevo.\n")