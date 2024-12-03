"""
Nombre: Albert Alexis Contreras Mendoza
Fecha: 24 de Octubre del 2024
Descripción: Ejercicio 1 del ciclo while.
    Este programa calculará la suma acumulativa del cero hasta un número ingresado por el usuario. Para ello:
    a) Solicite al usuario un número mayor a cero que será el número hasta donde se realizará la suma.
    b) Calcule la suma acumulativa.
    c) Muestre el resultado de la suma.
"""
print("+ - - - Programa que calcula la suma acumulativa - - - +")
# Bucle que no permite el ingreso de un número menor o igual a 0
while True:
    num = int(input("[Ingresa el número final (mayor a 0)]: "))
    if num < 1: continue
    else: break
# Inicializar la variable de control del ciclo y el acumulador
i = 0
acumulador = 0
# Ciclo while que se ejecuta mientras i sea menor o igual al número ingresado
while i <= num:
    # Sumar el valor actual de i al acumulador
    acumulador += i
    # Incrementar i en 1 para pasar al siguiente número
    i += 1
print(f"\nLa suma de 0 hasta el {num} es de: {acumulador}")
