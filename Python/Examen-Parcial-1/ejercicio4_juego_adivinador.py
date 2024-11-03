from random import randint

flag = 0
num_intento = 1
print("+ - - JUEGO DEL ADIVINADOR - - +")
print("Ingresa un número del 1 al 100")
num_generado = randint(1, 100)
print(f"        numero generado: {num_generado}")

while flag == 0 and num_intento != 6:
    num_jugador = int(input(f"Intento número {num_intento}: "))
    if num_jugador == num_generado:
        print("¡Ganaste! Has adivinado el número :D")
        flag = 1
    elif num_jugador < num_generado:
        print("El número a adivinar es MAYOR...")
    elif num_jugador > num_generado:
        print("El número a adivinar es MENOR...")
    num_intento += 1
if num_intento > 5:
    print("\n+ - - - - - - +")
    print("Perdiste, se han acabado tus intentos.")
    print(f"El número a adivinar era: {num_generado}")