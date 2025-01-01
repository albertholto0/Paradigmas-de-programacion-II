"""
Archivo que contiene las funcionalidades del juego:
- Control de todos los eventos.
- Colisiones del juego.
- Fin del juego.
- Movimiento de la serpiente.
- Actualización de los elementos en la pantalla.
"""

# Se importan las bibliotecas necesarias.
import sys
import pygame
from Snake import Snake
from Food import Food

# Banderas de movimiento, en donde se considera que inicialmente no hay movimiento.
is_moving_right = is_moving_left = is_moving_up = is_moving_down = False

""" Función que administra los eventos del juego."""
def game_events():
    # Se indica que las variables modificadas son las variables globales.
    global is_moving_right, is_moving_left, is_moving_up, is_moving_down

    for event in pygame.event.get():
        # El evento es un clic en cerrar el juego.
        if event.type == pygame.QUIT:
            sys.exit()

        # El evento es presionar una tecla.
        elif event.type == pygame.KEYDOWN:
            # Se presiona la tecla 'derecha', implicando un movimiento en esta dirección.
            if event.key == pygame.K_RIGHT:
                is_moving_right = True
                is_moving_left = is_moving_up = is_moving_down = False

            # Se presiona la tecla 'izquierda', implicando un movimiento en esta dirección.
            elif event.key == pygame.K_LEFT:
                is_moving_left = True
                is_moving_right = is_moving_up = is_moving_down = False

            # Se presiona la tecla 'arriba', implicando un movimiento en esta dirección.
            elif event.key == pygame.K_UP:
                is_moving_up = True
                is_moving_left = is_moving_right = is_moving_down = False

            # Se presiona la tecla 'abajo', implicando un movimiento en esta dirección.
            elif event.key == pygame.K_DOWN:
                is_moving_down = True
                is_moving_right = is_moving_left = is_moving_up = False

"""¡NUEVO! Ahora recibe el objeto media con el contenido multimedia."""
"""Función de las colisiones del juego: serpiente-comida, serpiente-pantalla y serpiente-serpiente."""
def check_collisions(snake_game_configurations, screen, snake_body, food_group, media):
    # Variables utilizadas.
    game_over = False
    snake_head = snake_body.sprites()[0]
    food = food_group.sprites()[0]
    screen_width = snake_game_configurations.screen_width
    screen_height = snake_game_configurations.screen_height
    body_size = len(snake_body.sprites())
    # Se verifica la colisión de la cabeza de la serpiente - comida.
    # En este caso, se tiene que agregar un nuevo objeto de la clase Food y eliminar el anterior.
    # De igual manera, se tiene que incrementar el tamaño de la serpiente.
    # Finalmente, se reproduce el sonido correspondiente.
    if snake_head.x == food.x and snake_head.y == food.y:
        # Se elimina la comida.
        food_group.remove(food)

        # Se agrega una nueva comida.
        new_food = Food(snake_game_configurations, screen, snake_game_configurations.food_color, snake_body)
        food_group.add(new_food)

        # Se incrementa el tamaño de la serpiente.
        new_snake = Snake(snake_game_configurations, screen, snake_game_configurations.snake_body_color)
        snake_body.add(new_snake)

        """NUEVO"""
        # Se reproduce el sonido correspondiente.
        media.play_eaten_sound()

    # Se verifican las colisiones cabeza de la serpiente - bordes de la pantalla.
    if not (0 <= snake_head.x <= screen_width) or not (0 <= snake_head.y <= screen_height):
        game_over = True

    # Se verifican las colisiones cabeza de la serpiente - serpiente.
    if not game_over:
        for i in range(1, body.size):
            if snake_head.x == snake_body.sprites()[i].x and snake_head.y == snake_body.sprites()[i].y:
                game_over = True
                break

    # Se devuelve la bandera.
    return game_over

"""Función del fin del juego."""

def game_over_fun(media):
    """NUEVO."""
    # Se reproduce el sonido del fin del juego y se detiene la música de fondo.
    media.play_game_over_sound()
    pygame.mixer.music.stop()

    """NUEVO."""
    # Se muestran las imágenes del fin del juego y de los créditos. Cabe mencionar que se actualiza la pantalla
    # para que muestre las imágenes en la pantalla.
    media.blit_game_over()
    media.blit_credits()
    pygame.display.flip()

    # Pausa para que el jugador note que ha perdido.
    pygame.time.delay(4000)

""" Función que administra el movimiento de la serpiente."""

def update_snake(snake_game_configurations, snake_body):
    # Se actualiza el movimiento de todos los bloques, asignándole a cada bloque la posición
    # que tiene su bloque predecesor.
    body_size = len(snake_body.sprites()) - 1
    for i in range(body_size, 0, -1):
        snake_body.sprites()[i].x = snake_body.sprites()[i - 1].x
        snake_body.sprites()[i].y = snake_body.sprites()[i - 1].y

    # Para el caso del movimiento de la cabeza, se verifican las banderas.
    if is_moving_right:
        snake_body.sprites()[0].x += snake_game_configurations.snake_block_size

    elif is_moving_left:
        snake_body.sprites()[0].x -= snake_game_configurations.snake_block_size

    elif is_moving_up:
        snake_body.sprites()[0].y -= snake_game_configurations.snake_block_size

    elif is_moving_down:
        snake_body.sprites()[0].y += snake_game_configurations.snake_block_size

    """NUEVO. Ahora se muestra una imagen en lugar de un color sólido, por lo que ya no se requiere el objeto screen, pero sí el objeto media con el contenido multimedia."""
    """Función que administra los elementos en la pantalla."""


def screen_refresh(snake_game_configurations, clock, snake_body, food_group, media):
    # Se muestra el fondo de la pantalla.
    media.blit_background()

    """NUEVO."""
    # Se muestra el marcador, el cual es el tamaño del cuerpo de la serpiente.
    score = len(snake_body) - 1
    media.update_score(score)

    # Se dibuja la serpiente.
    for snake in snake_body.sprites():
        snake.blitme()

    # Se dibuja la comida de la serpiente.
    for food in food_group.sprites():
        food.blitme()

    # Se actualiza la pantalla, dando la impresión visual de movimiento.
    clock.tick(snake_game_configurations.fps)
    pygame.display.flip()
