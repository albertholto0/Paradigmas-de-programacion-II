# Se importan las bibliotecas requeridas.
import pygame
from pygame.sprite import Sprite
from random import randint

""" Clase de la comida de la serpiente."""
class Food(Sprite):
    def __init__(self, snake_game_configurations, screen, color, snake_body):
        # Se llama al constructor de la clase Sprite.
        super(Food, self).__init__()

        # Se crean los objetos de las configuraciones del juego, la pantalla y del cuerpo de la serpiente.
        self.snake_game_configurations = snake_game_configurations
        self.screen = screen
        self.snake_body = snake_body

        # Se añaden las configuraciones iniciales de la comida.
        self.food_block_size = self.snake_game_configurations.food_block_size
        self.color = color

        # Posición inicial de la comida.
        # Se utiliza un ciclo para verificar que no se encuentre en alguna posición de la serpiente.
        repeat = True
        while repeat:
            # Primero se genera una posición aleatoria en (x, y) para la comida.
            available_pos_x = self.snake_game_configurations.screen_width // self.food_block_size
            available_pos_y = self.snake_game_configurations.screen_height // self.food_block_size
            self.x = randint(0, available_pos_x - 1) * self.food_block_size
            self.y = randint(0, available_pos_y - 1) * self.food_block_size

            # Se verifica que la posición aleatoria no sea la misma que cualquiera del cuerpo de la serpiente.
            # Si alguna se repite, entonces se vuelve a generar la posición aleatoria.
            for snake in self.snake_body.sprites():
                if self.x == snake.x and self.y == snake.y:
                    repeat = True
                    break
                else:
                    repeat = False

    """ Método que dibuja un bloque de la serpiente en la pantalla en su ubicación actual."""
    def blitme(self):
        # Se dibuja el bloque como un rectángulo, de la misma forma que en la clase Snake.
        pygame.draw.rect(self.screen, self.color,[self.x, self.y, self.food_block_size, self.food_block_size])
