"""
Nombre del archivo: Snake_game.py

Versión 0.6:
* Se agrega el contenido multimedia del juego, por lo que se agrega la clase Media en el archivo Media.py
  en donde
  * todos los archivos multimedia se encuentran en la carpeta media.
  * Se agrega el objeto media (de la clase Media) en Snake_game.py.
  * Se agrega la música y sonidos al juego. Para ello:
    * La música de fondo se reproduce al crear el objeto media.
    * Se reproduce un sonido del juego con el métod0 media.play_start_sound().
    * El sonido de la colisión cabeza de la serpiente - comida (media.play_eaten_sound()) se realiza en la función
      Game_functionalities.check_collisions(). Por lo tanto, se modifica para reproducir el efecto necesario.
    * EL sonido del fin del juego (media.play_game_over_sound()) se realiza en la función
      Game_functionalities.game_over_fun(). Por lo tanto, ahora recibe el objeto media.
  * Se agrega un fondo de pantalla como una imagen, en lugar de un color sólido. Para ello:
    * Se carga la imagen en la clase Media.
    * Se utiliza el métod0 blit_background() en Game_functionalities.screen_refresh() para mostrar el fondo.
    * Ya no se requiere el color de fondo de la pantalla, por lo que se elimina de Configurations.py.
  * Se muestran dos imágenes cuando se termina el juego. Para ello:
    * Se cargan las imágenes en la clase Media, se obtienen sus rect y se agregan los métodos blit para mostrarlas
      en la pantalla.
    * Ambos métodos se llaman en la función Game_functionalities.game_over_fun().
* Se oculta el puntero del ratón utilizando la función pygame.mouse.set_visible(), lo que se realiza antes de iniciar el ciclo del juego.
* Se añade el marcador en la parte superior izquierda. Para ello:
  * Se agregan las configuraciones de los marcadores, como el color del texto, la fuente y el tamaño, en Configurations.py.
  * Se utiliza la función get_rect de texto en la clase Media, en donde se agrega el métod0 update_scoreboard()
    que se utiliza para actualizar el marcador.
  * Este métod0 se llama en Game_functionalities.screen_refresh().
    En este caso, el marcador es la longitud del cuerpo de la serpiente.
"""

# Se importan las bibliotecas necesarias.
import pygame
from pygame.sprite import Group
from Configurations import Configurations
from Snake import Snake
import Game_functionalities
from Food import Food
"""NUEVO."""
from Media import Media

""" Se define la función para inicializar el juego, las configuraciones y crear la pantalla."""
def run_game():
    # Se inicializa pygame, se crea un objeto de la clase Configurations y un reloj para los FPS.
    pygame.init()
    snake_game_configurations = Configurations()
    clock = pygame.time.Clock()

    # Se dibuja la ventana principal con la resolución dada en las configuraciones.
    # Además, se muestra el título en la ventana.
    screen_size = (snake_game_configurations.screen_width, snake_game_configurations.screen_height)
    screen = pygame.display.set_mode(screen_size)
    game_title = snake_game_configurations.game_title
    pygame.display.set_caption(game_title)

    # Se crea un grupo que va ir guardando el cuerpo de la serpiente.
    # Por lo tanto, en primer lugar se agrega la cabeza de la serpiente.
    snake_head = Snake(snake_game_configurations, screen, snake_game_configurations.snake_head_color)
    snake_body = Group()
    snake_body.add(snake_head)

    # Se crea un objeto de la clase Food y se añade al grupo food_group.
    food = Food(snake_game_configurations, screen, snake_game_configurations.food_color, snake_body)
    food_group = Group()
    food_group.add(food)

    """NUEVO."""
    # Se crea un objeto que contiene los archivos multimedia. Además, se reproduce el sonido inicial.
    media = Media(snake_game_configurations, screen)
    media.play_start_sound()

    """NUEVO."""
    # Se oculta el cursor del mouse.
    pygame.mouse.set_visible(False)

    # Se inicializa el ciclo del juego, utilizando dos funciones principales.
    game_over = False
    while not game_over:
        # Función que administra los eventos del juego.
        Game_functionalities.game_events()

        """NUEVO. Ahora recibe el objeto media con el contenido multimedia."""
        # Función que administra las colisiones del juego. Devuelve la bandera del fin del juego.
        game_over = Game_functionalities.check_collisions(snake_game_configurations, screen, snake_body, food_group,
                                                          media)

        # Se verifica si hay un fin del juego.
        if game_over:
            """NUEVO. Ahora recibe el objeto media con el contenido multimedia."""
            Game_functionalities.game_over_fun(media)

        else:
            # Función que administra el movimiento de la serpiente.
            Game_functionalities.update_snake(snake_game_configurations, snake_body)

            """NUEVO. Ahora se muestra una imagen en lugar de un color sólido, por lo que ya no se requiere el
            objeto screen, pero sí el objeto media con el contenido multimedia."""
            # Función que administra los elementos en la pantalla.
            Game_functionalities.screen_refresh(snake_game_configurations, clock, snake_body, food_group, media)

    """ %%%%%% CÓDIGO A NIVEL DE MÓDULO %%%%%% """
    # Se ejecuta la función principal del juego.
run_game()
