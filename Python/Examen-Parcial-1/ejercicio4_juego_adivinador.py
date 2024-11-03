from random import randint

# Otra bandera, pero comienza en '0'
flag = 0
num_intento = 1
print("+ - - JUEGO DEL ADIVINADOR - - +")
print("Ingresa un número del 1 al 100")
num_generado = randint(1, 100)

# Para verificar el funcionamiento se muestra el siguiente letrero:
print(f"        numero generado: {num_generado}")
# En un juego real, esto se debe de ocultar

while flag == 0 and num_intento != 6:
    num_jugador = int(input(f"Intento número {num_intento}: "))
    # Compara el número ingresado con el generado aleatoriamente
    if num_jugador == num_generado:
        print("\n¡Ganaste! Has adivinado el número :D")
        print(f"Logrado en {num_intento} intento(s)...")
        flag = 1
    # Si el número es mayor, da una pista
    elif num_jugador < num_generado:
        print("El número a adivinar es MAYOR...")
    # Da una pista, si el número es menor
    elif num_jugador > num_generado:
        print("El número a adivinar es MENOR...")
    num_intento += 1
# Si el jugador termina sus intentos (pasando al intento 6),
# se muestra el mensaje de derrota :(
if num_intento > 5:
    print("\n+ - - - - - - +")
    print("Perdiste, se han acabado tus intentos.")
    print(f"El número a adivinar era: {num_generado}")