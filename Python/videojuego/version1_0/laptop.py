import pygame
from pygame.sprite import Sprite

class Laptop (Sprite):
    def __init__(self,esc_alumnos_config,screen,alumno):
        super(Laptop,self).__init__()
        self.esc_alumnos_config = esc_alumnos_config
        self.screen = screen
        self.alumno = alumno

        self.image = pygame.image.load("../media/rayo.png")
        self.image_rect = self.image.get_rect()
        self.alumno_rect = self.alumno.get_rect()

        self.image_rect.centerx = self.alumno_rect.centerx
        self.image_rect.bottom = self.alumno_rect.top

        self.image_rect_centerx = float(self.image_rect.centerx)
        self.image_rect_centery = float(self.image_rect.centery)

        self.laptop_speed = self.esc_alumnos_config.laptop_speed
