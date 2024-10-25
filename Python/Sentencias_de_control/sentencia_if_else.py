"""
Nombre: Albert Alexis Contreras Mendoza
Fecha: 23 de octubre del 2024
Descripción: Sentencia if-else

Sintaxis:
    if conficion:
        # Código si la condicion es verdadera
    else
        # Código si la condicion es falsa
"""
print(" - - - Núm. PAR O IMPAR ¿? - - -")
n = int(input("Ingrese un número entero: "))

if n % 2 == 0:
    print("Es par")
else:
    print("NO es par")