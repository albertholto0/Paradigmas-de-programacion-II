import pygame
from config import Config
from Tanque import Tanque
import game_functionalities
from pygame.sprite import Group
import sys
import time  # Para pausar el juego

""" Se define la función para inicializar el juego, las configuraciones y crear la pantalla. """
def run_game():
    # Inicializar el juego, las configuraciones y crear un objeto de la pantalla (screen).
    clock = pygame.time.Clock()
    pygame.init()
    # Se crea un objeto de la clase Config para las configuraciones.
    tank_config = Config()

    # Reproducir música de fondo
    pygame.mixer.music.load("media/musica_fondo.mp3")  # Cambia a la ruta de tu archivo de música
    pygame.mixer.music.set_volume(1)  # Ajusta el volumen (0.0 a 1.0)
    pygame.mixer.music.play(-1)  # Reproducir en bucle (-1 significa infinito)

    # Cargar sonido de disparo
    sonido_disparo = pygame.mixer.Sound("media/disparo.mp3")  # Cambia a la ruta de tu archivo de sonido
    sonido_disparo.set_volume(0.7)  # Ajusta el volumen del sonido de disparo

    # Se dibuja la ventana principal con la resolución dada en las configuraciones.
    screen_size = (tank_config.screen_width, tank_config.screen_height)
    screen = pygame.display.set_mode(screen_size)

    # Se muestra el título de la ventana con el nombre dado en las configuraciones.
    game_title = tank_config.game_title
    pygame.display.set_caption(game_title)

    # Crear los dos tanques: tanque1 y tanque2
    tanque1_position = (screen.get_rect().right - 100, screen.get_rect().centery)
    tanque1 = Tanque(screen, tank_config, position=tanque1_position)

    tanque2_position = (screen.get_rect().left + 100, screen.get_rect().centery)
    tanque2 = Tanque(screen, tank_config, image_path="media/tanque_arena.png", position=tanque2_position)

    # Se crea un grupo para guardar las balas de ambos tanques.
    balas_group = Group()

    # Se inicializa el ciclo del juego, en donde se verifican los eventos.
    running = True
    while running:
        # Manejo de eventos



        """ La función ahora también recibe los dos tanques y el grupo de balas. """
        # Los eventos se manejan en la función game_events (tanque1, tanque2) de game_functionalities.py
        game_functionalities.game_events(tank_config, screen, tanque1, tanque2, balas_group, sonido_disparo)

        # Se actualizan los elementos de la pantalla en la función screen_refresh.
        game_functionalities.screen_refresh(tank_config, clock, screen, tanque1, tanque2, balas_group)
        game_functionalities.manejar_colisiones(tanque1, tanque2, balas_group)
        game_functionalities.mostrar_niveles_vida(screen, tanque1, tanque2)
        # Actualiza la posición de las balas
        balas_group.update()

        """ Verifica si alguno de los tanques tiene vida <= 0 y detiene el juego. """
        if tanque1.vida <= 0 or tanque2.vida <= 0:
            print("Un tanque ha perdido toda su vida. El juego se cerrará en 3 segundos.")
            time.sleep(3)  # Pausa de 3 segundos
            pygame.quit()
            sys.exit()

""" %%%%%%% CÓDIGO A NIVEL DE MÓDULO %%%%%%%%%%%%%%%%%%%%%%%% """
# Se ejecuta la función del juego.
run_game()
