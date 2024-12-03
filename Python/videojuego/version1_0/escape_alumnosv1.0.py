import sys
import pygame
from config import Config
from alumno import Alumno
import game_functionalities
from laptop import Laptop

# Funcion para inicializar el juego
def run_game():
    pygame.init()
    esc_alumnos_config = Config()
    screen_size = (esc_alumnos_config.screen_width, esc_alumnos_config.screen_height)
    screen = pygame.display.set_mode(screen_size)

    game_title = esc_alumnos_config.game_title
    pygame.display.set_caption(game_title)

    alumno = Alumno(screen, esc_alumnos_config)
    laptop = Laptop(esc_alumnos_config, screen, alumno)

    running = True
    while running:
        game_functionalities.game_events(alumno)  # Procesar los eventos de teclado
        game_functionalities.screen_refresh(esc_alumnos_config, screen, alumno, laptop)  # Actualizar la pantalla
run_game()