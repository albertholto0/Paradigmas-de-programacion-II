# Se importan las bibliotecas necesarias.
import sys
import pygame
from Bala import Bala

def game_events(tank_config, screen, tanque1, tanque2, balas_group):
    # Se revisan los eventos del juego.
    for event in pygame.event.get():
        # El evento es un clic en cerrar el juego.
        if event.type == pygame.QUIT:
            sys.exit()

        # El evento es presionar una tecla.
        elif event.type == pygame.KEYDOWN:
            game_events_keydown(event, tank_config, screen, tanque1, tanque2, balas_group)

        # El evento es soltar una tecla.
        elif event.type == pygame.KEYUP:
            game_events_keyup(event, tanque1, tanque2)

def game_events_keydown(event, tank_config, screen, tanque1, tanque2, balas_group):
    # Tanque 1 (movimiento con las teclas de flecha)
    if event.key == pygame.K_RIGHT:
        tanque1.is_moving_right = True
    elif event.key == pygame.K_LEFT:
        tanque1.is_moving_left = True
    elif event.key == pygame.K_UP:
        tanque1.is_moving_up = True
    elif event.key == pygame.K_DOWN:
        tanque1.is_moving_down = True

    # Tanque 2 (movimiento con las teclas W, A, S, D)
    if event.key == pygame.K_d:
        tanque2.is_moving_right = True
    elif event.key == pygame.K_a:
        tanque2.is_moving_left = True
    elif event.key == pygame.K_w:
        tanque2.is_moving_up = True
    elif event.key == pygame.K_s:
        tanque2.is_moving_down = True

    # Intercambio de teclas de disparo:
    # Crear una bala cuando se presiona la tecla Enter (Tanque 1)
    elif event.key == pygame.K_RETURN:
        new_bala = Bala(tank_config, screen, tanque1)
        balas_group.add(new_bala)

    # Crear una bala cuando se presiona la tecla espacio (Tanque 2)
    elif event.key == pygame.K_SPACE:
        new_bala = Bala(tank_config, screen, tanque2)
        balas_group.add(new_bala)

# Función que administra el evento cuando se presiona una tecla.
def game_events_keyup(event, tanque1, tanque2):
    # Tanque 1
    if event.key == pygame.K_RIGHT:
        tanque1.is_moving_right = False
    elif event.key == pygame.K_LEFT:
        tanque1.is_moving_left = False
    elif event.key == pygame.K_UP:
        tanque1.is_moving_up = False
    elif event.key == pygame.K_DOWN:
        tanque1.is_moving_down = False

    # Tanque 2
    if event.key == pygame.K_d:
        tanque2.is_moving_right = False
    elif event.key == pygame.K_a:
        tanque2.is_moving_left = False
    elif event.key == pygame.K_w:
        tanque2.is_moving_up = False
    elif event.key == pygame.K_s:
        tanque2.is_moving_down = False

# Función para verificar la colisión entre los tanques.
def check_tank_collision(tanque1, tanque2):
    # Verifica si los rectángulos de los tanques colisionan.
    return tanque1.image_rect.colliderect(tanque2.image_rect)

# Función que administra la actualización de la pantalla.
def screen_refresh(tank_config, screen, tanque1, tanque2, balas_group):
    background = pygame.image.load(tank_config.background_image_path)
    background = pygame.transform.scale(background, (tank_config.screen_width, tank_config.screen_height))
    screen.blit(background, (0, 0))

    # Guardar posiciones previas de los tanques
    prev_pos_tanque1 = tanque1.image_rect.topleft
    prev_pos_tanque2 = tanque2.image_rect.topleft

    # Actualizar posiciones de los tanques con colisión verificada
    tanque1.update_pos(tanque2)
    tanque2.update_pos(tanque1)

    # Mostrar los tanques
    tanque1.blitme()
    tanque2.blitme()

    # Actualizar balas
    for bala in balas_group.copy():
        if not screen.get_rect().colliderect(bala.bala_rect):
            balas_group.remove(bala)

    for bala in balas_group.sprites():
        bala.update_pos()
        bala.blitme()

    pygame.display.flip()
