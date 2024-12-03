"""
Nombre: Albert Alexis Contreras Mendoza
Fecha: 29 de Octubre del 2024
Descripción: Uso del ciclo for.
"""
"""
El ciclo for se utiliza para iterar sobre una secuencia (como una lista, tupla o cadena) y ejecutar un bloque de código 
para cada elemento de esa secuencia.

Sintaxis:

for variable in secuencia:
    # Código a ejecutar con el valor de la variable dentro de la secuencia.

# Nota: Nuevamente, no hay llaves, sino que se deja un espacio. 
"""
# Ejemplo del ciclo for
# Título del programa.
print("+ - - Ciclo for - - +")
print()  # Imprime una línea en blanco.

frase = input("Ingresa una frase: ")

for caracter in frase:
    print(caracter, end = "-")
print("\nFIN DE CADENA")

# Otro ejemplo con el ciclo for. Imprime los alumnos
print() # Imprime espacio en blanco.
alumnos = ["Albert", "Kevin", "Elton", "Diana", "Rosendo", "Amelia", "Sergio"]
for alumno in alumnos:
    print(f"Hola {alumno}")