"""
Nombre: Albert Alexis Contreras Mendoza
Fecha: 14 de noviembre del 2024
Descripción: Conjuntos
"""
# Se crean dos conjuntos de números.
print("Se crean dos conjuntos.")

conjuntoA = {2, 223, 12, 1, 3, 4, 1, 6}    # Notar que el conjunto intenta repetir 2 veces el no. 1.
conjuntoB = {12, 23, 0, 6, 30, 4, 10}

print(f"Conjunto A: {conjuntoA}")
print(f"Conjunto B: {conjuntoB}")
print()

# Operaciones básicas.
print("Operaciones básicas.")

union = conjuntoA | conjuntoB
print(f"Unión de los conjuntos (|): {union}")   # La unión omite los valores repetidos en ambos conjuntos.

interseccion = conjuntoA & conjuntoB
print(f"Intersección de los conjuntos (&): {interseccion}") # Son los valores que coinciden en ambos conjuntos.

diferencia = conjuntoA - conjuntoB
print(f"Resta de los conjuntos: {diferencia}")  # Son los valores del conjunto A menos los que coincidente con el conjunto B.
print()

# Convertir de lista a conjunto y viceversa.
print("Convertir de lista a conjunto y viceversa.")

lista = ["Perro", "Gato", "Ratón", "Cuyo", "Gato", "Lobo", "Perro"]
print(f"Lista original: {lista}")

conjunto = set(lista)
print(f"Lista como conjunto: {conjunto}")      # No considera los valores repetidos.

lista_reconvertida = list(conjunto)
print(f"Lista reconvertida del conjunto: {lista_reconvertida}")
