
numero = 8

numero_binario = []

while numero > 0:
    if (numero % 2) == 0:
        numero_binario.append(0)
    else:
        numero_binario.append(1)
    numero //= 2
numero_binario.reverse()
cadena_numero_binario = ""
for i in numero_binario:
    cadena_numero_binario += str(i)
print(cadena_numero_binario)