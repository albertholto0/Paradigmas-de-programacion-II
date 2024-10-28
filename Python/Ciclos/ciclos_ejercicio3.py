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

    # Opción para salir del programa
    if opcion == 0:
        flag = 0  # Cambia el valor de 'flag' a 0, lo que causará que el ciclo while termine en la próxima iteración
    else:
        # Si la opción no es 0, se solicita al usuario que ingrese dos números para realizar la operación seleccionada
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