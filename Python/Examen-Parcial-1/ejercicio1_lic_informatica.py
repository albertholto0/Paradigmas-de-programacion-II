num = int(input("Ingrese hasta que número imprimir: "))
i = 1

while i <= num:
    if i % 3 == 0 and i % 5 == 0:
        print("Licenciatura en informática", end=" ")
    elif i % 3 == 0:
        print("Licenciatura", end=" ")
    elif i % 5 == 0:
        print("Informática", end=" ")
    else:
        print(i,end=" ")
    i += 1