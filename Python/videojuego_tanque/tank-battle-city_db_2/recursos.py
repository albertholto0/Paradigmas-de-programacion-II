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
    for pared in paredes:
        if rect.colliderect(pared.rect):
            return True
    return False

def verificar_colision_con_tanques(rect, tanque1, tanque2):
    if rect.colliderect(tanque1.image_rect) or rect.colliderect(tanque2.image_rect):
        return True
    return False

def crear_recurso(screen, tipo, image_path, paredes, tanque1, tanque2):
    while True:
        x = random.randint(0, screen.get_width() - 50)
        y = random.randint(0, screen.get_height() - 50)
        nuevo_rect = pygame.Rect(x, y, 50, 50)  # Tamaño de 50x50 para el recurso

        if not verificar_colision_con_paredes(nuevo_rect, paredes) and not verificar_colision_con_tanques(nuevo_rect, tanque1, tanque2):
            return Recurso(screen, tipo, image_path, (x, y))

def generar_recursos(screen, botiquines, municiones, paredes, tanque1, tanque2):
    tipo_recurso = random.choice(['botiquin', 'municion'])
    if tipo_recurso == 'botiquin':
        nuevo_botiquin = crear_recurso(screen, 'botiquin', 'media/botiquin.png', paredes, tanque1, tanque2)
        botiquines.add(nuevo_botiquin)
    else:
        nueva_municion = crear_recurso(screen, 'municion', 'media/municion.png', paredes, tanque1, tanque2)
        municiones.add(nueva_municion)