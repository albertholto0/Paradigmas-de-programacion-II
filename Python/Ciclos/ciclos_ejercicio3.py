"""
Nombre: Albert Alexis Contreras Mendoza
Fecha: 25 de Octubre del 2024
Descripción: Calculadora con ciclo while
"""

flag = 1
while flag != 0:
    print("+ - - Calculadora básica - - +")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. División entera")
    print("6. Exponencial")
    print("0. Salir")

    opcion = int(input("[OP]: "))

    if opcion == 0:
        flag = 0
    else:
        num_a = float(input("Ingrese el primer número: "))
        num_b = float(input("Ingrese el segundo número: "))

    if opcion == 1:
        print(f"Resultado: {num_a} + {num_b} = {num_a+num_b}")
    elif opcion == 2:
        print(f"Resultado: {num_a} - {num_b} = {num_a-num_b}")
    elif opcion == 3:
        print(f"Resultado: {num_a} * {num_b} = {num_a*num_b}")
    elif opcion == 4:
        print(f"Resultado: {num_a} / {num_b} = {num_a/num_b}")
    elif opcion == 5:
        print(f"Resultado: {num_a} / {num_b} = {num_a//num_b}")
    elif opcion == 6:
        print(f"Resultado: {num_a} ^ {num_b} = {num_a**num_b}")
print("Saliendo...")