"""
14 de noviembre del 2024
Conjuntos
    mutables
    desordenados
"""

# Conjunto vacío
conjunto1 = set()
conjunto2 = {10,5,24,11,8,7,21,9}
print(conjunto2)

# Añadir elementos
conjunto1.add(80)
conjunto1.add(111)
conjunto1.add(10)
conjunto1.add(5)
conjunto1.add(24)
print(conjunto1)
conjunto1.add(80)
print(conjunto1)

conjunto1.remove(111)
# conjunto1.remove(111) # Error si no existe
print(conjunto1)
conjunto1.discard(10)
conjunto1.discard(111)
print(conjunto1)

# Unión
conjunto_union = conjunto1 | conjunto2
print(f"[Conjunto unión]: {conjunto_union}")
# Intersección
conjunto_interseccion = conjunto1 & conjunto2
print(f"[Conjunto intersección]: {conjunto_interseccion}")
# Resta de conjuntos
# Borra al conjunto 1 y a los elementos que pertenecen a ambos conjuntos
resta_conjuntos = conjunto2 - conjunto1
print(f"[Resta de conjuntos]: {resta_conjuntos}")

alumnos_lista = ['albert','kevin','elton','diana','rosendo','amelia','sergio','elton']
alumnos_conjunto = set(alumnos_lista)
print(f"[Alumnos lista]: {alumnos_lista}\n"
      f"[Alumnos conjunto]: {alumnos_conjunto}")

nombre = input("Ingresa un nombre: ")
# strip() elimina los espacios que hay al inicio y al final
nombre = nombre.strip().lower()

if nombre in alumnos_conjunto:
    print("Se encuentra en el conjunto")
else:
    print("Se añadió al conjunto")
alumnos_conjunto.add(nombre)