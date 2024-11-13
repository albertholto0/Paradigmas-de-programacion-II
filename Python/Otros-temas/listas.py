""""
Albert Alexis Contreras Mendoza
11 de noviembre del 2024
Listas. Principios

Colecciones
    -> Listas
    -> Tuplas
    -> Conjuntos
    -> Diccionarios
Listas
    -> Ordenada
    -> Mutable
    -> Heterogenea
"""
# Lista
alumnos = ["Amelia","Albert"]
print(alumnos)
alumnos.append("kevin")
# Añade un elemento al final de la lista
print(alumnos)
alumnos.append("Diana")
# Añade un elemento en un índice específico
alumnos.insert(3,"Elton")
print(alumnos)
alumnos.insert(4,"Magdiel")
alumnos.append("Edén")
alumnos.append("Sergio")
print(alumnos)
alumnos.insert(7,"Magdiel")
alumnos.append("Magdiel")
print(alumnos)
# Borra un elemento por su 'valor'
alumnos.remove("Magdiel")
print(alumnos)
# Borra un elemento por su 'Índice'
alumnos.pop(6)
print(alumnos)
# Otra manera de eliminar por índice
del alumnos[7]
print(alumnos)
"""
Funciones comunes
-> len() #Convierte a minusculos
-> sort() #Ordena
-> sort(reverse = True) #Ordena pero al revés
"""