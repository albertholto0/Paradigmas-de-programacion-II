"""
Este programa es una versión mejorada del juego de piedra, papel y tijeras. Las reglas se muestran en el siguiente video:
    https://youtu.be/pIpmITBocfM
    Se debe mostrar el siguiente menú
          ***  Juego de piedra, papel, tijeras, lagarto, spock  ***
        1) Piedra.
        2) Papel.
        3) Tijeras.
        4) Lagarto.
        5) Spock.
        6) Ver reglas.
        0) Salir.
    Cualquier otro caso -> Opción no válida.
    Para ello:
        a) Muestre el menú en una función que pida al usuario una de las opciones.
        b) Utilice un diccionario para las distintas combinaciones.
        c) Realice la lógica adecuada para determinar al ganador.
        d) Muestre la elección del jugador y la del cpu.
        e) Muestre la cantidad de victorias, empates y derrotas.
        f) Repita nuevamente el menú hasta salir.
"""

import random

# Diccionario con las reglas del juego
reglas = {
    "Tijeras": ["Papel", "Lagarto"],
    "Papel": ["Piedra", "Spock"],
    "Piedra": ["Tijeras", "Lagarto"],
    "Lagarto": ["Spock", "Papel"],
    "Spock": ["Tijeras", "Piedra"]
}

# Variables para el puntaje
victorias = 0
empates = 0
derrotas = 0

# Función para mostrar el menú
def mostrar_menu():
    print("\n***  Juego de piedra, papel, tijeras, lagarto, spock  ***")
    print("1) Piedra.")
    print("2) Papel.")
    print("3) Tijeras.")
    print("4) Lagarto.")
    print("5) Spock.")
    print("6) Ver reglas.")
    print("0) Salir.")
    return input("Ingresa una de las opciones: ")

# Función para mostrar las reglas
def mostrar_reglas():
    print("\nReglas:")
    print("Selecciona una de las opciones de acuerdo a lo siguiente:")
    print("- Tijeras cortan papel.")
    print("- Papel cubre piedra.")
    print("- Piedra aplasta lagarto.")
    print("- Lagarto envenena Spock.")
    print("- Spock destruye tijeras.")
    print("- Tijeras decapitan lagarto.")
    print("- Lagarto come papel.")
    print("- Papel desaprueba Spock.")
    print("- Spock vaporiza piedra.")
    print("- Piedra aplasta tijeras.")
    print("\nLa CPU va a elegir una de las opciones de manera aleatoria.")

# Función para determinar el ganador
def determinar_ganador(eleccion_jugador, eleccion_cpu):
    global victorias, empates, derrotas
    if eleccion_jugador == eleccion_cpu:
        print(f"\n¡Empate! Ambos eligieron {eleccion_jugador}.")
        empates += 1
    elif eleccion_cpu in reglas[eleccion_jugador]:
        print(f"\n¡Victoria! {eleccion_jugador} gana a {eleccion_cpu}.")
        victorias += 1
    else:
        print(f"\n¡Derrota! {eleccion_cpu} gana a {eleccion_jugador}.")
        derrotas += 1

# Bucle principal del juego
while True:
    opcion = mostrar_menu()

    if opcion == "0":
        print("\nSaliendo del juego...")
        break
    elif opcion == "1":
        eleccion_jugador = "Piedra"
    elif opcion == "2":
        eleccion_jugador = "Papel"
    elif opcion == "3":
        eleccion_jugador = "Tijeras"
    elif opcion == "4":
        eleccion_jugador = "Lagarto"
    elif opcion == "5":
        eleccion_jugador = "Spock"
    elif opcion == "6":
        mostrar_reglas()
        continue
    else:
        print("Opción no válida.")
        continue

    # Elección aleatoria de la CPU
    eleccion_cpu = random.choice(["Piedra", "Papel", "Tijeras", "Lagarto", "Spock"])
    print(f"\nTu elección: {eleccion_jugador}")
    print(f"La CPU elige: {eleccion_cpu}")

    # Determinar el ganador
    determinar_ganador(eleccion_jugador, eleccion_cpu)

    # Mostrar el puntaje actual
    print(f"\nVictorias: {victorias} | Empates: {empates} | Derrotas: {derrotas}")
