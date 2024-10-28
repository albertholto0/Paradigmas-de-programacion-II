"""
Nombre: Albert Alexis Contreras Mendoza
Fecha: 20 de Octubre del 2024
Descripción: Este programa determinará True o False de acuerdo a la expresión (exp1 O exp2) Y (exp3 O exp4).
"""
print("+ - - EXPRESIÓN BOOLEANA (EXP1 O EXP2) y (EXP3 O EXP4) - - +")
# Solicita cuatro entradas booleanas
v1 = input("Expresión booleana 1: ")
v2 = input("Expresión booleana 2: ")
v3 = input("Expresión booleana 3: ")
v4 = input("Expresión booleana 4: ")
# Convierte las entradas a valores booleanos, siendo verdadero si el usuario ingresó "v".
v1 = v1.lower() == "v"
v2 = v2.lower() == "v"
v3 = v3.lower() == "v"
v4 = v4.lower() == "v"
# Calcula el resultado de las operaciones OR para los pares de expresiones.
or_uno = v1 or v2
or_dos = v3 or v4
# Calcula el resultado de las operaciones OR para los pares de expresiones.
expresion_final = or_uno and or_dos
print(f"El resultado de la expresión booleana es: {expresion_final}")
# Muestra el resultado de la expresión booleana.
