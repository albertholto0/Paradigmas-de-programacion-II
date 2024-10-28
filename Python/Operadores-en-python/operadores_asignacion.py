"""
Nombre: Albert Alexis Contreras Mendoza
Fecha: 17 de Octubre del 2024
Descripción: Ejemplos de uso de los operadores de asignación.
"""
"""
En programación, las operaciones de asignación se utilizan para almacenar un valor en una variable. 
Es decir, se establece una relación entre un nombre (la variable) y un valor en la memoria de la computadora.
"""

# Asignación múltiple.
print("   ***   Asignación múltiple   ***")
nombre, primer_apellido, segundo_apellido = "albert", "contreras", "mendoza"
print(f"Asignación múltiple de cadenas: {nombre} {primer_apellido} {segundo_apellido}")
# Se asignan varios valores a múltiples variables en una sola línea. En este caso, tres cadenas de texto.

# Asigna dos números enteros a las variables 'entero1' y 'entero2'.
entero1, entero2 = 1, 2
print(f"Asignación múltiple de enteros: {entero1} y {entero2}")

# Asigna varios valores decimales a las variables correspondientes.
decimal1, decimal2, decimal3, decimal4 = 3.14, 3.1416, 3.14159, 3.141592
print(f"Asignación múltiple de decimales: {decimal1}, {decimal2}, {decimal3} y {decimal4}")

# Demuestra que es posible asignar diferentes tipos de datos (cadena, entero y decimal) en una misma instrucción.
nombre, entero1, decimal4 = "Albert", 12, 3.1415926
print(f"Asignación múltiple: {nombre}, {entero1} y {decimal4}")

# Muestra que es posible asignar los resultados de operaciones aritméticas a variables en una sola línea.
suma, resta = entero1 + entero2, decimal1 - decimal2
print(f"Asignaciones de operaciones: suma {suma} y resta {resta:.4f}")

# Asignación encadenada.
print("\n  ***   Asignación encadenada   ***")
# Asigna el mismo valor a múltiples variables en una sola instrucción. En este caso, se asigna el valor 10.
entero3 = entero4 = entero5 = 10
print(f"Asignación encadenada de: {entero3} = {entero4} = {entero5} = 10")

# Intercambio de variables.
print("\n  ***   Intercambio de variables   ***")
entero5, entero6 = 5, 6
print(f"Valores asignados: entero5 = {entero5} y entero6 = {entero6}")
# Intercambia los valores de dos variables, utilizando la asignación simultánea.
entero6, entero5 = entero5, entero6
print(f"Valores intercambiados: entero5 = {entero5} y entero6 = {entero6}")

variable_prueba1, variable_prueba2 = 100, "Hola mundo"
variable_prueba1, variable_prueba2 = variable_prueba2, variable_prueba1
# Demuestra que el intercambio de variables también es posible con diferentes tipos de datos,
# ya que Python permite el uso dinámico de tipos de variables.
print(f"Valores asignados: variable_prueba1 = {variable_prueba1} y variable_prueba2 = {variable_prueba2}")
print(f"Valores intercambiados: variable_prueba1 = {variable_prueba1} y variable_prueba2 = {variable_prueba2}")