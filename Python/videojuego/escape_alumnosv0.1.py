import sys
import pygame

# Funcion para inicializar el juego
def run_game():
    pygame.init()

    # Estas dos líneas sirven para inicializar la pantalla
    screen = (1080, 720)
    display = pygame.display.set_mode(screen)
    game_title = "Escape de alumnos"
    # Muestra el titulo del juego
    pygame.display.set_caption(game_title)

    running = True
    # Evento o acción que realiza el usuario, como cosas del ratón o del teclado. Por eso siempre se usa el ciclo while, porque siempre vamos a estar buscando eventos
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            background_color = (212,230,241)
            display.fill(background_color)
            pygame.display.flip()   #Actualiza la pantalla con los cambios realizados (ilusión de movimiento)
## Código a nivel de módulo
run_game()