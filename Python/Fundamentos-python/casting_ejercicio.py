"""
Albert Alexis Contreras Mendoza
14 de Octubre del 2024
Ejercicio aplicando los conocimientos vistos en la lección "Casting en python"
    Instrucciones:
    Realiza un programa de nombre Casting_ejercicio.py que realice lo siguiente:
    a) Convierta los siguientes números en cadenas: 3.14159265, 12, 0.
    b) De los números anteriores, indica su valor booleano.
    c) Convierta las siguientes cadenas a números: "10002", "100.02", "0".
    d) De las cadenas anteriores, indica su valor booleano. Nota: especificar por qué el resultado de la cadena "0".
"""
#Definición de números
num_a = 3.14159265
num_b = 12
num_c = 0

#Impresión de los números
print("*** Números ***")
print("Numero a: ", num_a)
print("Numero b: ", num_b)
print("Numero c: ", num_c)

#Conversion de números a cadenas
'''
La función str() en Python convierte cualquier tipo de dato en su representación como cadena (string).
Esta operación es útil cuando se desea combinar datos numéricos con texto para mostrarlos, o para almacenarlos como texto en una base de datos.
'''
cadena_a = str(num_a)
cadena_b = str(num_b)
cadena_c = str(num_c)


print("+ + + Conversión de números a cadenas + + +")
print("Cadena a: ", cadena_a)
print("Cadena b: ", cadena_b)
print("Cadena c: ", cadena_c)

#Evaluaciones de los valores booleanos de los números
'''
En Python, todos los números diferentes de cero se consideran "True" cuando se convierten a un valor booleano.
El número cero (0) es la única excepción y se considera "False". Esta regla se aplica tanto a enteros como a flotantes.
'''

print("--- Valores booleanos ---")
es_verdadero = bool(num_a)
print(f"¿El valor de {num_a} es verdadero? {es_verdadero}")
es_verdadero = bool(num_b)
print(f"¿El valor de {num_b} es verdadero? {es_verdadero}")
es_verdadero = bool(num_c)
print(f"¿El valor de {num_c} es verdadero? {es_verdadero}")

#Conversión de cadenas a números
'''
Las funciones int() y float() permiten convertir cadenas que contienen números en sus correspondientes tipos numéricos.
Es importante que la cadena represente un valor numérico válido, de lo contrario, se producirá un error.
'''
cadena_aa = "10002"     #Cadena que representa un número entero
cadena_bb = "100.02"    #Cadena que representa un número flotante
cadena_cc = "0"         #Cadena que representa el número cero

num_aa = int(cadena_aa)
num_bb = float(cadena_bb)
num_cc = int(cadena_cc)

print("+++ Conversion de cadena a número +++")
print("Número a: ", num_aa)
print("Número b: ", num_bb)
print("Número c: ", num_cc)

#Evaluación de los valores booleanos de las cadenas
'''
Cuando se evalúan cadenas en un contexto booleano, cualquier cadena que no esté vacía se considera "True".
Incluso una cadena que contiene "0" se considera "True" porque no está vacía, aunque el valor numérico equivalente sea cero.
Una cadena vacía ("") es la única que se evalúa como "False".
'''

print("- - - Valores booleanos (cadenas) - - -")
es_verdadero = bool(cadena_aa)
print(f"El valor de {cadena_aa} es verdadero? {es_verdadero}")
es_verdadero = bool(cadena_bb)
print(f"El valor de {cadena_bb} es verdadero? {es_verdadero}")
es_verdadero = bool(cadena_cc)
print(f"El valor de {cadena_cc} es verdadero? {es_verdadero}")
'''
El resultado de la cadena '0' es verdadero, porque no está vacía aunque su valor númerico sea cero. 
'''

