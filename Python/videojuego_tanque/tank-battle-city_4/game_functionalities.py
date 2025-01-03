# Se importan las bibliotecas necesarias.
import sys
import pygame
from Bala import Bala

def game_events(tank_config, screen, tanque1, tanque2, balas_group, sonido_disparo, sonido_vacio):
    # Se revisan los eventos del juego.
    for event in pygame.event.get():
        # El evento es un clic en cerrar el juego.
        if event.type == pygame.QUIT:
            sys.exit()

        # El evento es presionar una tecla.
        elif event.type == pygame.KEYDOWN:
            game_events_keydown(event, tank_config, screen, tanque1, tanque2, balas_group, sonido_disparo, sonido_vacio)

        # El evento es soltar una tecla.
        elif event.type == pygame.KEYUP:
            game_events_keyup(event, tanque1, tanque2)

def game_events_keydown(event, tank_config, screen, tanque1, tanque2, balas_group, sonido_disparo, sonido_vacio):
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

    elif event.key == pygame.K_RETURN:
        if tanque1.balas_disparadas < tanque1.max_balas:
            new_bala = Bala(tank_config, screen, tanque1)
            balas_group.add(new_bala)
            tanque1.balas_disparadas += 1
            sonido_disparo.play()
        else:
            print("Tanque 1 no puede disparar más balas.")
            sonido_vacio.play()

    elif event.key == pygame.K_SPACE:
        if tanque2.balas_disparadas < tanque2.max_balas:
            new_bala = Bala(tank_config, screen, tanque2)
            balas_group.add(new_bala)
            tanque2.balas_disparadas += 1
            sonido_disparo.play()
        else:
            print("Tanque 2 no puede disparar más balas.")
            sonido_vacio.play()

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
def mostrar_niveles_vida(screen, vida_tanque1, vida_tanque2, tanque1, tanque2):
    font = pygame.font.Font("media/Pixeled.ttf", 14)  # Fuente personalizada
    # Mostrar niveles de vida
    vida_texto_2 = font.render(f"Tanque Verde: {vida_tanque1}", True, (13, 69, 23))
    vida_texto_1 = font.render(f"Tanque Arena: {vida_tanque2}", True, (92, 56, 2))

    # Mostrar contador de balas
    balas_texto_2 = font.render(f"Balas: {tanque1.max_balas - tanque1.balas_disparadas}", True, (13, 69, 23))
    balas_texto_1 = font.render(f"Balas: {tanque2.max_balas - tanque2.balas_disparadas}", True, (92, 56, 2))

    # Posiciones de los textos
    screen.blit(vida_texto_1, (10, 10))  # Vida del Tanque Arena (izquierda)
    screen.blit(balas_texto_1, (10, 30))  # Balas del Tanque Arena (debajo de la vida)

    screen.blit(vida_texto_2,
                (screen.get_width() - vida_texto_2.get_width() - 10, 10))  # Vida del Tanque Verde (derecha)
    screen.blit(balas_texto_2, (screen.get_width() - balas_texto_2.get_width() - 10, 30))  # Balas del Tanque Verde

def manejar_colisiones(tanque1, tanque2, balas_group):
    """Maneja las colisiones de balas con los tanques y elimina las balas fuera de la pantalla."""
    for bala in list(balas_group):  # Usamos una lista para evitar problemas al eliminar elementos durante la iteración
        # Verificar si la bala está fuera de la pantalla
        if bala.bala_rect.bottom < 0 or bala.bala_rect.top > bala.screen_rect.height or \
           bala.bala_rect.right < 0 or bala.bala_rect.left > bala.screen_rect.width:
            balas_group.remove(bala)
            continue

        # Verificar colisiones con los tanques
        if bala.tanque != tanque1 and tanque1.image_rect.colliderect(bala.bala_rect):
            tanque1.vida -= 10
            balas_group.remove(bala)
        elif bala.tanque != tanque2 and tanque2.image_rect.colliderect(bala.bala_rect):
            tanque2.vida -= 10
            balas_group.remove(bala)


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
            if bala.origen == tanque1:
                tanque1.balas_disparadas = max(0, tanque1.balas_disparadas - 1)
            elif bala.origen == tanque2:
                tanque2.balas_disparadas = max(0, tanque2.balas_disparadas - 1)

    for bala in balas_group.sprites():
        bala.update_pos()
        bala.blitme()

    mostrar_niveles_vida(screen, tanque1.vida, tanque2.vida, tanque1, tanque2)
    clock.tick(tank_config.fps)
    pygame.display.flip()
