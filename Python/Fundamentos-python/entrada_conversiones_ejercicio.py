"""
Nombre: Albert Alexis Contreras Mendoza
Fecha: 15 de octubre del 2024
Descripción: Ejercicio aplicando los conocimientos de la lección <<entrada-conversiones>>

Escribe un programa que realice lo siguiente:
a) Pida los datos de los profesores utilizando nombres de variables adecuadas, la función input y el casting:
    Nombre (cadena).
    No. de cubículo (int).
    Horas que imparte clase a la semana (float con 3 decimales).
    ¿Tiene más de 5 años en la UNSIJ? (booleano).
b) Muestre los datos en consola de forma adecuada.

Nota: Asuma que el usuario siempre va a ingresar números cuando se requiera.
"""

# Solicita el nombre del profesor (cadena de texto).
nombre = input("Ingrese nombre: ")
# Solicita el número de cubículo y lo convierte a un número entero.
num_cubiculo = int(input("Ingrese su número de cubículo: "))
# Solicita las horas de clase a la semana y las convierte a un número decimal.
horas_chamba = float(input("Ingrese horas que imparte a la semana: "))
# Solicita si el profesor tiene más de 5 años en la UNSIJ.
es_antiguo = input("¿Tiene más de 5 años en la UNSIJ? [si/no]: ")

# Convierte la respuesta a minúsculas y verifica si es "si" para convertirlo a un valor booleano.
es_antiguo = es_antiguo.lower() == "si"

# Muestra los datos ingresados en un formato adecuado.
print(f"El/la docente {nombre} está en el cubículo {num_cubiculo} y trabaja {horas_chamba} hrs por semana. Además, es {es_antiguo} que lleva más de 5 años en la UNSIJ.")
