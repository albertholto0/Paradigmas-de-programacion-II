import sys
import pygame


def game_events(alumnos):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN: #Verificar si se presionó una tecla
            if event.key == pygame.K_RIGHT:
                alumnos.is_moving_right = True
            if event.key == pygame.K_LEFT:
                alumnos.is_moving_left = True
            if event.key == pygame.K_UP:
                alumnos.is_moving_up = True
            if event.key == pygame.K_DOWN:
                alumnos.is_moving_down = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                alumnos.is_moving_right = False
            if event.key == pygame.K_LEFT:
                alumnos.is_moving_left = False
            if event.key == pygame.K_UP:
                alumnos.is_moving_up = False
            if event.key == pygame.K_DOWN:
                alumnos.is_moving_down = False

