'''
Nombre: Albert Alexis Contreras Mendoza
Fecha: 15 de octubre del 2024
Descripción: Conversión de cadenas a int, float y boolean mediante la interacción con consola.
'''

# Las funciones anidadas se usan para convertir la entrada del usuario al tipo de dato necesario.
print("****   Datos de los alumnos    *****")
nombre = input("Ingresa el nombre: ")
semestre = int(input("Ingresa el no. de semestre: "))
promedio = float(input("Ingresa el promedio: "))
es_mujer = input("¿Es mujer (Si/No)?: ")

# No es posible convertir directamente una cadena a un valor booleano.
# Por ello, utilizamos la misma variable, convertimos a  minúsculas y lo comparamos con la cadena "si".
es_mujer = es_mujer.lower() == "si"

# Se imprimen los datos del alumno.
# {promedio:.2f} redondea el promedio a 2 decimales para mostrar solo dos cifras después del punto decimal
"""
Si promedio = 8.56789, muestra 8.57 porque se redondea a dos decimales
Si promedio = 7.0, muestra 7.00
Si promedio = 9.234,muestra 9.23 porque se trunca a dos decimales.
"""
print()
print(f"El alumno {nombre} cursa el {semestre} semestre con un promedio de {promedio:.2f}. Además, es mujer: {es_mujer}.")