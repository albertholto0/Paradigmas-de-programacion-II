"""
Cambios respecto a la versión anterior:
3 - Se importa Group de pygame.sprite para generar un grupo de laptops que van a ser el arma del alumno.
4 - El punto anterior es la razón del por qué la clase Laptop hereda de la clase Sprite.
5 - Se modificó la velocidad de la laptop en la clase Config del archivo Config.py de 0.15 a 0.45

6 - La función game_events() ahora también recibe el objeto de las configuraciones, de la pantalla y del grupo de
7   las laptops. Por lo tanto, se modificó el archivo Game_functionalities.py
8 - Similarmente, la función screen_refresh() ahora recibe el grupo de laptops, en lugar del objeto de la laptop.
9   También se modificó esta parte en el archivo Game_functionalities.py
10 - En el archivo Game_functionalities.py también se revisa el nuevo evento de presionar el espacio para crear un
11   nueva objeto de la clase Laptop. El evento en donde se agrega la laptop al grupo de laptops es cuando se
12   presiona la tecla 'espacio'.
13 - En la función screen_refresh(), del archivo Game_functionalities.py, se actualiza la posición y se muestra el
14   grupo de laptops en la pantalla.
15 - Como resultado, se debería mostrar una laptop con una dirección hacia arriba cada que se presiona 'espacio'.
"""
# Se importan las bibliotecas necesarias.
import pygame
from Config import Config
from Alumno import Alumno
import Game_functionalities
"""NUEVO"""
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

    """NUEVO"""
    # Se crea un grupo para guardar las laptops (arma) del alumno.
    laptops_group = Group()

    # Se inicializa el ciclo del juego, en donde se verifican los eventos.
    running = True
    while running:
        """NUEVO. La función ahora también recibe el objeto de las configuraciones, de la pantalla y del grupo de las laptops."""
        # Los eventos se manejan en la función game_events(alumno) de Game_functionalities.py
        Game_functionalities.game_events(esc_alumnos_config, screen, alumno, laptops_group)

        """NUEVO. La función ahora recibe el grupo de las laptops."""
        # Se actualizan los elementos de la pantalla en la función screen_refresh que recibe los parámetros de las configuraciones, la pantalla y el alumno.
        Game_functionalities.screen_refresh(esc_alumnos_config, screen, alumno, laptops_group)


""" %%%%%%%  CÓDIGO A NIVEL DE MÓDULO  %%%%%%%%%%%%%%%%%%%%%%%% """
# Se ejecuta la función del juego.
run_game()