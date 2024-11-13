"""
Albert Alexis Contreras Mendoza
13 de noviembre del 2024
Muestra el promedio del semestre de las cuatro calificaciones
"""

def calcular_promedios(c1, c2, c3, ordinario):
    promedio_parcial = (c1 + c2 + c3) / 3
    promedio_final = (promedio_parcial + ordinario) / 2
    return promedio_parcial, promedio_final


calif_p1 = float(input("Calificación parcial 1: "))
calif_p2 = float(input("Calificación parcial 2: "))
calif_p3 = float(input("Calificación parcial 3: "))
calif_or = float(input("Calificación ordinario: "))

promedios_finales = calcular_promedios(calif_p1, calif_p2, calif_p3, calif_or)

print(f"\nParcial 1: {calif_p1:.1}"
      f"\nParcial 2: {calif_p2:.1}"
      f"\nParcial 3: {calif_p3:.1}"
      f"\nOrdinario: {calif_or:.1}"
      f"\n-----\n"
      f"El promedio final del parcial es: {promedios_finales[0]:.1}"
      f"\nEl promedio final es: {promedios_finales[1]:.1}")