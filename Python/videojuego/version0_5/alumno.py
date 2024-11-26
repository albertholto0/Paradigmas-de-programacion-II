import pygame

# Clase para manipular al alumno
class Alumno:
    # Constructor
    def __init__(self,screen):
        self.screen = screen
        # Se cargan la imagen
        self.image = pygame.image.load("../media/pikachu.png")
        self.image_rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # Inicializar la posición
        self.image_rect.centerx = self.screen_rect.centerx
        self.image_rect.bottom = self.screen_rect.bottom
        self.is_moving_right = False
        self.is_moving_left = False
        self.is_moving_up = False
        self.is_moving_down = False
    # Métod0 que dibuja al alumno en su ubicación
    def blitme(self):
        self.screen.blit(self.image,self.image_rect)
    def update(self):
        if self.is_moving_right and self.image_rect.right < self.screen_rect.right:
            self.image_rect.centerx += 1
        if self.is_moving_left and self.image_rect.left > 0:
            self.image_rect.centerx -= 1
        if self.is_moving_up and self.image_rect.top > 0:
            self.image_rect.centery -= 1
        if self.is_moving_down and self.image_rect.bottom < self.screen_rect.bottom:
            self.image_rect.centery += 1

    # para mañana un ensayo d pq quiero ser programador
