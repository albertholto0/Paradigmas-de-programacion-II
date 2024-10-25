"""
bonificacion buen fin
cantidad gastada:
la compra fue a MSI?
aplica bonificacion de BF: T/F
"""
print("*** Bonificación buen fin ***")
cantidad = float(input("Cantidad gastada: "))
cantidadComprobacion = bool(cantidad > 5000)
compraMSI = input("¿La compra fue a meses sin intereses?: ")
compraMSI = compraMSI.lower() == "si"

print(f"¿Aplica bonificación de buen fin?: {cantidadComprobacion and compraMSI}")