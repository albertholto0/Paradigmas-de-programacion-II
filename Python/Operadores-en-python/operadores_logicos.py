"""
Nombre: Albert Alexis Contreras Mendoza
Fecha: 18 de Octubre del 2024
Descripción: Ejemplos de uso de los operadores relacionales.
"""

"""
Los operadores lógicos permiten combinar expresiones booleanas (verdadero o falso) para crear condiciones más complejas.
Estos operadores nos permiten realizar operaciones lógicas como "y", "o" y "no", lo que nos da la capacidad de tomar 
decisiones más sofisticadas dentro de nuestros programas.
"""

# Se solicita por consola que se ingresen dos valores (Si/No) para covnertirlas a expresiones booleanas.
p = input("p = ingresa si/no: ")
p = p.lower() == "si"

# Las cadenas se convierten a expresiones booleanas (ver Fundamentos-Python -> Entrada_conversiones.py).
q = input("q = ingresa si/no: ")
q = q.lower() == "si"

# Se imprimen mensajes sobre operaciones lógicas.
print(f"p and q: {p and q}")
print(f"p or q: {p or q}")
print(f"not p: {not p}")
print(f"not q: {not q}")
