"""
Nombre: Albert Alexis Contreras Mendoza
Fecha: 23 de octubre del 2024
Descripción: Sentencia if-elif-else
"""
"""
La sentencia elif es una extensión del if-else y permite evaluar múltiples condiciones de forma secuencial. 
Es como tener varias opciones a elegir, ejecutándose el bloque de código correspondiente a la primera condición 
que sea verdadera.

Sintaxis:

if condicion_1:
    # Código a ejecutar si la condición_1 es verdadera.

elif condición_2:
    # Código a ejecutar si la condición_2 es verdadera.
  .
  .
else:
    # Código que se ejecuta si todas las condiciones fueron falsas.
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
###############################################
"""
MODO DEPURACIÓN (DEBUG)

Utilizar ahora el modo depuración.
1) Crear un punto de ruptura en la variable edad. Marcar el número de línea y se pondrá un círculo color rojo.
2) Clic derecho y ejecutar el modo Debug.
3) Observar la nueva pantalla e ir ejecutando paso-a-paso (step over) F8.
4) Observar el comportamiento.
"""