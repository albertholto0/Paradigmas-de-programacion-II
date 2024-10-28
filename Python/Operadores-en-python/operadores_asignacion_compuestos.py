"""
Nombre: Albert Alexis Contreras Mendoza
Fecha: 17 de Octubre del 2024
Descripción: Ejemplos de uso de los operadores de asignación compuestos.
"""
"""
Los operadores de asignación compuestos son una forma abreviada de realizar una operación aritmética y una asignación
en una sola línea de código. Combinan un operador aritmético (como suma, resta, multiplicación, división, etc.) 
con el operador de asignación (=).
"""

# Se solicita un número para realizar diferentes operaciones de asignación compuestas.
numero = int(input("Ingresa un número: "))
print(f"Valor ingresado: {numero}")

numero+=20      # equivale a numero = numero + 20
print(f"Nuevo valor (+20): {numero}")

numero-=4       # equivale a numero = numero - 4
print(f"Nuevo valor (-4): {numero}")

numero*=2       # equivale a numero = numero * 2
print(f"Nuevo valor (*2): {numero}")

numero/=5       # equivale a numero = numero / 5
print(f"Nuevo valor (/5): {numero:.2f}")

# Ejemplo. ¿Qué se obtiene cuando los números ingresados son 8 y 7?

numero1 = int(input("Ingresa un número: "))
numero2 = int(input("Ingresa otro número: "))

numero1 += numero2
numero1 += 2
numero1 *= 5
numero2 -= 3
numero1 /= numero2
# Se realizan una serie de operaciones de asignación compuestas sobre 'numero1' y 'numero2':
# - 'numero1' se incrementa en el valor de 'numero2'.
# - Luego, 'numero1' se incrementa en 2.
# - 'numero1' se multiplica por 5.
# - 'numero2' se decrementa en 3.
# - Finalmente, 'numero1' se divide por el valor actualizado de 'numero2'.

print(f"Resultado de las operaciones sobre el primer número: {numero1}")
print(f"Resultado de las operaciones sobre el segundo número: {numero2}")