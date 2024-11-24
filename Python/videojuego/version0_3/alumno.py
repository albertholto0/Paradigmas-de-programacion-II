import pygame

# Clase para manipular al alumno
class Alumno:
    # Constructor
    def __init__(self,screen):
        self.screen = screen
        # Se cargan la imagen
        self.image = pygame.image.load("../media/estudianteb.png")
        self.image_rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # Inicializar la posición
        self.image_rect.centerx = self.screen_rect.centerx
        self.image_rect.bottom = self.screen_rect.bottom
        # Bandera
        self.is_moving_right = False
    def update(self):
        if self.is_moving_right:
            self.image_rect.centerx += 5
    # Métod0 que dibuja al alumno en su ubicación
    def blitme(self):
        self.screen.blit(self.image,self.image_rect)
