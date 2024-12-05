"""
Archivo que contiene las funcionalidades del juego.
- Control de los eventos.
- Refresco de los elementos en la pantalla.
"""

# Se importan las bibliotecas necesarias.
import sys
import pygame
"""NUEVO"""
from Bala import Bala

""" NUEVO. Ahora también recibe el objeto de las configuraciones, la pantalla y el grupo de laptops, ya que
se genera una laptop al presionar el 'espacio'"""
""" Función que administra los eventos del juego."""
def game_events(tank_config, screen, tanque, balas_group):
    # Se revisan los eventos del juego.
    for event in pygame.event.get():
        # El evento es un clic en cerrar el juego.
        if event.type == pygame.QUIT:
            sys.exit()

        # El evento es presionar una tecla.
        elif event.type == pygame.KEYDOWN:
            game_events_keydown(event, tank_config, screen, tanque, balas_group)

        # El evento es soltar una tecla.
        elif event.type == pygame.KEYUP:
            game_events_keyup(event, tanque)

""" NUEVO. Ahora también recibe el objeto de las configuraciones, la pantalla y el grupo de laptops, ya que
se genera una laptop al presionar el 'espacio'"""
""" Función que administra el evento cuando se presiona una tecla."""
def game_events_keydown(event, tank_config, screen, tanque, balas_group):
    # Se presiona la tecla 'derecha', implicando un movimiento en esta dirección.
    if event.key == pygame.K_RIGHT:
        tanque.is_moving_right = True

    # Se presiona la tecla 'izquierda', implicando un movimiento en esta dirección.
    elif event.key == pygame.K_LEFT:
        tanque.is_moving_left = True

    # Se presiona la tecla 'arriba', implicando un movimiento en esta dirección.
    elif event.key == pygame.K_UP:
        tanque.is_moving_up = True

    # Se presiona la tecla 'abajo', implicando un movimiento en esta dirección.
    elif event.key == pygame.K_DOWN:
        tanque.is_moving_down = True

    # NUEVO.
    # Se presiona la tecla 'espacio', por lo que se debe crear un nuevo objeto de la clase Laptop y añadirlo
    # al grupo de laptops.
    elif event.key == pygame.K_SPACE:
        new_bala = Bala(tank_config, screen, tanque)
        balas_group.add(new_bala)

# Función que administra el evento cuando se presiona una tecla.
def game_events_keyup(event, tanque):
    # Se suelta la tecla 'derecha', por lo que deja de moverse en esta dirección.
    if event.key == pygame.K_RIGHT:
        tanque.is_moving_right = False

    # Se suelta la tecla 'izquierda', por lo que deja de moverse en esta dirección.
    elif event.key == pygame.K_LEFT:
        tanque.is_moving_left = False

    # Se suelta la tecla 'arriba', por lo que deja de moverse en esta dirección.
    if event.key == pygame.K_UP:
        tanque.is_moving_up = False

    # Se suelta la tecla 'abajo', por lo que deja de moverse en esta dirección.
    elif event.key == pygame.K_DOWN:
        tanque.is_moving_down = False

# Función que administra la actualización de la pantalla.
def screen_refresh(tank_config, screen, tanque, balas_group):
    # Se muestra el fondo de la ventana como un único color.
    background = tank_config.background_color
    screen.fill(background)

    # NUEVO. Se regresan los comentarios antes de la versión 1.0
    # Se actualiza la posición del alumno.
    tanque.update_pos()

    # Se muestra el objeto alumno en la pantalla.
    tanque.blitme()

    # NUEVO
    # Se actualiza la posición y se muestra el grupo de laptops en la pantalla.
    for bala in balas_group.sprites():
        bala.update_pos()
        bala.blitme()

    # Se actualiza la pantalla, dando la impresión visual de movimiento.
    pygame.display.flip()  # Actualiza la pantalla