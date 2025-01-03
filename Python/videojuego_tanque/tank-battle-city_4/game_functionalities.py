# Se importan las bibliotecas necesarias.
import sys
import pygame
from Bala import Bala

def game_events(tank_config, screen, tanque1, tanque2, balas_group, sonido_disparo):
    # Se revisan los eventos del juego.
    for event in pygame.event.get():
        # El evento es un clic en cerrar el juego.
        if event.type == pygame.QUIT:
            sys.exit()

        # El evento es presionar una tecla.
        elif event.type == pygame.KEYDOWN:
            game_events_keydown(event, tank_config, screen, tanque1, tanque2, balas_group, sonido_disparo)

        # El evento es soltar una tecla.
        elif event.type == pygame.KEYUP:
            game_events_keyup(event, tanque1, tanque2)

def game_events_keydown(event, tank_config, screen, tanque1, tanque2, balas_group, sonido_disparo):
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

    # Crear una bala cuando se presiona la tecla Enter (Tanque 1)
    elif event.key == pygame.K_RETURN:
        new_bala = Bala(tank_config, screen, tanque1)
        balas_group.add(new_bala)
        sonido_disparo.play()  # Reproducir sonido de disparo

    # Crear una bala cuando se presiona la tecla espacio (Tanque 2)
    elif event.key == pygame.K_SPACE:
        new_bala = Bala(tank_config, screen, tanque2)
        balas_group.add(new_bala)
        sonido_disparo.play()  # Reproducir sonido de disparo

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

# Parte de mostrar_niveles_vida en game_functionalities.py
def mostrar_niveles_vida(screen, vida_tanque1, vida_tanque2):
    font = pygame.font.Font("media/Pixeled.ttf", 14)  # Fuente por defecto, tamaño 36
    vida_texto_2 = font.render(f"Tanque Verde: {vida_tanque1}", True, (13, 69, 23))
    vida_texto_1 = font.render(f"Tanque Arena: {vida_tanque2}", True, (92, 56, 2))

    # Mostrar los textos en las posiciones correspondientes
    screen.blit(vida_texto_1, (10, 10))  # Superior izquierda
    screen.blit(vida_texto_2, (screen.get_width() - vida_texto_2.get_width() - 10, 10))  # Superior derecha

def manejar_colisiones(tanque1, tanque2, balas_group):
    for bala in balas_group:
        # Actualizamos la posición de la bala
        bala.update_pos()

        # Verificamos si la bala está fuera de la pantalla
        if not bala.bala_rect.colliderect(bala.screen.get_rect()):
            balas_group.remove(bala)
            continue  # Pasamos a la siguiente bala

        # Verificar colisiones con los tanques
        if tanque1.image_rect.colliderect(bala.bala_rect) and tanque1.vida > 0:
            tanque1.vida -= 10  # Reducir vida de tanque1
            balas_group.remove(bala)  # Eliminar la bala
            break  # Salir del bucle después de la colisión

        elif tanque2.image_rect.colliderect(bala.bala_rect) and tanque2.vida > 0:
            tanque2.vida -= 10  # Reducir vida de tanque2
            balas_group.remove(bala)  # Eliminar la bala
            break  # Salir del bucle después de la colisión

# Función que administra la actualización de la pantalla.
def screen_refresh(tank_config, clock, screen, tanque1, tanque2, balas_group):
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

    # En game_functionalities.py, dentro de screen_refresh
    mostrar_niveles_vida(screen, tanque1.vida, tanque2.vida)
    clock.tick(tank_config.fps)
    pygame.display.flip()
