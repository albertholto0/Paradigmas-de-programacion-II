"""
Nombre: Albert Alexis Contreras Mendoza
Fecha: 2 de diciembre del 2024
Descripción: Ejercicio 1 haciendo uso de las listas
    Este programa es una playlist de videos de Youtube.
    Se debe mostrar el siguiente menú:
          ***  Playlist de videos de YouTube  ***
        1) Ver playlist por videos añadidos.
        2) Ver playlist por orden ascendente (A-Z).
        3) Ver playlist por orden descendente (Z-A).
        4) Añadir video de YouTube a la playlist.
        5) Añadir varios videos de YouTube a la playlist.
        6) Eliminar video de la playlist.
        0) Salir.
    Cualquier otro caso -> Opción no válida.
    Para ello:
        a) Utilice funciones para modular el código.
        b) Utilice una lista para la playlist.
        c) Utilice índices para mostrar los videos.
"""
playlist = []

# Función para mostrar el menú
def mostrar_menu():
    print("\n***  Playlist de videos de YouTube  ***")
    print("1. Ver playlist por videos añadidos.")
    print("2. Ver playlist por orden ascendente (A-Z).")
    print("3. Ver playlist por orden descendente (Z-A).")
    print("4. Añadir video de YouTube a la playlist.")
    print("5. Añadir varios videos de YouTube a la playlist.")
    print("6. Eliminar video de la playlist.")
    print("0. Salir.")
    return input("\nIngresa una de las opciones: ")

def ver_playlist():
    if not playlist:
        print("\nLa playlist está vacía.")
    else:
        print("\n*** Playlist de videos ***")
        for i, video in enumerate(playlist, start=1):
            print(f"{i}. {video}")
# Mostrar de la A la Z
def ver_ascendente():
    if not playlist:
        print("\nLa playlist está vacía.")
    else:
        print("\n*** Playlist ordenada (A-Z) ***")
        for i, video in enumerate(sorted(playlist), start=1):
            print(f"{i}. {video}")
# Mostrar de la Z la A
def ver_descendente():
    if not playlist:
        print("\nLa playlist está vacía.")
    else:
        print("\n*** Playlist ordenada (Z-A) ***")
        for i, video in enumerate(sorted(playlist, reverse=True), start=1):
            print(f"{i}. {video}")
# Función para agregar un video
def agregar_video():
    video = input("\nIngresa el nombre del video a añadir: ")
    playlist.append(video)
    print(f"'{video}' ha sido añadido a la playlist.")
# Función para agregar varios videos
def agregar_varios_videos():
    num_video = int(input("\nIngresa el número de videos a añadir: "))
    for i in range(num_video):
        video = input(f"\nIngresa el nombre del video [{i+1}] a añadir: ")
        playlist.append(video)
        print(f"'{video}' ha sido añadido a la playlist.")
    print("Los videos han sido añadidos a la playlist")
# Función para eliminar videos de la playlist
def eliminar_video():
    if not playlist:
        print("\nLa playlist está vacía.")
    else:
        ver_playlist()  # Mostrar la playlist actual
        while True:
            indice = int(input("\nIngresa el número del video que deseas eliminar: "))
            if indice % 1 == 0:  # Verificar si la entrada es un número entero positivo
                indice -= 1  # Ajustar el índice
                if -1 < indice < len(playlist):
                    video_eliminado = playlist.pop(indice)  # Eliminar el video
                    print(f"'{video_eliminado}' ha sido eliminado de la playlist.")
                    break
                else:
                    print("Índice fuera de rango. Intenta de nuevo.")
            else:
                print("Por favor, ingresa un número válido.")  # Mensaje si la entrada no es un número válido
                
# Código a nivel de modulo
while True:
    opcion = mostrar_menu()
    if opcion == "0":
        print("\nSaliendo del youtube...")
        break
    elif opcion == "1":
        ver_playlist()
    elif opcion == "2":
        ver_ascendente()
    elif opcion == "3":
        ver_descendente()
    elif opcion == "4":
        agregar_video()
    elif opcion == "5":
        agregar_varios_videos()
    elif opcion == "6":
        eliminar_video()
    else:
        print("\nOpción no válida. Por favor, intenta de nuevo.")
