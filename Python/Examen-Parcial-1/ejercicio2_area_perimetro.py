# Una bandera. El programa funcionará siempre y cuando la bandera tenga el valor de '1'
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
        print(f"El area resultante es: {base * altura:.3f}")
    elif op == 2:
        print("+ - - CALCULAR PERÍMETRO DE UN RECTÁNGULO - - +")
        base = float(input("Ingrese [base]: "))
        altura = float(input("Ingrese [altura]: "))
        print(f"El perimetro resultante es: {(2 * base + 2 * altura):.3f}")
    elif op == 3:
        print("+ - - CALCULAR ÁREA DE UN CÍRCULO - - +")
        radio = float(input("Ingrese [radio]: "))
        print(f"El area resultante es: {(radio ** 2) * 3.1416:.3f}")
    elif op == 4:
        print("+ - - CALCULAR PERÍMETRO DE UN CÍRCULO - - +")
        radio = float(input("Ingrese [radio]: "))
        print(f"El perimetro resultante es: {radio * 2 * 3.1416:.3f}")
    elif op == 0:
        # Si el usuario ingresa '0' (donde el menú dice que 0 es para salir),
        # la bandera toma el valor de '0', por lo tanto el programa no puede seguir funcionando
        # y termina
        flag = 0
    else:
        print("Opción no válida")
    print("\n - - - - - - - -")