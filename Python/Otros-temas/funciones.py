"""
Albert Alexis Contreras Mendoza
7 de noviembre del 2024
Programa que muestra el uso de funciones
"""

def operacion(num_a, num_b, opcion):
    if opcion == 1:
        return num_a + num_b
    elif opcion == 2:
        return num_a - num_b
    elif opcion == 3:
        return num_a * num_b
    elif opcion == 4:
        if num_b != 0:
            return num_a / num_b
        else:
            return "Error división por cero"
    else:
        return "Error: Opción no válida"

def menu():
    print("+ - - Calculadora básica - - +")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    return int(input("[Opción]: "))

while True:
    opcion = menu()
    if opcion == 0:
        break
    num_a = float(input("Número a: "))
    num_b = float(input("Número b: "))
    resultado = operacion(num_a, num_b, opcion)
    print(f"El resultado de la operación es: {resultado}")
