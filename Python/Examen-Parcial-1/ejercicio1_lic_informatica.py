num = int(input("Ingrese hasta que número imprimir: "))
i = 1

while i <= num:
    #La condición evalua si 'i' es divisible entre 3 o 5 y su residuo '0'
    if i % 3 == 0 and i % 5 == 0:
        print("Licenciatura en informática", end="\n")
    # La condición evalua si 'i' es divisible entre 3 y su residuo '0'
    elif i % 3 == 0:
        print("Licenciatura", end=", ")
    # La condición evalua si 'i' es divisible entre 5 y su residuo '0'
    elif i % 5 == 0:
        print("Informática", end=", ")
    # Si ninguna de las 3 condiciones anteriores se cumplieron,
    # se imprime el valor que tenga 'i' en ese momento.
    else:
        print(i,end=" ")
    i += 1