# Convert number to reversed array of digits

def separar(n):
    lista = []
    if n == 0:
        lista.append(0)
        return lista
    else:
        while n != 0:
            digito = n % 10
            lista.append(digito)
            n = n // 10
        return lista

numero = int(input("[Número]: "))
print(separar(numero))

