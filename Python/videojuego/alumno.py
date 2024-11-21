import pygame

# Clase para manipular al alumno
class Alumno:
    # Constructor
    def __init__(self,screen):
        self.screen = screen
        # Se cargan la imagen
        self.image = pygame.image.load()
        self.screen_rect = screen.get_rect()