flag = 1

while flag != 0:
    print("+ - - PROGRAMA QUE CALCULA ÁREA Y PERIMETRO - - +")
    print("1) Calcular el área de un rectángulo")
    print("2) Calcular el perímetro de un rectángulo")
    print("3) Calcular el área de un círculo")
    print("4) Calcular el perímetro de un círculo")
    print("0) Salir")

    op = int(input("Ingrese una opción: "))

    if op == 1:
        print("+ - - CALCULAR ÁREA DE UN RECTÁNGULO - - +")
        base = float(input("Ingrese [base]: "))
        altura = float(input("Ingrese [altura]: "))
        print(f"El area resultante es: {base * altura}")
    elif op == 2:
        print("+ - - CALCULAR PERÍMETRO DE UN RECTÁNGULO - - +")
        base = float(input("Ingrese [base]: "))
        altura = float(input("Ingrese [altura]: "))
        print(f"El perimetro resultante es: {base + altura + base + altura}")
    elif op == 3:
        print("+ - - CALCULAR ÁREA DE UN CÍRCULO - - +")
        radio = float(input("Ingrese [radio]: "))
        print(f"El area resultante es: {(radio ** 2) * 3.1416}")
    elif op == 4:
        print("+ - - CALCULAR PERÍMETRO DE UN CÍRCULO - - +")
        radio = float(input("Ingrese [radio]: "))
        print(f"El perimetro resultante es: {radio * 2 * 3.1416}")
    elif op == 0:
        flag = 0
    else:
        print("Opción no válida")
    print("\n - - - - - - - -")