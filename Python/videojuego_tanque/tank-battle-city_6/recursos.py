import pygame
import random

class Recurso(pygame.sprite.Sprite):
    def __init__(self, screen, tipo, image_path, position):
        super().__init__()
        self.screen = screen
        self.tipo = tipo
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.topleft = position

    def blitme(self):
        self.screen.blit(self.image, self.rect)

def verificar_colision_con_paredes(rect, paredes):
    # Verifica si la posición del recurso colide con alguna pared
    for pared in paredes:
        if rect.colliderect(pared.rect):
            return True
    return False

def crear_recurso(screen, tipo, image_path, paredes):
    # Intentamos generar una posición aleatoria que no colisione con las paredes
    while True:
        x = random.randint(0, screen.get_width() - 50)
        y = random.randint(0, screen.get_height() - 50)
        nuevo_rect = pygame.Rect(x, y, 50, 50)  # Tamaño de 50x50 para el recurso

        if not verificar_colision_con_paredes(nuevo_rect, paredes):
            return Recurso(screen, tipo, image_path, (x, y))

def generar_recursos(screen, botiquines, municiones, paredes):
    tipo_recurso = random.choice(['botiquin', 'municion'])
    if tipo_recurso == 'botiquin':
        nuevo_botiquin = crear_recurso(screen, 'botiquin', 'media/botiquin.png', paredes)
        botiquines.add(nuevo_botiquin)
    else:
        nueva_municion = crear_recurso(screen, 'municion', 'media/municion.png', paredes)
        municiones.add(nueva_municion)