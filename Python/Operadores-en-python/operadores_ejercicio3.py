"""
Nombre: Albert Alexis Contreras Mendoza
Fecha: 20 de Octubre del 2024
Descripción: Este programa determinará si un usuario se autentifica correctamente con su usuario y contraseña.
"""
# Contraseñas constantes para la autenticación.
usuarioConstante = "beto19"
contraseniaConstante = "CharmandeR"

print("+ - - SISTEMA DE AUTENTIFICACIÓN - - +")

# Solicita al usuario que ingrese sus contraseñas.
usuario = input("Ingresa tu usuario: ")
contrasenia = input("Ingresa tu contraseña: ")

# Verifica si las contraseñas ingresadas coinciden con las predefinidas y muestra si el acceso es válido.
print(f"\nEl acceso es correcto: {usuarioConstante == usuario and contraseniaConstante == contrasenia}")
