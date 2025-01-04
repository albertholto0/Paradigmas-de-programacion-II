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

def crear_recurso(screen, tipo, image_path):
    """Crea un recurso (botiquin o munición) en una posición aleatoria."""
    x = random.randint(0, screen.get_width() - 50)
    y = random.randint(0, screen.get_height() - 50)
    recurso = Recurso(screen, tipo, image_path, (x, y))
    return recurso

def generar_recursos(screen, botiquines, municiones):
    """Genera recursos de manera periódica."""
    tipo_recurso = random.choice(['botiquin', 'municion'])
    if tipo_recurso == 'botiquin':
        nuevo_botiquin = crear_recurso(screen, 'botiquin', 'media/botiquin.png')
        botiquines.add(nuevo_botiquin)
    else:
        nueva_municion = crear_recurso(screen, 'municion', 'media/municion.png')
        municiones.add(nueva_municion)
