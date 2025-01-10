import sys
import pygame
from Bala import Bala
from recursos import generar_recursos
from Explosion import Explosion
from mina import Mina
explosiones = []

def game_events(tank_config, screen, tanque1, tanque2, balas_group, botiquines, municiones, sonido_disparo, sonido_vacio, paredes,  minas_group):
    # Se revisan los eventos del juego.
    for event in pygame.event.get():
        # El evento es un clic en cerrar el juego.
        if event.type == pygame.QUIT:
            sys.exit()

        # El evento es presionar una tecla.
        elif event.type == pygame.KEYDOWN:
            game_events_keydown(event, tank_config, screen, tanque1, tanque2, balas_group, sonido_disparo, sonido_vacio, minas_group)

        # El evento es soltar una tecla.
        elif event.type == pygame.KEYUP:
            game_events_keyup(event, tanque1, tanque2)

        elif event.type == pygame.USEREVENT:
            generar_recursos(screen, botiquines, municiones, paredes, tanque1, tanque2)

def game_events_keydown(event, tank_config, screen, tanque1, tanque2, balas_group, sonido_disparo, sonido_vacio,  minas_group):
    sonido_tiempo_mina = pygame.mixer.Sound("media/contador_mina.mp3")
    sonido_tiempo_mina.set_volume(1)
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

    # Minas
    elif event.key == pygame.K_0:
        if tanque1.minas_disponibles > 0:
            nueva_mina = Mina(screen, tanque1.image_rect.centerx, tanque1.image_rect.centery, tanque1)
            minas_group.add(nueva_mina)
            tanque1.minas_disponibles -= 1
            sonido_tiempo_mina.play()
    elif event.key == pygame.K_f:
            if tanque2.minas_disponibles > 0:
                nueva_mina = Mina(screen, tanque2.image_rect.centerx, tanque2.image_rect.centery, tanque2)
                minas_group.add(nueva_mina)
                tanque2.minas_disponibles -= 1
                sonido_tiempo_mina.play()

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

    # Mostrar minas disponibles
    minas_texto_2 = font.render(f"Minas: {tanque1.minas_disponibles}", True, (13, 69, 23))
    minas_texto_1 = font.render(f"Minas: {tanque2.minas_disponibles}", True, (92, 56, 2))

    # Posiciones de los textos
    screen.blit(vida_texto_1, (10, 10))  # Vida del Tanque Arena
    screen.blit(balas_texto_1, (10, 30))  # Balas del Tanque Arena
    screen.blit(minas_texto_1, (10, 50))  # Minas del Tanque Arena

    screen.blit(vida_texto_2, (screen.get_width() - vida_texto_2.get_width() - 10, 10))  # Vida del Tanque Verde
    screen.blit(balas_texto_2, (screen.get_width() - balas_texto_2.get_width() - 10, 30))  # Balas del Tanque Verde
    screen.blit(minas_texto_2, (screen.get_width() - minas_texto_2.get_width() - 10, 50))  # Minas del Tanque Verde


def manejar_colisiones(tanque1, tanque2, balas_group, botiquines, municiones, sonido_botiquin, sonido_municion, paredes,
                       minas_group):
    sonido_colision = pygame.mixer.Sound("media/colision_bala_tanque.mp3")
    sonido_colision.set_volume(1)
    sonido_colision_pared = pygame.mixer.Sound("media/colision_pared.mp3")
    sonido_colision_pared.set_volume(1)

    for bala in list(balas_group):
        if bala.bala_rect.bottom < 0 or bala.bala_rect.top > bala.screen_rect.height or \
                bala.bala_rect.right < 0 or bala.bala_rect.left > bala.screen_rect.width:
            balas_group.remove(bala)
            continue

        # Colisión con paredes
        for pared in paredes:
            if bala.bala_rect.colliderect(pared.rect):
                sonido_colision_pared.play()
                balas_group.remove(bala)
                explosiones.append(Explosion(bala.screen, bala.bala_rect.centerx, bala.bala_rect.centery))
                break

        # Colisiones con tanques
        if bala.tanque != tanque1 and tanque1.image_rect.colliderect(bala.bala_rect):
            sonido_colision.play()
            tanque1.vida -= 10
            balas_group.remove(bala)
            explosiones.append(Explosion(bala.screen, bala.bala_rect.centerx, bala.bala_rect.centery))
        elif bala.tanque != tanque2 and tanque2.image_rect.colliderect(bala.bala_rect):
            sonido_colision.play()
            tanque2.vida -= 10
            balas_group.remove(bala)
            explosiones.append(Explosion(bala.screen, bala.bala_rect.centerx, bala.bala_rect.centery))

    # Colisiones con minas
    for mina in minas_group:
        if mina.exploded and mina.activo:
            for explosion_rect in mina.explosion_rects:
                if explosion_rect.colliderect(tanque1.image_rect):
                    mina.aplicar_dano(tanque1)
                elif explosion_rect.colliderect(tanque2.image_rect):
                    mina.aplicar_dano(tanque2)


    # Colisiones con botiquines
    for botiquin in list(botiquines):
        if tanque1.image_rect.colliderect(botiquin.rect):
            tanque1.vida = min(100, tanque1.vida + 20)
            botiquines.remove(botiquin)
            sonido_botiquin.play()
        elif tanque2.image_rect.colliderect(botiquin.rect):
            tanque2.vida = min(100, tanque2.vida + 20)
            botiquines.remove(botiquin)
            sonido_botiquin.play()

    # Colisiones con municiones
    for municion in list(municiones):
        if tanque1.image_rect.colliderect(municion.rect):
            tanque1.balas_disparadas = max(0, tanque1.balas_disparadas - 5)
            municiones.remove(municion)
            sonido_municion.play()
        elif tanque2.image_rect.colliderect(municion.rect):
            tanque2.balas_disparadas = max(0, tanque2.balas_disparadas - 5)
            municiones.remove(municion)
            sonido_municion.play()


def preguntar_jugar_de_nuevo(screen):
    font = pygame.font.Font("media/Pixeled.ttf", 25)
    while True:
        screen.fill((0, 0, 0))  # Fondo negro
        mensaje = font.render("¿Jugar de nuevo?", True, (255, 255, 255))
        si_boton = font.render("[SI]", True, (0, 255, 0))
        no_boton = font.render("[NO]", True, (255, 0, 0))

        mensaje_rect = mensaje.get_rect(center=(screen.get_width() // 2, screen.get_height() // 3))
        si_rect = si_boton.get_rect(center=(screen.get_width() // 3, screen.get_height() // 2))
        no_rect = no_boton.get_rect(center=(2 * screen.get_width() // 3, screen.get_height() // 2))

        screen.blit(mensaje, mensaje_rect)
        screen.blit(si_boton, si_rect)
        screen.blit(no_boton, no_rect)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if si_rect.collidepoint(event.pos):
                    return True  # Reiniciar el juego
                if no_rect.collidepoint(event.pos):
                    return False  # Salir del juego

def screen_refresh(tank_config, clock, screen, tanque1, tanque2, balas_group, botiquines, municiones, explo, paredes, minas_group):
    background = pygame.image.load(tank_config.background_image_path)
    background = pygame.transform.scale(background, (tank_config.screen_width, tank_config.screen_height))
    screen.blit(background, (0, 0))

    prev_pos_tanque1 = tanque1.image_rect.topleft
    prev_pos_tanque2 = tanque2.image_rect.topleft

    tanque1.update_pos(tanque2, paredes)
    tanque2.update_pos(tanque1, paredes)

    tanque1.blitme()
    tanque2.blitme()

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

    for botiquin in botiquines.sprites():
        botiquin.blitme()

    for municion in municiones.sprites():
        municion.blitme()

    for pared in paredes:
        pared.blitme()

    for explosion in explo:
        explosion.update()
        explosion.blitme()

    explo = [explosion for explosion in explo if explosion.activa]  # Eliminar explosiones inactivas
    for explosion in explosiones[:]:
        explosion.update()
        if not explosion.activa:
            explosiones.remove(explosion)
        else:
            explosion.blitme()

    for mina in minas_group.copy():
        mina.update()
        mina.blitme()
        if not mina.activo:
            minas_group.remove(mina)

    mostrar_niveles_vida(screen, tanque1.vida, tanque2.vida, tanque1, tanque2)
    clock.tick(tank_config.fps)
    pygame.display.flip()
