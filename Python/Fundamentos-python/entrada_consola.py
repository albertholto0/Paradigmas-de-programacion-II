'''
Nombre: Albert Alexis Contreras Mendoza
Fecha: 15 de octubre del 2024
Descripción: Entrada de datos por consola para interactuar con el usuario con valores dinámicos.
'''

#La función input() obtiene una entrada de texto del usuario.
numero1_cadena = input("Introduce un número decimal: ")
numero2_cadena = input("Introduce otro número decimal: ")

#Al sumar cadenas, los valores se concatenan (se unen como texto).
resultado_cadena = numero1_cadena + numero2_cadena
print()
print(" ****  Recibir número sin un casting de variables  ****")
print(f"El resultado de {numero1_cadena} y {numero2_cadena} es: {resultado_cadena}")

#El casting convierte las cadenas a números decimales para realizar operaciones matemáticas.
numero1_float = float(numero1_cadena)
numero2_float = float(numero2_cadena)

#Aquí, la suma es matemática porque las variables son de tipo float.
resultado_float = numero1_float + numero2_float
print()
print(" ****  Casting de variables  ****")
print(f"El resultado de {numero1_float} y {numero2_float} es: {resultado_float}")
