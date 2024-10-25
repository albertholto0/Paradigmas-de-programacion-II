"""
Nombre: Albert Alexis Contreras Mendoza
Fecha: 23 de octubre del 2024
Descripción: Sentencia if-elif-else
"""
print("- - - Grupo de edad - - -")
edad = int(input("Ingresa edad: "))

if edad < 15:
    print("Eres niño o adolescente")
elif edad >= 15 and edad <= 24:
    print("Eres un joven")
elif edad >= 25 and edad <= 44:
    print("Eres un adulto joven")
elif edad >= 45 and edad <= 60:
    print("Eres un adulto maduro")
elif edad > 60:
    print("Eres un adulto mayor")