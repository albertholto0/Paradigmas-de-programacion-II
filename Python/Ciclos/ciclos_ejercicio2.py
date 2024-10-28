"""
Nombre: Albert Alexis Contreras Mendoza
Fecha: 24 de Octubre del 2024
Descripción: Ejercicio 2 de bucles
"""
print("+ - - Programa que calcula la suma acumulativa entre 2 números - - +")
num_a = int(input("Ingresa número inicial: "))
num_b = int(input("Ingresa número final: "))

acumulador = 0
# Guarda en i el valor del primer número, para no afectarlo
i = num_a

# Bucle que itera desde el número inicial hasta el número final
while i <= num_b:
    acumulador += i  # Acumula la suma de i
    i += 1  # Incrementa i para continuar con el siguiente número
print(f"La suma de {num_a} hasta {num_b} es de: {acumulador}")
