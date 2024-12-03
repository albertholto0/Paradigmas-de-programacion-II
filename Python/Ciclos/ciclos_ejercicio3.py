"""
Nombre: Albert Alexis Contreras Mendoza
Fecha: 25 de Octubre del 2024
Descripción: Calculadora con ciclo while
    Este programa es una calculadora básica que contenga el siguiente menú:
        1) Suma.
        2) Resta.
        3) Multiplicación.
        4) División.
        5) División entera.
        6) Exponenciación.
        0) Salir.
        Cualquier otro caso -> Mostrar un mensaje de "opción no válida".
"""
flag = 1
while flag != 0:
    # Menú básico
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
    elif 0 < opcion < 7:
            # Si la opción no es 0, se solicita al usuario que ingrese dos números para realizar la operación seleccionada
            num_a = float(input("Ingrese el primer número: "))
            num_b = float(input("Ingrese el segundo número: "))
    else:
        # Si se ingresa una opción distinta al menú
        print("Ingrese una opción válida...")
    if opcion == 1: print(f"Resultado: {num_a} + {num_b} = {num_a + num_b:.2f}")
    elif opcion == 2: print(f"Resultado: {num_a} - {num_b} = {num_a - num_b:.2f}")
    elif opcion == 3: print(f"Resultado: {num_a} * {num_b} = {num_a * num_b:.2f}")
    elif opcion == 4: print(f"Resultado: {num_a} / {num_b} = {num_a / num_b:.2f}")
    elif opcion == 5: print(f"Resultado: {num_a} // {num_b} = {num_a // num_b:.2f}")
    elif opcion == 6: print(f"Resultado: {num_a} ^ {num_b} = {num_a ** num_b:.2f}")
print("\nSaliendo...")