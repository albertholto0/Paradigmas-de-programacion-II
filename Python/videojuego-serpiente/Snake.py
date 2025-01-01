# Nombre del archivo: Snake.py

# Se importan las bibliotecas requeridas.
import pygame
from pygame.sprite import Sprite

""" Clase de un bloque (cuerpo) de la serpiente."""
class Snake(Sprite):
    def __init__(self, snake_game_configurations, screen, color):
        # Se llama al constructor de la clase Sprite.
        super(Snake, self).__init__()

        # Se crean los objetos de las configuraciones del juego y de la pantalla.
        self.snake_game_configurations = snake_game_configurations
        self.screen = screen

        # Se añaden las configuraciones iniciales de la serpiente.
        self.snake_block_size = self.snake_game_configurations.snake_block_size
        self.color = color

        # Posición inicial de la serpiente en el centro de la pantalla.
        self.x = (self.snake_game_configurations.screen_width // (2 * self.snake_block_size)) * self.snake_block_size
        self.y = (self.snake_game_configurations.screen_height // (2 * self.snake_block_size)) * self.snake_block_size

    """ Método que dibuja un bloque de la serpiente en la pantalla en su ubicación actual."""
    def blitme(self):
        # Se dibuja el bloque como un rectángulo utilizando la función de pygame.
        # Los argumentos que recibe la función son los siguientes:
        # (la pantalla, el color del rectángulo, [pos en x, pos en y, el ancho en x, el ancho en y]).
        # En este caso, se dibuja un cuadrado de tamaño del snake_block_size.
        pygame.draw.rect(self.screen, self.color,
                         [self.x, self.y, self.snake_block_size, self.snake_block_size])
