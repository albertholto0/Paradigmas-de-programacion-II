import random

archivo_rifa = open("archivo_rifa.txt","w",encoding = "UTF-8")
archivo_participantes = open("archivo_participantes.txt","w",encoding = "UTF-8")
contador_rifa = 1

# función para mostrar el menú
def mostrar_menu():
    print("\n * - - RIFA DE UNA COMPUTADORA - - *")
    print("1) Ver correos de participantes.")
    print("2) Agregar correo de participante.")
    print("3) Eliminar correo de participante.")
    print("4) Seleccionar ganador.")
    print("5) Ganadores previos")
    print("0) Salir.")
    return int(input("\nIngresa una de las opciones: "))

# función para ver los correos de los participantes
def ver_participantes():
    with open("archivo_participantes.txt","r",encoding="UTF-8") as archivo:
        participantes = archivo.readlines()
        if participantes:
            for i, participante in enumerate(participantes,start = 1):
                print(f"{i}. {participante}",end="")
        else:
            print("\nNo hay participantes...")

# Función para agregar un correo de participante
def agregar_participante():
    correo = input("\nIngresa el correo del participante: ")
    with open("archivo_participantes.txt","r",encoding="UTF-8") as archivo:
        for linea in archivo:
            if correo in linea:
                print("Este participante ya ha sido agregado...")
                return
    with open("archivo_participantes.txt","a",encoding="UTF-8") as archivo:
        archivo.write(f"{correo}\n")

# Eliminar participantes
def eliminar_participantes():
    with open("archivo_participantes.txt", "r", encoding="UTF-8") as archivo:
        participantes = archivo.readlines()
        if not participantes:
            print("No hay participantes a borrar...")
        else:
            ver_participantes()
            try:
                eliminar = int(input("Ingrese número de participante a eliminar: "))
                if 1 < eliminar < len(participantes):
                    participante_eliminar = participantes[eliminar - 1]
                    participantes.remove(participante_eliminar)
                    with open("archivo_participantes.txt", "w", encoding="UTF-8") as archivo_actualizado:
                        archivo_actualizado.writelines(participantes)
                else:
                    print("Numero no válido en el rango...")
            except ValueError as error_funcion:
                print(f"Ingresa un valor númerico | {error_funcion}")

# Selección de ganador
def escoger_ganador(contador_rifa_funcion):
    with open("archivo_participantes.txt", "r", encoding="UTF-8") as archivo:
        participantes = archivo.readlines()
        if not participantes:
            print("No hay participantes a rifar...")
        else:
            ganador = random.choice(participantes)
            print(f"El ganador de la xbox 720 es: {ganador}")
            with open("archivo_rifa.txt","a",encoding = "UTF-8") as archivo_ganador:
                archivo_ganador.write(f"El ganador de la rifa número {contador_rifa_funcion} es {ganador}.")
            contador_rifa_funcion += 1

try:
    while True:
        opcion = 0
        try:
            opcion = mostrar_menu()
        except ValueError as e:
            print(f"Ingresa un valor númerico | {e}")
            continue
        if opcion == 0:
            print("\nSaliendo de la rifa...")
            break
        elif opcion == 1:
            ver_participantes()
        elif opcion == 2:
            agregar_participante()
        elif opcion == 3:
            eliminar_participantes()
        elif opcion == 4:
            escoger_ganador(contador_rifa)
        else:
            print("\nOpción no válida. Por favor, intenta de nuevo.")
except KeyboardInterrupt:
    print("El programa ha sido cerrado por el usuario repentinamente...")