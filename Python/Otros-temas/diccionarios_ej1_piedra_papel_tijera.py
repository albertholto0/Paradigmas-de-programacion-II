"""
Nombre: Albert Alexis Contreras Mendoza
Fecha: 2 de diciembre del 2024
Descripción:
    Escribe un programa de nombre Diccionarios_ej1_piedra_papel_tijera.py que realice lo siguiente:
    Este programa es una nueva versión del juego realizado de piedra, papel y tijeras, pero utilizando un diccionario para las reglas del juego.
    El juego mostrará las victorias del jugador, los partidos empatados y las victorias del CPU. Se debe mostrar el siguiente menú:
          ***  Juego de piedra, papel o tijeras  ***
        1) Piedra.
        2) Papel.
        3) Tijeras.
        0) Salir.
    Cualquier otro caso -> Opción no válida.
    Para ello:
        a) Muestre el menú en una función que pida al usuario una de las opciones: piedra, papel o tijeras.
        b) Utilice un diccionario para las distintas combinaciones.
        c) Realice la lógica adecuada para determinar al ganador. Se requiere que utilice al menos una función.
        d) Muestre la elección del jugador y la del cpu.
        e) Muestre la cantidad de victorias, empates y derrotas.
        f) Repita nuevamente el menú hasta salir.
"""
import random

# Diccionario con las reglas del juego
reglas = {
    "piedra": {"piedra": "empate", "papel": "derrota", "tijeras": "victoria"},
    "papel": {"piedra": "victoria", "papel": "empate", "tijeras": "derrota"},
    "tijeras": {"piedra": "derrota", "papel": "victoria", "tijeras": "empate"}
}

# Función para mostrar el menú
def mostrar_menu():
    print("\n***  Juego de piedra, papel o tijeras  ***")
    print("1. Piedra.")
    print("2. Papel.")
    print("3. Tijeras.")
    print("0, Salir.")
    opcion = int(input("\nSelecciona una opción: "))
    if opcion == 1:
        return "piedra"
    elif opcion == 2:
        return "papel"
    elif opcion == 3:
        return "tijeras"
    elif opcion == 0:
        return "salir"
    else:
        return None

# Función para seleccionar la jugada de la CPU
def cpu_jugada():
    return random.choice(["piedra", "papel", "tijeras"])

# Función para determinar el ganador
def jugar_ronda(jugador, cpu):
    if reglas[jugador][cpu] == "victoria":
        return "victoria"
    elif reglas[jugador][cpu] == "derrota":
        return "derrota"
    else:
        return "empate"

# Uso de variables para llevar el conteo de victorias, empates y derrotas
victorias, empates, derrotas = 0, 0, 0

while True:
    print(f"\n[Victorias: {victorias}]  [Empates: {empates}]  [Derrotas: {derrotas}]")

    # Mostrar el menú y obtener la elección del jugador
    jugador = mostrar_menu()

    if jugador == "salir":
        print("\nSaliendo del juego...")
        break
    elif jugador is None:
        print("\nOpción no válida. Por favor, intenta de nuevo.")
        continue

    # Selección aleatoria de la CPU
    cpu = cpu_jugada()
    print(f"\n[Jugador]: {jugador.capitalize()}  [CPU]: {cpu.capitalize()}")

    # Determinar el resultado de la ronda
    resultado = jugar_ronda(jugador, cpu)

    # Si el resultado de la ronda es una victoria...
    if resultado == "victoria":
        print("¡Ganaste esta ronda!")
        victorias += 1  # Incrementa el contador de victorias
    # Si el resultado de la ronda es una derrota...
    elif resultado == "derrota":
        print("¡Perdiste esta ronda!")
        derrotas += 1  # Incrementa el contador de derrotas
    # Si el resultado no es ni victoria ni derrota, se asume que es un empate
    else:
        print("¡Es un empate!")

