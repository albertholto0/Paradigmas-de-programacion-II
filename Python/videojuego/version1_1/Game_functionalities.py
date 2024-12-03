"""
Archivo que contiene las funcionalidades del juego.
- Control de los eventos.
- Refresco de los elementos en la pantalla.
"""

# Se importan las bibliotecas necesarias.
import sys
import pygame
"""NUEVO"""
from Laptop import Laptop

""" NUEVO. Ahora también recibe el objeto de las configuraciones, la pantalla y el grupo de laptops, ya que
se genera una laptop al presionar el 'espacio'"""
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

""" NUEVO. Ahora también recibe el objeto de las configuraciones, la pantalla y el grupo de laptops, ya que
se genera una laptop al presionar el 'espacio'"""
""" Función que administra el evento cuando se presiona una tecla."""
def game_events_keydown(event, esc_alumnos_config, screen, alumno, laptops_group):
    # Se presiona la tecla 'derecha', implicando un movimiento en esta dirección.
    if event.key == pygame.K_RIGHT:
        alumno.is_moving_right = True

    # Se presiona la tecla 'izquierda', implicando un movimiento en esta dirección.
    elif event.key == pygame.K_LEFT:
        alumno.is_moving_left = True

    # Se presiona la tecla 'arriba', implicando un movimiento en esta dirección.
    elif event.key == pygame.K_UP:
        alumno.is_moving_up = True

    # Se presiona la tecla 'abajo', implicando un movimiento en esta dirección.
    elif event.key == pygame.K_DOWN:
        alumno.is_moving_down = True

    # NUEVO.
    # Se presiona la tecla 'espacio', por lo que se debe crear un nuevo objeto de la clase Laptop y añadirlo
    # al grupo de laptops.
    elif event.key == pygame.K_SPACE:
        new_laptop = Laptop(esc_alumnos_config, screen, alumno)
        laptops_group.add(new_laptop)

# Función que administra el evento cuando se presiona una tecla.
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

# Función que administra la actualización de la pantalla.
def screen_refresh(esc_alumnos_config, screen, alumno, laptops_group):
    # Se muestra el fondo de la ventana como un único color.
    background = esc_alumnos_config.background_color
    screen.fill(background)

    # NUEVO. Se regresan los comentarios antes de la versión 1.0
    # Se actualiza la posición del alumno.
    alumno.update_pos()

    # Se muestra el objeto alumno en la pantalla.
    alumno.blitme()

    # NUEVO
    # Se actualiza la posición y se muestra el grupo de laptops en la pantalla.
    for laptop in laptops_group.sprites():
        laptop.update_pos()
        laptop.blitme()

    # Se actualiza la pantalla, dando la impresión visual de movimiento.
    pygame.display.flip()  # Actualiza la pantalla