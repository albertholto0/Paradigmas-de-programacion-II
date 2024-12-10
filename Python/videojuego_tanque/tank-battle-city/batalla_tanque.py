import pygame
from config import Config
from Tanque import Tanque
import game_functionalities
"""NUEVO"""
from pygame.sprite import Group



""" Se define la función para inicializar el juego, las configuraciones y crear la pantalla."""
def run_game():
    # Inicializar el juego, las configuraciones y crear un objeto de la pantalla (screen).
    pygame.init()

    # Se crea un objeto de la clase Config para las configuraciones.
    tank_config = Config()

    # Se dibuja la ventana principal con la resolución dada en las configuraciones.
    screen_size = (tank_config.screen_width, tank_config.screen_height)
    screen = pygame.display.set_mode(screen_size)

    # Se muestra el título de la ventana con el nombre dado en las configuraciones.
    game_title = tank_config.game_title
    pygame.display.set_caption(game_title)

    # Se crea un objeto alumno de la clase Alumno.
    tanque = Tanque(screen, tank_config)

    """NUEVO"""
    # Se crea un grupo para guardar las laptops (arma) del alumno.
    balas_group = Group()

    # Se inicializa el ciclo del juego, en donde se verifican los eventos.
    running = True
    while running:
        """NUEVO. La función ahora también recibe el objeto de las configuraciones, de la pantalla y del grupo de las laptops."""
        # Los eventos se manejan en la función game_events(alumno) de game_functionalities.py
        game_functionalities.game_events(tank_config, screen, tanque, balas_group)

        """NUEVO. La función ahora recibe el grupo de las laptops."""
        # Se actualizan los elementos de la pantalla en la función screen_refresh que recibe los parámetros de las configuraciones, la pantalla y el alumno.
        game_functionalities.screen_refresh(tank_config, screen, tanque, balas_group)


""" %%%%%%%  CÓDIGO A NIVEL DE MÓDULO  %%%%%%%%%%%%%%%%%%%%%%%% """
# Se ejecuta la función del juego.
run_game()