"""
Archivo que contiene las funcionalidades del juego.
- Control de los eventos.
- Refresco de los elementos en la pantalla.
"""

# Se importan las bibliotecas necesarias.
import sys
import pygame
from Laptop import Laptop
"""NUEVO"""
from Hacker import Hacker

""" Función que administra los eventos del juego."""
def game_events(esc_alumnos_config, screen, alumno, laptops_group):
    # Se revisan los eventos del juego.
    for event in pygame.event.get():
        # El evento es un clic en cerrar el juego.
        if event.type == pygame.QUIT:
            sys.exit()

        # El evento es presionar una tecla.
        elif event.type == pygame.KEYDOWN:
            game_events_keydown(event, esc_alumnos_config, screen, alumno, laptops_group)

        # El evento es soltar una tecla.
        elif event.type == pygame.KEYUP:
            game_events_keyup(event, alumno)

""" Funci\u00F3n que administra el evento cuando se presiona una tecla."""
def game_events_keydown(event, esc_alumnos_config, screen, alumno, laptops_group):
    # Se presiona la tecla 'derecha', implicando un movimiento en esta direcci\u00F3n.
    if event.key == pygame.K_RIGHT:
        alumno.is_moving_right = True

    # Se presiona la tecla 'izquierda', implicando un movimiento en esta direcci\u00F3n.
    elif event.key == pygame.K_LEFT:
        alumno.is_moving_left = True

    # Se presiona la tecla 'arriba', implicando un movimiento en esta direcci\u00F3n.
    elif event.key == pygame.K_UP:
        alumno.is_moving_up = True

    # Se presiona la tecla 'abajo', implicando un movimiento en esta direcci\u00F3n.
    elif event.key == pygame.K_DOWN:
        alumno.is_moving_down = True

    # Si se presiona la tecla 'espacio' y el n\u00FAmero de laptops es menor al permitido en las configuraciones,
    # se crea un nuevo objeto de la clase Laptop y se agrega al grupo de laptops.
    elif event.key == pygame.K_SPACE and (len(laptops_group) + 1) <= esc_alumnos_config.max_laptops:
        new_laptop = Laptop(esc_alumnos_config, screen, alumno)
        laptops_group.add(new_laptop)
"""
Función que administra el evento cuando se presiona una tecla.
"""
def game_events_keyup(event, alumno):
    # Se suelta la tecla 'derecha', por lo que deja de moverse en esta dirección.
    if event.key == pygame.K_RIGHT:
        alumno.is_moving_right = False

    # Se suelta la tecla 'izquierda', por lo que deja de moverse en esta dirección.
    elif event.key == pygame.K_LEFT:
        alumno.is_moving_left = False

    # Se suelta la tecla 'arriba', por lo que deja de moverse en esta dirección.
    if event.key == pygame.K_UP:
        alumno.is_moving_up = False

    # Se suelta la tecla 'abajo', por lo que deja de moverse en esta dirección.
    elif event.key == pygame.K_DOWN:
        alumno.is_moving_down = False

"""
Función que administra la actualización de la pantalla.
"""
def screen_refresh(esc_alumnos_config, screen, alumno, laptops_group, hackers_group):
    # Se muestra el fondo de la ventana como un único color.
    background = esc_alumnos_config.background_color
    screen.fill(background)

    # Se actualiza la posición del alumno.
    alumno.update_pos()

    # Se muestra el objeto alumno en la pantalla.
    alumno.blitme()

    # Se verifica si la parte inferior de alguna de las laptops deja de verse en la pantalla.
    # Si es el caso, se elimina del grupo.
    for laptop in laptops_group.copy():
        if laptop.laptop_rect.bottom < screen.get_rect().top:
            laptops_group.remove(laptop)

    # Se actualiza la posición y se muestra el grupo de laptops en la pantalla.
    for laptop in laptops_group.sprites():
        laptop.update_pos()
        laptop.blitme()

    # Se muestra el grupo de hackers en la pantalla.
    for hacker in hackers_group.sprites():
        hacker.blitme()

    # Se actualiza la pantalla, dando la impresión visual de movimiento.
    pygame.display.flip()  # Actualiza la pantalla

"""
Función para generar una flota de hackers (enemigos).
"""
def enemy_aircraft(esc_alumnos_config, screen, hackers_group):
    # Se crea un objeto de la clase Hacker y lo añadimos al grupo de hackers.
    hacker = Hacker(esc_alumnos_config, screen)
    hackers_group.add(hacker)
    # Se calcula el número de hackers que alcanzan en la pantalla. Primero se obtiene la longitud del hacker y de
    # la pantalla. Después, se calcula el espacio disponible considerando un espacio adicional de la longitud del
    # hacker para el movimiento (por eso la multiplicación por dos).
    # Finalmente, se obtiene el número entero con la cantidad de hackers que alcanzan en el ancho de la pantalla.
    hacker_width = hacker.hacker_rect.width
    screen_width = esc_alumnos_config.screen_width

    available_space = screen_width - (2 * hacker_width)
    num_hackers = available_space // hacker_width

    # Se agrega una fila de hackers, considerando que ya tenemos un hacker en el grupo.
    # Hay que notar que se modifica la posición en x de cada hacker para que no estén superpuestos.
    # Finalmente, se añaden todos los hackers al grupo, formando una fila que abarca toda la pantalla.
    for i in range(1, num_hackers):
        hacker = Hacker(esc_alumnos_config, screen)
        hacker.x = hacker_width + (2 * i * hacker_width)
        hacker.hacker_rect.x = hacker.x
        hackers_group.add(hacker)

