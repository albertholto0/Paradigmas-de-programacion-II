from random import randint

numero_de_partida = 0
archivo_adivinar_historial = open("archivo_adivinar_historial.txt","w",encoding = "UTF-8")

def adivinar_numero(num_partida):
    with open("archivo_adivinar_historial.txt", "a", encoding="UTF-8") as historial:
        historial.write(f"+ - - Partida [{num_partida}] - - +\n")
        intento = 5
        numero_adivinar = randint(1, 100)
        while True:
            try:
                if intento > 0:
                    print(f"\nNumero de partida: {num_partida}"
                          f"\nIntentos restantes: {intento}")
                    num_ingresado = int(input("Ingrese un número entre el 1 y el 100: "))
                    historial.write(f"El usuario ingresó [{num_ingresado}] en el intento [{intento}]\n")
                    if num_ingresado == numero_adivinar:
                        return  intento,numero_adivinar
                    elif num_ingresado < numero_adivinar:
                        print("El número a adivinar es MAYOR...")
                    elif num_ingresado > numero_adivinar:
                        print("El número a adivinar es MENOR...")
                    intento -= 1
                else:
                    return intento,numero_adivinar
            except ValueError as e:
                print(f"Ingrese un número... | {e}")

def determinar_victoria(n_intentos, n_adivinar):
    with open("archivo_adivinar_historial.txt", "a", encoding="UTF-8") as historial:
        if ultimo_intento > 0:
            print(f"¡Ganaste en {n_intentos} intento(s)!")
            historial.write(f"\nEl usuario ganó en intento [{n_intentos}].\n"
                            f"El número a adivinar era: [ {n_adivinar} ]\n")
        else:
            print("¡Perdiste! Se han terminado tus intentos :/\n"
                  f"El número a advinar era: {n_adivinar}")
            historial.write("El usuario perdió. Se le acabaron los intentos.\n"
                            f"El número a advinar era: [ {n_adivinar} ]\n")

try:
    while True:
        if numero_de_partida == 0:
            print(" ¡Adivina el número!")
            seguir_jugando = input("¿Jugar? [Si / No]: ")
        else:
            seguir_jugando = input("¿Seguir jugando? [Si / No]: ")

        if seguir_jugando.lower() == 'si':
            numero_de_partida += 1
            ultimo_intento, numero_generado = adivinar_numero(numero_de_partida)
            determinar_victoria(ultimo_intento, numero_generado)
        elif seguir_jugando.lower() == 'no':
            print("Saliendo...")
            break
        else:
            print("Por favor, ingresa una opción válida (Si / No).")
except KeyboardInterrupt:
    print(f"\n\nEl programa ha sido cerrado repentinamente por el usuario...")

