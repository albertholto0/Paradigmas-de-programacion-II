# Se importan las bibliotecas requeridas.
import pygame
from pygame.sprite import Sprite

""" Clase para controlar el hacker (funciona como el enemigo). """
class Hacker(Sprite):
    # Se define el constructor del Hacker que hereda del constructor del Sprite.
    def __init__(self, esc_alumnos_config, screen):
        # Se llama al constructor de la clase Sprite.
        super(Hacker, self).__init__()

        # Se crean los objetos de la pantalla y de las configuraciones del juego.
        self.screen = screen
        self.esc_alumnos_config = esc_alumnos_config

        # Se carga la imagen y obtiene el Rect (se utiliza para representar coordenadas rectangulares).
        self.hacker_image = pygame.image.load("../media/team_rocket.png")
        self.hacker_rect = self.hacker_image.get_rect()
        self.screen_rect = screen.get_rect()

        # Posición inicial del hacker (en el eje-x y en el eje-y). En este caso, se deja la distancia de
        # un hacker a la derecha y de la parte superior.
        self.hacker_rect.x = self.hacker_rect.width
        self.hacker_rect.y = self.hacker_rect.height

        # Centros del rectángulo utilizando variables flotantes. Esto permite controlar la velocidad porque,
        # por defecto, self.hacker_rect.x y self.hacker_rect.y almacenan valores enteros.
        self.hacker_rect_x = float(self.hacker_rect.x)
        self.hacker_rect_y = float(self.hacker_rect.y)

        # Velocidad del hacker obtenida de las configuraciones.
        self.hacker_speed = self.esc_alumnos_config.hacker_speed

    """ Método que dibuja el hacker en la pantalla en su ubicación actual."""
    def blitme(self):
        self.screen.blit(self.hacker_image, self.hacker_rect)
