"""
Nombre: Albert Alexis Contreras Mendoza
Fecha: 2 de diciembre del 2024
Descripción: Ejercicio aplicando los conceptos de conjuntos
    Este programa es una rifa, en donde se registra el correo electrónico y solamente permite ingresar un correo por participante.
    Se debe mostrar el siguiente menú:
          ***  Rifa de una computadora  ***
        1) Ver correos de participantes.
        2) Agregar correo de participante.
        3) Eliminar correo de participante.
        4) Seleccionar ganador.
        0) Salir.
    Cualquier otro caso -> Opción no válida.
    Para ello:
        a) Utilice un conjunto para almacenar los correos de los participantes.
        b) Utilice un valor aleatorio utilizando la función random.choice(lista). Notar que hay que convertir primero a una lista.
"""
import random

# Conjunto vacío
participantes = set()

# Función para mostrar el menú
def mostrar_menu():
    print("\n***  Rifa de una computadora  ***")
    print("1) Ver correos de participantes.")
    print("2) Agregar correo de participante.")
    print("3) Eliminar correo de participante.")
    print("4) Seleccionar ganador.")
    print("0) Salir.")
    return int(input("\nIngresa una de las opciones: "))

# Función para ver los correos de los participantes
def ver_participantes():
    if not participantes:
        print("\nNo hay participantes en la rifa.")
    else:
        print("\n*** Participantes registrados ***")
        # Usa "enumerate" para obtener el índice y el valor de cada elemento en la lista. "Start" para comenzar en 1 y no en 0
        for i, correo in enumerate(participantes, start=1):
            print(f"{i}. {correo}")

# Función para agregar un correo de participante
def agregar_participante():
    correo = input("\nIngresa el correo del participante: ")
    if correo in participantes:
        print("Este correo ya está registrado en la rifa.")
    else:
        participantes.add(correo)
        print(f"{correo} ha sido registrado como participante.")

# Función para eliminar un correo de participante
def eliminar_participante():
    if not participantes:
        print("\nNo hay participantes para eliminar.")
    else:
        ver_participantes()  # Muestra los participantes actuales
        try:
            indice = int(input("\nIngresa el número del participante a eliminar: ")) - 1 # Esto permite convertir la entrada del usuario (que usa numeración desde 1) a un índice de lista (que empieza desde 0).
            if 0 <= indice < len(participantes):    # len() devuelve la cantidad de elementos en la lista participantes
                participante_a_eliminar = list(participantes)[indice]
                participantes.remove(participante_a_eliminar)
                print(f"{participante_a_eliminar} ha sido eliminado de la rifa.")
            else:
                print("Índice fuera de rango.")
        except ValueError:
            print("Por favor, ingresa un número válido.")

# Función para seleccionar un ganador aleatorio
def seleccionar_ganador():
    if not participantes:
        print("\nNo hay participantes para seleccionar un ganador.")
    else:
        ganador = random.choice(list(participantes))  # Convierte a lista para usar random.choice
        print(f"\nEl ganador de la rifa es: {ganador}")

# Código a nivel de módulo
while True:
    opcion = mostrar_menu()
    if opcion == 0:
        print("\nSaliendo de la rifa...")
        break
    elif opcion == 1:
        ver_participantes()
    elif opcion == 2:
        agregar_participante()
    elif opcion == 3:
        eliminar_participante()
    elif opcion == 4:
        seleccionar_ganador()
    else:
        print("\nOpción no válida. Por favor, intenta de nuevo.")