"""
Nombre: Albert Alexis Contreras Mendoza
Fecha: 19 de Octubre del 2024
Descripción: Este programa determina si el usuario aplica para una bonificación.
"""

print("*** Bonificación buen fin ***")
cantidad = float(input("Cantidad gastada: "))
# Se obtiene la cantidad gastada y se convierte a un número decimal.
cantidadComprobacion = bool(cantidad > 5000)
# Se verifica si la cantidad es mayor a 5000 para determinar si cumple con ese requisito.
compraMSI = input("¿La compra fue a meses sin intereses?: ")
compraMSI = compraMSI.lower() == "si"
# Convierte la respuesta a minúsculas y verifica si es "si" para determinar si la compra fue a meses sin intereses.
print(f"¿Aplica bonificación de buen fin?: {cantidadComprobacion and compraMSI}")
# Muestra si aplica la bonificación comprobando que ambos requisitos sean verdaderos.
