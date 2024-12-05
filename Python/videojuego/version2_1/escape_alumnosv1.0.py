"""
Cambios respecto a la versión anterior:
- Los hackers ahora se van a manejar como grupos, similar a como se realizó con las laptops.
- Lo anterior implica que ya no se requiere importar la clase Hacker, crear el objeto hacker y dibujarlo con
  la función screen_refresh()
- Se crea el grupo de hackers utilizando la función Group de pygame.sprite
- Se agrega una nueva función llamada enemy_aircraft(), dentro del archivo Game_functionalities.py, la cual se
  llama en este archivo y se utiliza para crear una fila de enemigos.
- La función screen_refresh() de Game_functionalities.py también se modifica para dibujar el grupo de hackers.
- Todavía no hay interacción con el alumno.
"""

# Se importan las bibliotecas necesarias.
import pygame
from Config import Config
from Alumno import Alumno
import Game_functionalities
from pygame.sprite import Group

""" Se define la función para inicializar el juego, las configuraciones y crear la pantalla."""
def run_game():
    # Inicializar el juego, las configuraciones y crear un objeto de la pantalla (screen).
    pygame.init()

    # Se crea un objeto de la clase Config para las configuraciones.
    esc_alumnos_config = Config()

    # Se dibuja la ventana principal con la resolución dada en las configuraciones.
    screen_size = (esc_alumnos_config.screen_width, esc_alumnos_config.screen_height)
    screen = pygame.display.set_mode(screen_size)

    # Se muestra el título de la ventana con el nombre dado en las configuraciones.
    game_title = esc_alumnos_config.game_title
    pygame.display.set_caption(game_title)

    # Se crea un objeto alumno de la clase Alumno.
    alumno = Alumno(screen, esc_alumnos_config)

    # Se crea un grupo para guardar las laptops (arma) del alumno.
    laptops_group = Group()

    # Se crea un grupo para guardar los hackers (enemigos del alumno).
    hackers_group = Group()

    """NUEVO"""
    # Se llama a la función para generar una flota de enemigos.
    Game_functionalities.enemy_aircraft(esc_alumnos_config, screen, hackers_group)

    # Se inicializa el ciclo del juego, en donde se verifican los eventos.
    running = True
    while running:
        # Los eventos se manejan en la función game_events(alumno) de Game_functionalities.py
        Game_functionalities.game_events(esc_alumnos_config, screen, alumno, laptops_group)

        """NUEVO. La función ahora recibe el grupo de hackers, en lugar del objeto del hacker."""
        # Se actualizan los elementos de la pantalla en la función screen_refresh que recibe
        # los parámetros de las configuraciones, la pantalla, el alumno, el grupo de laptops y el de hackers.
        Game_functionalities.screen_refresh(esc_alumnos_config, screen, alumno, laptops_group, hackers_group)


""" %%%%%%% CÓDIGO A NIVEL DE MÓDULO %%%%%%%%%%%%%%%% """
# Se ejecuta la función del juego.
run_game()
