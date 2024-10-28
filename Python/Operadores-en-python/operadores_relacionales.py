"""
Nombre: Albert Alexis Contreras Mendoza
Fecha: 18 de Octubre del 2024
Descripción: Ejemplos de uso de los operadores relacionales.
"""

"""
Los operadores relacionales son símbolos que se utilizan en programación para comparar dos valores. 
Estos operadores devuelven un valor booleano (verdadero o falso) dependiendo del resultado de la comparación. 
Son fundamentales para tomar decisiones dentro de un programa, ya que permiten construir expresiones condicionales 
que determinan el flujo de ejecución.

Operadores Relacionales Comunes:
Operador	Significado
==	Igual a
!=	Diferente de
>	Mayor que
<	Menor que
>=	Mayor o igual que
<=	Menor o igual que
"""

# Se solicitan dos números para realizar distintas operaciones relacionales.
num_a = float(input("Ingresa un numero: "))
num_b = float(input("Ingresa otro: "))

comprobacion = num_a > num_b
print(f"¿El número {num_a} es mayor que {num_b}?: {comprobacion}")
comprobacion = num_a >= num_b
print(f"¿El número {num_a} es mayor o igual que {num_b}?: {comprobacion}")
comprobacion = num_a < num_b
print(f"¿El número {num_a} es menor que {num_b}?: {comprobacion}")
comprobacion = num_a <= num_b
print(f"¿El número {num_a} es menor o igual que {num_b}?: {comprobacion}")
comprobacion = num_a == num_b
print(f"¿El número {num_a} es igual que {num_b}?: {comprobacion}")
comprobacion = num_a != num_b
print(f"¿El número {num_a} es distinto que {num_b}?: {comprobacion}")
