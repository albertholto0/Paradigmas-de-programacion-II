from random import randint

# Este programa tambien funciona con una 'bandera'
flag = 1
victorias, empates, derrotas = 0,0,0
opcion_letrero, cpu_opcion_letero = "",""

while flag != 0:
    # Genera de manera aleatoria, la elección de la CPU
    # (1 para Piedra, 2 para Papel, 3 para Tijeras).
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

    # Si el jugador no selecciona la opción de salir (opción 0), muestra las elecciones de ambos.
    if opcion != 0:
        print(f"[JUGADOR]: {opcion_letrero}   [CPU]: {cpu_opcion_letero}")

    if opcion == 0:
        print("\nSaliendo...")
        flag = 0    # La bandera cambia a 0
    elif opcion < 1 or opcion > 3:
        print("¡Ingrese una opción válida!")
    else:
        if opcion == cpu_opcion:
            print("Empate!")
            empates += 1
        else:
            # Piedra pierde contra Papel, Papel pierde contra Tijeras, Tijeras pierde contra Piedra
            if (opcion == 1 and cpu_opcion == 2) or (opcion == 2 and cpu_opcion == 3) or (opcion == 3 and cpu_opcion == 1):
                print("Derrota!")
                derrotas += 1
            # Piedra gana contra Tijeras, Papel gana contra Piedra, Tijeras gana contra Papel
            elif (opcion == 1 and cpu_opcion == 3) or (opcion == 2 and cpu_opcion == 1) or (opcion == 3 and cpu_opcion == 2):
                print("Victoria!")
                victorias += 1