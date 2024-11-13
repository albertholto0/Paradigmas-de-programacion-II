n = int(input("Ingresa alto de piramide: "))
asterisco = "*"
espacio = " "

for i in range(1, n + 1):
    asteriscos = asterisco* i
    print(f"{asteriscos}")
print("")
for i in range(0,n + 1):
    asteriscos = asterisco * (n-i)
    print(f"{asteriscos}")
for i in range (1, n + 1):
    espacios = espacio * (n - i)
    asteriscos = asterisco * (2 * i - 1)
    print(f"{espacios}{asteriscos}")
print("")
for i in range(1, n + 1):
    asteriscos = asterisco * i
    espacios = espacio * (n-i)
    print(f"{espacios}{asteriscos}")

