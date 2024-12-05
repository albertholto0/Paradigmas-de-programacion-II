# Se importan las bibliotecas necesarias
import pygame
from pygame.sprite import Sprite

""" Clase para controlar la laptop (funciona como el arma). """
class Laptop(Sprite):
    # Se define el constructor de la Laptop que hereda del constructor del Sprite.
    def __init__(self, esc_alumnos_conf, screen, alumno):
        # Se llama al constructor de la clase Sprite
        super(Laptop, self).__init__()

        # Se asignan los objetos de las configuraciones, la pantalla y del alumno.
        self.esc_alumnos_config = esc_alumnos_conf
        self.screen = screen
        self.alumno = alumno

        # Se carga la imagen y obtiene el Rect (se utiliza para representar coordenadas rectangulares).
        self.laptop_image = pygame.image.load("../media/rayo.png")
        self.laptop_rect = self.laptop_image.get_rect()
        self.screen_rect = screen.get_rect()

        # Posición inicial de la laptop (centrado con el alumno).
        self.laptop_rect.centerx = self.alumno.image_rect.centerx
        self.laptop_rect.top = self.alumno.image_rect.top

        # Centros del rectángulo utilizando variables flotantes. Esto permite controlar la velocidad porque,
        # por defecto, self.laptop_rect almacenan valores enteros.
        self.laptop_rect_centerx = float(self.laptop_rect.centerx)
        self.laptop_rect_centery = float(self.laptop_rect.centery)

        # Velocidad de la laptop obtenida de las configuraciones.
        self.laptop_speed = self.esc_alumnos_config.laptop_speed

    """ Método para actualizar la posición del alumno."""
    # Al salir disparada la laptop, se debe actualizar únicamente la posición en el eje-y.
    # Por lo tanto, se debe restar un valor para que la dirección sea hacia arriba.
    def update_pos(self):
        # Se actualiza el valor decimal de la posición.
        self.laptop_rect_centery -= self.laptop_speed

        # Se actualiza el valor de la posición del Rect de la laptop.
        self.laptop_rect.centery = self.laptop_rect_centery

    """ Método que dibuja la laptop en la pantalla en su ubicación actual."""
    def blitme(self):
        self.screen.blit(self.laptop_image, self.laptop_rect)
