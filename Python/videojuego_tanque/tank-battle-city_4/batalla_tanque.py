import pygame
from config import Config
from Tanque import Tanque
import game_functionalities
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

    # Crear los dos tanques: tanque1 y tanque2
    tanque1 = Tanque(screen, tank_config)  # Tanque 1 con imagen predeterminada
    tanque2 = Tanque(screen, tank_config, image_path="media/tanque_arena.png")  # Tanque 2 con imagen diferente

    # Crear los dos tanques: tanque1 y tanque2
    # Crear los dos tanques: tanque1 y tanque2
    # Tanque1 centrado a la derecha
    tanque1_position = (screen.get_rect().right - tanque1.image_rect.width // 2, screen.get_rect().centery)
    tanque1 = Tanque(screen, tank_config, position=tanque1_position)

    # Tanque2 centrado a la izquierda
    tanque2_position = (screen.get_rect().left + tanque2.image_rect.width // 2, screen.get_rect().centery)
    tanque2 = Tanque(screen, tank_config, image_path="media/tanque_arena.png", position=tanque2_position)

    # Se crea un grupo para guardar las balas de ambos tanques.
    balas_group = Group()

    # Se inicializa el ciclo del juego, en donde se verifican los eventos.
    running = True
    while running:
        """ La función ahora también recibe los dos tanques y el grupo de balas. """
        # Los eventos se manejan en la función game_events (tanque1, tanque2) de game_functionalities.py
        game_functionalities.game_events(tank_config, screen, tanque1, tanque2, balas_group)

        """ La función ahora recibe ambos tanques y el grupo de balas. """
        # Se actualizan los elementos de la pantalla en la función screen_refresh.
        game_functionalities.screen_refresh(tank_config, screen, tanque1, tanque2, balas_group)

""" %%%%%%% CÓDIGO A NIVEL DE MÓDULO %%%%%%%%%%%%%%%%%%%%%%%% """
# Se ejecuta la función del juego.
run_game()
