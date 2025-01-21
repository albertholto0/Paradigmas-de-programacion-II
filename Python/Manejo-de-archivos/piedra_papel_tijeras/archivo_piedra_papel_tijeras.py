import random

archivo_historial = open("archivo_piedra_papel_tijeras_historial.txt", "w", encoding="UTF-8")
victorias, empates, derrotas, rondas = 0, 0, 0, 1

reglas = {
    "Tijeras": ["Papel", "Lagarto"],
    "Papel": ["Piedra", "Spock"],
    "Piedra": ["Tijeras", "Lagarto"],
    "Lagarto": ["Spock", "Papel"],
    "Spock": ["Tijeras", "Piedra"]
}

def menu():
    print("\n+ - - [ PIEDRA, PAPEL, TIJERAS, LAGARTO O SPOCK ] - - +")
    print("1. Piedra.")
    print("2. Papel.")
    print("3. Tijeras.")
    print("4. Lagarto.")
    print("5. Spock.")
    print("\n0. Salir.")
    try:
        opcion = int(input("\nSelecciona una opción: "))
        if opcion == 1:
            return "Piedra"
        elif opcion == 2:
            return "Papel"
        elif opcion == 3:
            return "Tijeras"
        elif opcion == 4:
            return "Lagarto"
        elif opcion == 5:
            return "Spock"
        elif opcion == 0:
            return "salir"
        else:
            print("Por favor, selecciona una opción válida (0-5).")
            return None
    except ValueError as e:
        print(f"Por favor, ingresa un número válido... | {e}")
        return None

def determinar_ganador(jugador, cpu):
    if jugador == cpu:
        return "empate"
    elif cpu in reglas[jugador]:
        return "jugador"
    else:
        return "cpu"

try:
    while True:
        print(f"\n\t\t\t| Ronda actual: {rondas} | \n[Victorias: {victorias}]  [Empates: {empates}]  [Derrotas: {derrotas}]")
        archivo_historial.write(f"[Numero de ronda: {rondas}]  [Victorias: {victorias}]  [Empates: {empates}]  [Derrotas: {derrotas}]\n")

        jugador_opcion = menu()

        if jugador_opcion is None:
            continue

        if jugador_opcion == "salir":
            print("\nSaliendo del juego...")
            archivo_historial.write("\n------> El jugador cerró el juego.")
            break

        cpu_opcion = random.choice(list(reglas.keys()))
        print(f"\n[Jugador]: {jugador_opcion}  [CPU]: {cpu_opcion}")
        resultado = determinar_ganador(jugador_opcion, cpu_opcion)

        rondas += 1

        if resultado == "jugador":
            print("¡Ganaste esta ronda!")
            victorias += 1
            archivo_historial.write(f"Ronda {rondas}:\n[Jugador]: {jugador_opcion}  [CPU]: {cpu_opcion}\nEn esta ronda ganó el jugador\n\n")
        elif resultado == "cpu":
            print("¡Perdiste esta ronda!")
            derrotas += 1
            archivo_historial.write(f"Ronda {rondas}:\n[Jugador]: {jugador_opcion}  [CPU]: {cpu_opcion}\nEn esta ronda ganó el CPU\n\n")
        else:
            print("¡Es un empate!")
            empates += 1
            archivo_historial.write(f"Ronda {rondas}:\n[Jugador]: {jugador_opcion}  [CPU]: {cpu_opcion}\nEn esta ronda fue un empate\n\n")
except KeyboardInterrupt:
    print("\n\nEl programa ha sido cerrado repentinamente por el usuario...")