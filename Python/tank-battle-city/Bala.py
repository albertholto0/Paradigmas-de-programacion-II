# Se importan las bibliotecas necesarias
import pygame
from pygame.sprite import Sprite

""" Clase para controlar la bala (funciona como el arma). """
class Bala(Sprite):
    # Se define el constructor de la Laptop que hereda del constructor del Sprite.
    def __init__(self, tank_config, screen, tanque):
        # Se llama al constructor de la clase Sprite
        super(Bala, self).__init__()

        # Se asignan los objetos de las configuraciones, la pantalla y del alumno.
        self.tank_config = tank_config
        self.screen = screen
        self.tanque = tanque

        # Se carga la imagen y obtiene el Rect (se utiliza para representar coordenadas rectangulares).
        self.bala_image = pygame.image.load("media/bala.png")
        self.bala_rect = self.bala_image.get_rect()
        self.screen_rect = screen.get_rect()

        # Posición inicial de la laptop (centrado con el alumno).
        self.bala_rect.centerx = self.tanque.image_rect.centerx
        self.bala_rect.top = self.tanque.image_rect.top

        # Centros del rectángulo utilizando variables flotantes. Esto permite controlar la velocidad porque,
        # por defecto, self.laptop_rect almacenan valores enteros.
        self.bala_rect_centerx = float(self.bala_rect.centerx)
        self.bala_rect_centery = float(self.bala_rect.centery)

        # Velocidad de la laptop obtenida de las configuraciones.
        self.bala_speed = self.tank_config.bala_speed

    """ Método para actualizar la posición del alumno."""
    # Al salir disparada la laptop, se debe actualizar únicamente la posición en el eje-y.
    # Por lo tanto, se debe restar un valor para que la dirección sea hacia arriba.
    def update_pos(self):
        # Se actualiza el valor decimal de la posición.
        self.bala_rect_centery -= self.bala_speed

        # Se actualiza el valor de la posición del Rect de la laptop.
        self.bala_rect.centery = self.bala_rect_centery

    """ Método que dibuja la laptop en la pantalla en su ubicación actual."""
    def blitme(self):
        self.screen.blit(self.bala_image, self.bala_rect)