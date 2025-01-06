import pygame
from config import Config
from Tanque import Tanque
import game_functionalities
from pygame.sprite import Group
import sys
import time

def run_game():
    clock = pygame.time.Clock()
    pygame.init()
    tank_config = Config()

    pygame.mixer.music.load("media/musica_fondo.mp3")
    pygame.mixer.music.set_volume(1)
    pygame.mixer.music.play(-1)

    sonido_disparo = pygame.mixer.Sound("media/disparo.mp3")
    sonido_disparo.set_volume(0.7)
    sonido_vacio = pygame.mixer.Sound("media/vacio.mp3")
    sonido_vacio.set_volume(0.7)

    sonido_botiquin = pygame.mixer.Sound("media/recoger_botiquin.mp3")
    sonido_municion = pygame.mixer.Sound("media/recoger_municion.mp3")
    sonido_botiquin.set_volume(0.7)
    sonido_municion.set_volume(0.7)

    screen_size = (tank_config.screen_width, tank_config.screen_height)
    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption(tank_config.game_title)

    tanque1_position = (screen.get_rect().right - 100, screen.get_rect().centery)
    tanque1 = Tanque(screen, tank_config, position=tanque1_position)

    tanque2_position = (screen.get_rect().left + 100, screen.get_rect().centery)
    tanque2 = Tanque(screen, tank_config, image_path="media/tanque_arena.png", position=tanque2_position)

    balas_group = Group()
    botiquines = Group()
    municiones = Group()
    pygame.time.set_timer(pygame.USEREVENT, 10000)

    running = True
    while running:
        game_functionalities.game_events(tank_config, screen, tanque1, tanque2, balas_group, botiquines, municiones, sonido_disparo, sonido_vacio)
        game_functionalities.screen_refresh(tank_config, clock, screen, tanque1, tanque2, balas_group, botiquines, municiones)
        game_functionalities.manejar_colisiones(tanque1, tanque2, balas_group, botiquines, municiones, sonido_botiquin, sonido_municion)
        balas_group.update()

        if tanque1.vida <= 0 or tanque2.vida <= 0:
            print("Un tanque ha perdido toda su vida. El juego se cerrará en 2 segundos.")
            time.sleep(2)
            pygame.quit()
            sys.exit()

"""Código a nivel de módulo"""
# Se ejecuta la función del juego.
run_game()
