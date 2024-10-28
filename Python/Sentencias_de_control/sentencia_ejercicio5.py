"""
Nombre: Albert Alexis Contreras Mendoza
Fecha: 23 de octubre del 2024
Descripción: Este programa determina el promedio de una materia e indica si el alumno aprobó o no.
"""

print("+ - - PROGRAMA PARA CALCULAR EL PROMEDIO DE UNA MATERIA - - +")
# Solicita las calificaciones de los tres parciales y del examen ordinario.
calif_p1 = float(input("Calificación [Parcial 1]: "))
calif_p2 = float(input("Calificación [Parcial 2]: "))
calif_p3 = float(input("Calificación [Parcial 3]: "))
calif_or = float(input("Calificación [Ordinario]: "))

# Calcula el promedio ponderado, asignando un 50% al promedio de los parciales y 50% al ordinario.
promedio = ((calif_p1 + calif_p2 + calif_p3) / 3) * 0.5 + calif_or * 0.5

# Verifica si el promedio es mayor o igual a 6 para determinar si el alumno aprobó.
if promedio >= 6:
    print(f"La calificación final es de {promedio:.1f}. ¡Felicidades! Aprobaste :)")
else:
    print(f"La calificación final es de {promedio:.1f}. ¿Has pensado en cambiarte de carrera?")
