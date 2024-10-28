"""
Nombre: Albert Alexis Contreras Mendoza
Fecha: 24 de Octubre del 2024
Descripción: Aplicación que simula el funcionamiento de una cuenta bancaria
"""

flag = 1
# Inicializar el saldo de la cuenta bancaria
saldo = 0.0

while flag != 0:
    print("- - - BIENVENIDO a Banco Azteca - - -")
    print("1. Consulta tu saldo")
    print("2. Ingresar dinero")
    print("3. Retirar dinero")
    print("0. Salir")

    op = int(input("[OP]: "))

    if op == 1:
        print(f"Tu saldo es de ${saldo}")
    elif op == 2:
        dinero_ingresado = float(input("Ingrese cantidad: "))  # Solicita la cantidad a ingresar
        saldo += dinero_ingresado  # Actualiza el saldo sumando el dinero ingresado
        print(f"Saldo actual: ${saldo}")
    elif op == 3:
        dinero_ingresado = float(input("Ingrese cantidad: "))  # Solicita la cantidad a retirar
        saldo -= dinero_ingresado  # Actualiza el saldo restando el dinero retirado
        print(f"Saldo actual: ${saldo}")
    elif op == 0:
        flag = 0  # Cambia el flag a 0 para finalizar el ciclo
    else:
        print("Opcion no valida...")
