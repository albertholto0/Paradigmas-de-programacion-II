"""
Nombre: Albert Alexis Contreras Mendoza
Fecha: 24 de Octubre del 2024
Descripción: Ejercicio 1 del ciclo while
"""
print("+ - - - Programa que calcula la suma acumulativa - - - +")
num = int(input("Ingresa el número final: "))
# Inicializar la variable de control del ciclo y el acumulador
i = 0
acumulador = 0
# Ciclo while que se ejecuta mientras i sea menor o igual al número ingresado
while i <= num:
    # Sumar el valor actual de i al acumulador
    acumulador += i
    # Incrementar i en 1 para pasar al siguiente número
    i += 1
print(f"La suma de 0 hasta el {num} es de: {acumulador}")
