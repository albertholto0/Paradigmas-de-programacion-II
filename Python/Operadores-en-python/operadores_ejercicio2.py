"""
Nombre: Albert Alexis Contreras Mendoza
Fecha: 19 de Octubre del 2024
Descripción: Este programa determinara si una persona forma parte de la comunidad de la UNSIJ.
"""
print("+ - - COMUNIDAD UNSIJ - - +")
profesor = input("¿Eres profesor de la UNSIJ? [si/no]: ")
alumno = input("¿Eres alumno de la UNSIJ? [si/no]: ")
# Se preguntan dos veces al usuario si es profesor o alumno de la UNSIJ.

esProfesor = profesor.lower() == "si"
esAlumno = alumno.lower() == "si"
# Se convierten las respuestas a minúsculas y se comparan con "si" para ver si son verdaderas.

print(f"\nLa persona forma parte de la comunidad UNSIJ: {esProfesor or esAlumno}")
# Determina si la persona pertenece a la comunidad UNSIJ verificando si cumple alguna de las dos condiciones.
