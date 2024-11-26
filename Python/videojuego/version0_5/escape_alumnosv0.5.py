import sys
import pygame


from config import Config
from alumno import Alumno
import game_functionalities

# Funcion para inicializar el juego
def run_game():
    pygame.init()
    esc_alumnos_config = Config()
    screen_size = (esc_alumnos_config.screen_width,esc_alumnos_config.screen_height)
    screen = pygame.display.set_mode(screen_size)
    game_title = esc_alumnos_config.game_title
    pygame.display.set_caption(game_title)
    alumno = Alumno(screen)
    running = True
    # Evento o acción que realiza el usuario, como cosas del ratón o del teclado. Por eso siempre se usa el ciclo while, porque siempre vamos a estar buscando eventos
    while running:
        # Meterlo en una función
        game_functionalities.game_events(alumno)
        background_color = esc_alumnos_config.background_color
        screen.fill(background_color)
        alumno.update()
        alumno.blitme()
        pygame.display.flip()  # Actualiza la pantalla con los cambios realizados (ilusión de movimiento)
## Código a nivel de módulo
run_game()