"""
Nombre: Albert Alexis Contreras Mendoza
Fecha: 2 de diciembre del 2024
Descripción: Ejercicio que implementa el uso de tuplas
    Este programa almacena diversos puntos como coordenadas y permite obtener la ecuación de la recta entre dos de los puntos.
    Se debe mostrar el siguiente menú:
          ***  Rectas a partir de puntos (coordenadas) en el plano cartesiano  ***
        1) Ver coordenadas almacenadas.
        2) Agregar coordenada (x,y).
        3) Calcular la pendiente y la ecuación de la recta entre dos coordenadas.
        4) Eliminar coordenada (x,y).
        0) Salir.
    Cualquier otro caso -> Opción no válida.
    Para ello:
        a) Utilice funciones para modular el código.
        b) Utilice una tupla para almacenar las coordenadas (x,y) del punto.
        c) Utilice una lista para almacenar las tuplas de las coordenadas.
"""
coordenadas = []
# Función que muestre el menú
def menu():
    print("\n***  Rectas a partir de puntos (coordenadas) en el plano cartesiano  ***")
    print("1. Ver coordenadas almacenadas")
    print("2. Agregar coordenadas (x,y)")
    print("3. Calcular la pendiente y la ecuación de la recta entre dos coordenadas")
    print("4. Eliminar coordenada (x,y)")
    print("0. Salir...")
    return input("\nIngresa una de las opciones: ")

# Función para mostrar coordenadas
def ver_coordenadas():
    if not coordenadas:
        print("Lista vacía...")
    else:
        for i,coordenada in enumerate(coordenadas, start=1):
            print(f"{i}. {coordenada}")
# Función para agregar coordenada
def agregar_coordenadas():
    while True:
        # Solicitar las coordenadas
        x = input("Coordenada [x]: ")
        y = input("Coordenada [y]: ")
        # Intentar convertir las entradas a float
        try:
            # El bloque 'try' intenta ejecutar este código
            x = float(x)
            y = float(y)
        except ValueError:
            # Si ocurre un error (en este caso, si el usuario llegase a ingresar algo no numérico) el bloque 'except' captura el error y ejecuta este código
            print("Ingrese un dato válido...")
            continue  # Si no se puede convertir, vuelve a pedir las coordenadas
        # Si se convirtió correctamente, agregar la coordenada
        coordenadas.append((x, y))
        print(f"Coordenada ({x}, {y}) agregada exitosamente.")
        break
# Función para calcular la ecuación de la recta con 2 pares de coordenadas
def calcular_recta():
    if len(coordenadas) < 2:
        print("\nSe necesitan al menos dos coordenadas para calcular la recta.")
        return
    # Mostrar coordenadas para que el usuario seleccione
    ver_coordenadas()
    while True:
        # Selección de las dos coordenadas
        indice1 = input("Selecciona el número de la primera coordenada: ")
        indice2 = input("Selecciona el número de la segunda coordenada: ")
        # Verificar si las entradas son números enteros
        if indice1.isdigit() and indice2.isdigit():
            indice1 = int(indice1) - 1  # Ajustar el índice (base 0)
            indice2 = int(indice2) - 1  # Ajustar el índice (base 0)
            # Validar índices
            if 0 <= indice1 < len(coordenadas) and 0 <= indice2 < len(coordenadas) and indice1 != indice2:
                x1, y1 = coordenadas[indice1]
                x2, y2 = coordenadas[indice2]
                # Calcular la pendiente
                if x1 == x2:
                    print("\nLa pendiente es indefinida (recta vertical).")
                    print(f"Ecuación de la recta: x = {x1}")
                else:
                    pendiente = (y2 - y1) / (x2 - x1)
                    b = y1 - pendiente * x1
                    print(f"\nLa pendiente de la recta es: {pendiente:.2f}")
                    print(f"Ecuación de la recta: y = {pendiente:.2f}x + {b:.2f}")
                break
            else:
                print("Selección de coordenadas no válida. Intenta de nuevo.")
        else:
            print("Por favor, ingresa números válidos.")

# Función para eliminar coordenadas
def eliminar_coordenada():
    if not coordenadas:
        print("\nNo hay coordenadas para eliminar.")
    else:
        ver_coordenadas()  # Mostrar las coordenadas actuales
        while True:
            # Solicitar el índice de la coordenada a eliminar
            indice = int(input("Selecciona el número de la coordenada a eliminar: "))
            if indice % 1 == 0:  # Verificar si la entrada es un número entero
                indice -= 1  # Ajustar el índice (base 0)
                if 0 <= indice < len(coordenadas):
                    coordenada_eliminada = coordenadas.pop(indice)  # Eliminar la coordenada
                    print(f"Coordenada {coordenada_eliminada} eliminada correctamente.")
                    break  # Salir del bucle después de eliminar
                else:
                    print("Número de coordenada no válido. Intenta de nuevo.")
            else:
                print("Por favor, ingresa un número válido.")  # Mensaje si la entrada no es un número

# Código a nivel de módulo
while True:
    menu()
    opcion = input("\nIngresa una de las opciones: ")

    if opcion == '1':
        ver_coordenadas()
    elif opcion == '2':
        agregar_coordenadas()
    elif opcion == '3':
        calcular_recta()
    elif opcion == '4':
        eliminar_coordenada()
    elif opcion == '0':
        print("\nSaliendo del programa...")
        break
    else:
        print("\nOpción no válida. Intenta de nuevo.")