import pygame

class Pared:
    def __init__(self, screen, x, y, width, height):
        self.screen = screen
        self.image = pygame.image.load("media/pared.png")
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def blitme(self):
        self.screen.blit(self.image, self.rect)
