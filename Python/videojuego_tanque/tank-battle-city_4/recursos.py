import pygame
import random

class Recurso(pygame.sprite.Sprite):
    def __init__(self, screen, tipo, image_path, position):
        super().__init__()
        self.screen = screen
        self.tipo = tipo  # Puede ser 'botiquin' o 'municion'
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.topleft = position

    def blitme(self):
        """Dibuja el recurso en la pantalla."""
        self.screen.blit(self.image, self.rect)

def crear_recursos(screen, num_recursos, tipo, image_path):
    """Crea una lista de recursos (botiquines o munición) en posiciones aleatorias."""
    recursos = pygame.sprite.Group()
    for _ in range(num_recursos):
        x = random.randint(0, screen.get_width() - 50)
        y = random.randint(0, screen.get_height() - 50)
        recurso = Recurso(screen, tipo, image_path, (x, y))
        recursos.add(recurso)
    return recursos
