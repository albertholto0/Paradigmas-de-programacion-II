"""
Nombre: Albert Alexis Contreras Mendoza
Fecha: 24 de Octubre del 2024
Descripción: Aplicación que simula el funcionamiento de una cuenta bancaria
"""
flag = 1
saldo = 0.0
while flag != 0:
    print("- - - bienVENIDO a Banco Azteca - - -")
    print("1. Consulta tu saldo")
    print("2. Ingresar dinero")
    print("3. Retirar dinero")
    print("0. Salir")

    op = int(input("[OP]: "))

    if op == 1:
        print(f"Tu saldo es de ${saldo}")
    elif op == 2:
        dinero_ingresado = float(input("Ingrese cantidad: "))
        saldo += dinero_ingresado
        print(f"Saldo actual: ${saldo}")
    elif op == 3:
        dinero_ingresado = float(input("Ingrese cantidad: "))
        saldo -= dinero_ingresado
        print(f"Saldo actual: ${saldo}")
    elif op == 0:
        flag = 0
    else:
        print("Opcion no valida...")
