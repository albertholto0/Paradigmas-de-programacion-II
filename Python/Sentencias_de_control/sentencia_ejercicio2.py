"""
Nombre: Albert Alexis Contreras Mendoza
Fecha: 23 de octubre del 2024
Descripción: Programa que determina la estación del año
"""

print("+ - - - Estaciones del año - - - +")
estacion = ""
num_mes = int(input("Ingresa el número de mes: "))

# Verifica en qué rango cae el número del mes para determinar la estación correspondiente
if num_mes >= 3 and num_mes <= 5:
    estacion = "Primavera"  # Si el mes está entre marzo (3) y mayo (5), la estación es Primavera
elif num_mes >= 6 and num_mes <= 8:
    estacion = "Verano"     # Si el mes está entre junio (6) y agosto (8), la estación es Verano
elif num_mes >= 9 and num_mes <= 11:
    estacion = "Otoño"      # Si el mes está entre septiembre (9) y noviembre (11), la estación es Otoño
elif num_mes >= 1 and num_mes <= 2 or num_mes == 12:
    estacion = "Invierno"   # Si el mes es enero (1), febrero (2) o diciembre (12), la estación es Invierno
else:
    # Si el número ingresado no corresponde a ningún mes válido, muestra un mensaje de error
    estacion = "Error. Ingrese un mes válido!!!"

# Imprime el resultado con la estación correspondiente o el mensaje de error
print(f"La estación es: {estacion}")