"""
Nombre:Albert Alexis Contreras Mendoza
Fecha: 17 de Octubre del 2024
Descripción:Ejemplos de uso de los operadores aritméticos.
"""
"""
Los operadores aritméticos en Python son los siguientes:
- Suma (+).
- Resta (-).
- Multiplicación (*).
- División (/).
- División entera (//).
- Módulo (%).
- Exponenciación (**).
"""

# Se solicitan dos números enteros al usuario.
numero1 = int(input("Ingresa un número entero: "))
numero2 = int(input("Ingresa otro número entero: "))

# Se realizan las operaciones aritméticas.
print("\n  ***   Ejemplos de uso de los operadores aritméticos   ***")

print(f"La suma de ({numero1} + {numero2}) es: {numero1 + numero2}")
print(f"La resta de ({numero1} - {numero2}) es: {numero1 - numero2}")
print(f"La multiplicación de ({numero1} * {numero2}) es: {numero1 * numero2}")
# Muestra la división de los dos números ingresados, con el resultado mostrado con dos decimales.
print(f"La división de ({numero1} / {numero2}) es: {(numero1 / numero2):.2f}")
# Muestra la división entera de los dos números ingresados, donde el resultado es el cociente sin los decimales.
print(f"La división entera de ({numero1} // {numero2}) es: {numero1 // numero2}")
# Muestra el módulo de los dos números ingresados, es decir, el residuo de la división.
print(f"El módulo de ({numero1} % {numero2}) es: {numero1 % numero2}")
# Muestra la exponenciación, donde el primer número es elevado a la potencia del segundo número.
print(f"La exponenciación  de ({numero1} ** {numero2}) es: {numero1 ** numero2}")
