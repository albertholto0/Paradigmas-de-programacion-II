#Contreras Mendoza Albert

# Título del programa.
print("+ - - Ciclo for - - +")
print()  # Imprime una línea en blanco.

frase = input("Ingresa una frase: ")

for caracter in frase:
    print(caracter, end = "-")
print("\nFIN DE CADENA")

print() # Imprime espacio en blanco.
alumnos = ["Albert", "Kevin", "Elton", "Diana", "Rosendo", "Amelia", "Sergio"]
for alumno in alumnos:
    print(f"Hola {alumno}")