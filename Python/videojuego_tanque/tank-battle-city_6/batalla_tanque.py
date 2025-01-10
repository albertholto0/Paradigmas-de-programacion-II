import pygame
from config import Config
from Tanque import Tanque
import game_functionalities
from pygame.sprite import Group
import sys
import time
from Pared import Pared

def mostrar_pantalla_inicio(screen):
    """Muestra una pantalla inicial con un botón funcional 'Iniciar'."""
    while True:
        screen.fill((0, 0, 0))  # Fondo negro

        # Cargar y mostrar la imagen en el centro
        imagen_inicio = pygame.image.load("media/inicio_juego.jpg")  # Cambia "inicio.png" al nombre de tu imagen
        imagen_inicio = pygame.transform.scale(imagen_inicio, (420, 400))  # Escalar imagen a 250x250
        imagen_inicio_rect = imagen_inicio.get_rect(center=(screen.get_width() // 2, screen.get_height() // 3.5))
        screen.blit(imagen_inicio, imagen_inicio_rect)

        # Mostrar botón "Iniciar"
        font = pygame.font.Font("media/Pixeled.ttf", 30)  # Fuente personalizada
        texto_iniciar = font.render("Iniciar", True, (255, 255, 255))
        boton_iniciar_rect = texto_iniciar.get_rect(center=(screen.get_width() // 2, imagen_inicio_rect.bottom + 60))
        pygame.draw.rect(screen, (50, 50, 50), boton_iniciar_rect.inflate(20, 10))  # Fondo del botón
        screen.blit(texto_iniciar, boton_iniciar_rect)  # Texto del botón

        pygame.display.flip()

        # Manejar eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Verificar si se hace clic sobre el botón "Iniciar"
                if boton_iniciar_rect.collidepoint(event.pos):
                    return  # Salir de la pantalla de inicio


def run_game():

    clock = pygame.time.Clock()
    pygame.init()
    tank_config = Config()

    screen_size = (tank_config.screen_width, tank_config.screen_height)
    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption(tank_config.game_title)

    mostrar_pantalla_inicio(screen)

    tanque1_position = (screen.get_rect().right - 100, screen.get_rect().centery)
    tanque1 = Tanque(screen, tank_config, position=tanque1_position)

    tanque2_position = (screen.get_rect().left + 100, screen.get_rect().centery)
    tanque2 = Tanque(screen, tank_config, image_path="media/tanque_arena.png", position=tanque2_position)

    pygame.mixer.music.load("media/musica_fondo.mp3")
    pygame.mixer.music.set_volume(0.7)
    pygame.mixer.music.play(-1)

    sonido_disparo = pygame.mixer.Sound("media/disparo.mp3")
    sonido_disparo.set_volume(0.7)
    sonido_vacio = pygame.mixer.Sound("media/vacio.mp3")
    sonido_vacio.set_volume(0.7)

    sonido_derribo_tanque = pygame.mixer.Sound("media/destruccion_pared.mp3")
    sonido_derribo_tanque.set_volume(1)

    grito = pygame.mixer.Sound("media/scream.mp3")
    grito.set_volume(0.7)

    sonido_botiquin = pygame.mixer.Sound("media/recoger_botiquin.mp3")
    sonido_municion = pygame.mixer.Sound("media/recoger_municion.mp3")
    sonido_botiquin.set_volume(0.7)
    sonido_municion.set_volume(0.7)

    balas_group = Group()
    minas_group = Group()
    botiquines = Group()
    municiones = Group()
    pygame.time.set_timer(pygame.USEREVENT, 7500)
    explosiones = []

    paredes = [Pared(screen, *coords) for coords in tank_config.paredes]

    running = True
    while running:
        game_functionalities.game_events(tank_config, screen, tanque1, tanque2, balas_group, botiquines, municiones, sonido_disparo, sonido_vacio, paredes, minas_group)
        game_functionalities.screen_refresh(tank_config, clock, screen, tanque1, tanque2, balas_group, botiquines, municiones, explosiones, paredes, minas_group)
        game_functionalities.manejar_colisiones(tanque1, tanque2, balas_group, botiquines, municiones, sonido_botiquin, sonido_municion, paredes,minas_group)

        balas_group.update()
        minas_group.update()

        for mina in minas_group.copy():
            if  not mina.activo:
                minas_group.remove(mina)

        if tanque1.vida <= 0 or tanque2.vida <= 0:
            tanque_derrotado = "Tanque 1" if tanque1.vida <= 0 else "Tanque 2"
            print(f"El {tanque_derrotado} ha perdido toda su vida. Mostrando pantalla de fin del juego.")
            tanque_rect = tanque1.image_rect if tanque1.vida <= 0 else tanque2.image_rect

            pygame.mixer.music.stop()
            sonido_derribo_tanque.play()
            time.sleep(1)
            grito.play()

            explosion_imagen = pygame.image.load("media/explosion.png")
            explosion_imagen = pygame.transform.scale(explosion_imagen, (tanque_rect.width, tanque_rect.height))
            explosion_rect = explosion_imagen.get_rect(center=tanque_rect.center)
            screen.blit(explosion_imagen, explosion_rect)

            pygame.display.flip()
            time.sleep(5)

            # Pantalla negra con imagen y texto
            screen.fill((0, 0, 0))  # Fondo negro

            # Cargar y mostrar la imagen en el centro superior
            imagen_mensaje = pygame.image.load(
                "media/game_over_tanque.jpg")  # Cambia "imagen_mensaje.png" según el archivo correcto
            imagen_mensaje = pygame.transform.scale(imagen_mensaje, (270, 250))  # Tamaño ajustado a 250x250
            imagen_mensaje_rect = imagen_mensaje.get_rect(center=(screen.get_width() // 2, screen.get_height() // 3.5))

            screen.blit(imagen_mensaje, imagen_mensaje_rect)

            # Mostrar texto debajo de la imagen
            font = pygame.font.Font("media/Pixeled.ttf", 30)  # Fuente personalizada
            mensaje1 = font.render("Fin del juego.", True, (255, 255, 255))
            if tanque_derrotado == "Tanque 1":
                color_nombre = (110, 148, 107)  # Verde
            else:
                color_nombre = (210, 180, 140)  # Arena

            mensaje2 = font.render(f"El {tanque_derrotado} ha sido derribado.", True, color_nombre)

            # Posicionar los textos debajo de la imagen
            mensaje1_rect = mensaje1.get_rect(center=(screen.get_width() // 2, imagen_mensaje_rect.bottom + 40))
            mensaje2_rect = mensaje2.get_rect(center=(screen.get_width() // 2, mensaje1_rect.bottom + 40))

            screen.blit(mensaje1, mensaje1_rect)
            screen.blit(mensaje2, mensaje2_rect)
            pygame.display.flip()

            # Reproducir música de game over
            pygame.mixer.music.load("media/game_over.mp3")
            pygame.mixer.music.set_volume(1)
            pygame.mixer.music.play(0)
            time.sleep(5)

            # Preguntar si desea jugar de nuevo
            jugar_de_nuevo = game_functionalities.preguntar_jugar_de_nuevo(screen)
            if jugar_de_nuevo:
                run_game()  # Reiniciar el juego
            else:
                pygame.quit()
                sys.exit()

"""Código a nivel de módulo"""
# Se ejecuta la función del juego.
run_game()
