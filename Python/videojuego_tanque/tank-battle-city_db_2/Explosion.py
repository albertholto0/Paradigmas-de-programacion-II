import pygame

class Explosion:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.image = pygame.image.load("media/explosion.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.tiempo_inicio = pygame.time.get_ticks()
        self.duracion = 500
        self.activa = True

    def update(self):
        tiempo_actual = pygame.time.get_ticks()
        if tiempo_actual - self.tiempo_inicio > self.duracion:
            self.activa = False

    def blitme(self):
        if self.activa:
            self.screen.blit(self.image, self.rect)