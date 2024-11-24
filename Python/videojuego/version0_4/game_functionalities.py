import sys
import pygame


def game_events(alumnos):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN: #Verificar si se presionó una tecla
            if event.key == pygame.K_RIGHT:
                alumnos.is_moving_right = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                alumnos.is_moving_right = False
