import sys
import pygame


def game_events(alumno):
    # Se revisan los eventos del juego
    for event in pygame.event.get():
        # El evento es un clic en cerrar el juego
        if event.type == pygame.QUIT:
            sys.exit()
        # El evento es presionar una tecla
        elif event.type == pygame.KEYDOWN: #Verificar si se presionó una tecla
           game_events_keydown(event,alumno)
        # El evento es soltar una tecla
        elif event.type == pygame.KEYUP:
            game_events_keyup(event, alumno)

def game_events_keydown(event,alumno):
    if event.key == pygame.K_RIGHT:
        alumno.is_moving_right = True
    if event.key == pygame.K_LEFT:
        alumno.is_moving_left = True
    if event.key == pygame.K_UP:
        alumno.is_moving_up = True
    if event.key == pygame.K_DOWN:
        alumno.is_moving_down = True

def game_events_keyup(event,alumno):
    if event.key == pygame.K_RIGHT:
        alumno.is_moving_right = False
    if event.key == pygame.K_LEFT:
        alumno.is_moving_left = False
    if event.key == pygame.K_UP:
        alumno.is_moving_up = False
    if event.key == pygame.K_DOWN:
        alumno.is_moving_down = False

def screen_refresh(esc_alumnos_config, screen, alumno, laptop):
    background = esc_alumnos_config.background_color
    screen.fill(background)  # Limpiar la pantalla con el color de fondo
    alumno.update_pos()  # Actualiza la posición del alumno
    laptop.update_pos()   # Actualiza la posición de la laptop
    alumno.blitme()  # Dibuja el alumno en la pantalla
    laptop.blitme()   # Dibuja la laptop en la pantalla
    pygame.display.flip()  # Actualiza la pantalla con los nuevos cambios
