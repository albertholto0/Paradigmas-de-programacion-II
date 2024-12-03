"""
Nombre: Albert Alexis Contreras Mendoza
Fecha: 24 de Octubre del 2024
Descripción: Programa que imprime 4 tipos de piramides
Este programa imprime una pirámide de caracteres '*' de cuatro formas y es la versión del ejercicio Ciclos_ej5_piramide.py, pero ahora utilizando funciones.
Cada pirámide debe estar en una función, la cual se llama en el código a nivel de módulo de acuerdo a las filas requeridas por el usuario.

1) Creciente a la izquierda       2) Decreciente a la izquierda       3) Creciente centrada       4) Creciente a la derecha
*                                  ***                                 *                          *
**                                 **                                 ***                        **
***                                *                                 *****                      ***

Para ello:
a) Solicite el número de filas de la pirámide en el código a nivel de módulo.
b) Defina una función para cada pirámide, recibiendo el número de filas como parámetro.
"""

def piramide_creciente_izquierda(n):
    for i in range(1, n + 1):   # Itera desde el primer número hasta el último que se quiere incluir
        asteriscos = "*" * i    # Crea la cadena con "i" asteriscos
        print(asteriscos)       # Imprime la cadena, formando una línea de la pirámide
    print("")                   # Línea en blanco para separar las figuras

def piramide_decreciente_izquierda(n):
    for i in range(n, 0, -1):   # Itera desde n hasta 1, decrementando en 1
        asteriscos = "*" * i    # Crea una cadena con "i" asteriscos
        print(asteriscos)       # Imprime la cadena, formando una línea de la pirámide decreciente
    print("")                   # Línea en blanco para separar las figuras

def piramide_centrada(n):
    for i in range(1, n + 1):               # Itera desde el primer número hasta el último que se quiere incluir
        espacios = " " * (n - i)            # Crea una cadena con (n-i) espacios para centrar la línea
        asteriscos = "*" * (2 * i - 1)      # Crea una cadena con (2*i - 1) asteriscos, que aumenta en cada línea
        print(f"{espacios}{asteriscos}")    # Imprime los espacios seguidos de los asteriscos, dando forma a una pirámide simétrica
    print("")                               # Línea en blanco para separar las figuras

def piramide_creciente_derecha(n):
    for i in range(1, n + 1):               # Itera desde el primer número hasta el último que se quiere incluir
        espacios = " " * (n - i)            # Crea una cadena con (n-i) espacios para alinear la pirámide a la derecha
        asteriscos = "*" * i                # Crea una cadena con i asteriscos
        print(f"{espacios}{asteriscos}")    # Imprime los espacios seguidos de los asteriscos
    print("")                               # Línea en blanco para separar las figuras

# Función para mostrar el menú
def mostrar_menu():
    print("Selecciona el tipo de pirámide:")
    print("1. Pirámide creciente alineada a la izquierda")
    print("2. Pirámide decreciente alineada a la izquierda")
    print("3. Pirámide centrada")
    print("4. Pirámide creciente alineada a la derecha")
    print("0. Salir")

# Código a nivel de módulo
# Bucle infinito para el menú
while True:
    mostrar_menu()
    opcion = int(input("Elige una opción: "))

    if opcion == 0:
        # Ingresando 0 el bucle infinito finaliza
        print("Saliendo del programa...")
        break
    if opcion == 1:
        m = int(input("Ingresa el número de filas para la pirámide: "))
        piramide_creciente_izquierda(m)
    elif opcion == 2:
        m = int(input("Ingresa el número de filas para la pirámide: "))
        piramide_decreciente_izquierda(m)
    elif opcion == 3:
        m = int(input("Ingresa el número de filas para la pirámide: "))
        piramide_centrada(m)
    elif opcion == 4:
        m = int(input("Ingresa el número de filas para la pirámide: "))
        piramide_creciente_derecha(m)
    else:
        print("Opción no válida, intenta de nuevo.\n")