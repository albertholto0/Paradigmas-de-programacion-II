"""
Nombre: Albert Alexis Contreras Mendoza
Fecha: 24 de Octubre del 2024
Descripción: Ejercicio 2 de bucles
    Escribe un programa de nombre Ciclos_ej2_suma_acumulativa_v2.py que realice lo siguiente:
    Este programa calculará la suma acumulativa de dos números ingresados por el usuario.
    A diferencia del programa anterior, ahora el usuario también definirá el número inicial. Para ello:
        a) Solicite al usuario los números inicial y final de la suma acumulativa.
        b) Calcule la suma acumulativa entre ambos números.
        c) Muestre el resultado de la suma.
"""
print("+ - - Programa que calcula la suma acumulativa entre 2 números - - +")
while True:
    # Ingresamos el número inicial (num_a) y número final (num_b)
    num_a = int(input("Ingresa número inicial: "))
    num_b = int(input("Ingresa número final: "))
    if num_b < num_a:
        print("El número inicial debe ser MENOR que el número final")
        continue
    else: break

acumulador = 0
# Guarda en i el valor del primer número, para no afectarlo
i = num_a
# Bucle que itera desde el número inicial hasta el número final
while i <= num_b:
    acumulador += i  # Acumula la suma de i
    i += 1  # Incrementa i para continuar con el siguiente número
print(f"La suma de {num_a} hasta {num_b} es de: {acumulador}")
