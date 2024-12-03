"""
Nombre: Albert Alexis Contreras Mendoza
Fecha: 2 de diciembre del 2024
Descripción: Programa que realiza la función de una calculadora haciendo uso de funciones.
    Este programa es la versión del ejercicio Ciclos_ej3_calculadora.py, pero ahora utilizando funciones.
    Se sigue mostrando el mismo menú:
        1) Suma.
        2) Resta.
        3) Multiplicación.
        4) División.
        5) División entera.
        6) Exponenciación.
        0) Salir.
    Cualquier otro caso -> Mostrar un mensaje de "opción no válida".
    Para ello:
        a) En el código a nivel de módulo, utilice el ciclo en donde se está ejecutando el programa.
        b) Defina una función para el menú y devuelva la opción seleccionada por el usuario.
        c) Defina una función en donde los parámetros sean la opción y los números, devolviendo el resultado.
        d) Muestre el resultado en pantalla.
"""
# Nombre: Albert Alexis Contreras Mendoza
# Fecha: 25 de Octubre del 2024
# Descripción: Calculadora con funciones

# Función para mostrar el menú y devolver la opción seleccionada por el usuario
def mostrar_menu():
    print("+ - - Calculadora básica - - +")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. División entera")
    print("6. Exponenciación")
    print("0. Salir")
    return int(input("[OP]: "))

# Función para realizar la operación seleccionada por el usuario. Todas las operaciones devuelven el resultado con dos decimales
def calcular(opcion, num_a, num_b):
    if opcion == 1:
        return f"Resultado: {num_a} + {num_b} = {num_a + num_b:.2f}"    # Suma
    elif opcion == 2:
        return f"Resultado: {num_a} - {num_b} = {num_a - num_b:.2f}"    # Resta
    elif opcion == 3:
        return f"Resultado: {num_a} * {num_b} = {num_a * num_b:.2f}"    # Multiplicación
    elif opcion == 4:
        return f"Resultado: {num_a} / {num_b} = {num_a / num_b:.2f}"    # División
    elif opcion == 5:
        return f"Resultado: {num_a} // {num_b} = {num_a // num_b:.2f}"  # División entera
    elif opcion == 6:
        return f"Resultado: {num_a} ^ {num_b} = {num_a ** num_b:.2f}"   # Exponenciación

# Código a nivel de módulo
flag = 1
while flag != 0:
    op = mostrar_menu() # Llama a la función para mostrar el menú y obtener la opción
    if op == 0:
        flag = 0  # Salir del programa haciendo uso de la bandera
    elif 0 < op < 7:    # Verifica que la opción esté dentro del rango de 1 a 6
        # Solicita ambos números
        numero_a = float(input("Ingrese el primer número: "))
        numero_b = float(input("Ingrese el segundo número: "))
        r = calcular(op, numero_a, numero_b)    # Llama a la función de cálculo
        print(r)
    else:
        print("Ingrese una opción válida...")   # Mensaje de error cuando se ingrese una opción fuera del rango
print("\nSaliendo...")  # Mensaje al salir del programa
