import pygame
from pygame.sprite import Sprite

class Bala(Sprite):
    """ Clase para controlar la bala (funciona como el arma). """
    def __init__(self, tank_config, screen, tanque):
        # Se llama al constructor de la clase Sprite
        super(Bala, self).__init__()

        # Se asignan los objetos de las configuraciones, la pantalla y del tanque.
        self.tank_config = tank_config
        self.screen = screen
        self.tanque = tanque

        # Se carga la imagen y obtiene el Rect (se utiliza para representar coordenadas rectangulares).
        self.bala_image = pygame.image.load("media/bala.png")
        self.bala_rect = self.bala_image.get_rect()
        self.screen_rect = screen.get_rect()

        # Ajustamos la posición inicial de la bala según la dirección del tanque.
        if self.tanque.direction == 'right':
            self.bala_rect.centerx = self.tanque.image_rect.right  # Se ajusta para disparar desde el borde derecho
            self.bala_rect.centery = self.tanque.image_rect.centery  # Centrado verticalmente con el tanque
        elif self.tanque.direction == 'left':
            self.bala_rect.centerx = self.tanque.image_rect.left  # Se ajusta para disparar desde el borde izquierdo
            self.bala_rect.centery = self.tanque.image_rect.centery  # Centrado verticalmente con el tanque
        elif self.tanque.direction == 'up':
            self.bala_rect.centerx = self.tanque.image_rect.centerx  # Centrado horizontalmente con el tanque
            self.bala_rect.bottom = self.tanque.image_rect.top  # Posición inicial en la parte superior del tanque
        elif self.tanque.direction == 'down':
            self.bala_rect.centerx = self.tanque.image_rect.centerx  # Centrado horizontalmente con el tanque
            self.bala_rect.top = self.tanque.image_rect.bottom  # Posición inicial en la parte inferior del tanque

        # Centros del rectángulo utilizando variables flotantes.
        self.bala_rect_centerx = float(self.bala_rect.centerx)
        self.bala_rect_centery = float(self.bala_rect.centery)

        # Velocidad de la bala obtenida de las configuraciones.
        self.bala_speed = self.tank_config.bala_speed

        # Dirección de la bala (se ajusta según la dirección del tanque)
        self.direction = self.tanque.direction

        # Ajustar la imagen de la bala según la dirección del tanque
        self.rotate_bala_image()

    """ Método para actualizar la posición de la bala. """
    def update_pos(self):
        # Actualizar la posición según la dirección del tanque
        if self.direction == 'up':
            self.bala_rect_centery -= self.bala_speed
        elif self.direction == 'down':
            self.bala_rect_centery += self.bala_speed
        elif self.direction == 'left':
            self.bala_rect_centerx -= self.bala_speed
        elif self.direction == 'right':
            self.bala_rect_centerx += self.bala_speed

        # Se actualiza el valor de la posición del Rect de la bala
        self.bala_rect.centerx = self.bala_rect_centerx
        self.bala_rect.centery = self.bala_rect_centery

    """ Método que dibuja la bala en la pantalla en su ubicación actual. """
    def blitme(self):
        self.screen.blit(self.bala_image, self.bala_rect)

    """ Método para rotar la imagen de la bala según la dirección del tanque. """
    def rotate_bala_image(self):
        if self.direction == 'right':
            self.bala_image = pygame.transform.rotate(pygame.image.load("media/bala.png"), 270)  # 270° hacia la derecha
        elif self.direction == 'left':
            self.bala_image = pygame.transform.rotate(pygame.image.load("media/bala.png"), 90)  # 90° hacia la izquierda
        elif self.direction == 'up':
            self.bala_image = pygame.image.load("media/bala.png")  # Mantener la imagen original para arriba
        elif self.direction == 'down':
            self.bala_image = pygame.transform.rotate(pygame.image.load("media/bala.png"), 180)  # 180° hacia abajo

        self.bala_rect = self.bala_image.get_rect(center=self.bala_rect.center)