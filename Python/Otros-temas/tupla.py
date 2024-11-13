"""
Albert Alexis Contreras Mendoza
13 de Noviembre del 2024
Tuplas
    Para la creación de tuplas se usan parentesis
"""

calificaciones_parcial1 = (9.6, 6.3, 6.0, 8.7, 5.0)
poo,bd,redes,arq,ings = calificaciones_parcial1
print(calificaciones_parcial1)

for calicacion in calificaciones_parcial1:
    print(calicacion,end = " ")

promedio_parcial1 = sum(calificaciones_parcial1)/len(calificaciones_parcial1)
print("\n",promedio_parcial1)

