from random import randint

flag = 1
victorias, empates, derrotas = 0,0,0
opcion_letrero, cpu_opcion_letero = "",""

while flag != 0:
    cpu_opcion = randint(1,3)
    print("+ - - Juego de PIEDRA, PAPEL O TIJERAS - - +")
    print(f"[Victorias del Jugador: {victorias}]    [Victorias del CPU: {derrotas}]     [Empates: {empates}]")
    print("1) Piedra")
    print("2) Papel")
    print("3) Tijeras")
    print("0) Salir...")
    opcion = int(input("[Opción]: "))

    if opcion == 1:
        opcion_letrero = "Piedra"
    elif opcion == 2:
        opcion_letrero = "Papel"
    elif opcion == 3:
        opcion_letrero = "Tijeras"
    if cpu_opcion == 1:
        cpu_opcion_letero = "Piedra"
    if cpu_opcion == 2:
        cpu_opcion_letero = "Papel"
    if cpu_opcion == 3:
        cpu_opcion_letero = "Tijeras"

    if opcion != 0:
        print(f"[JUGADOR]: {opcion_letrero}   [CPU]: {cpu_opcion_letero}")

    if opcion == 0:
        print("\nSaliendo...")
        flag = 0
    elif opcion < 1 or opcion > 3:
        print("¡Ingrese una opción válida!")
    else:
        if opcion == cpu_opcion:
            print("Empate!")
            empates += 1
        else:
            if (opcion == 1 and cpu_opcion == 2) or (opcion == 2 and cpu_opcion == 3) or (opcion == 3 and cpu_opcion == 1):
                print("Derrota!")
                derrotas += 1
            elif (opcion == 1 and cpu_opcion == 3) or (opcion == 2 and cpu_opcion == 1) or (opcion == 3 and cpu_opcion == 2):
                print("Victoria!")
                victorias += 1