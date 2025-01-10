import pygame
from pygame.sprite import Sprite

class Mina(Sprite):
    def __init__(self, screen, x, y, tanque_propietario, paredes):
        super(Mina, self).__init__()
        self.screen = screen
        self.image = pygame.image.load("media/bomba.png")
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.explosion_time = pygame.time.get_ticks() + 2000
        self.exploded = False
        self.explosion_end_time = None
        self.activo = True
        self.explosion_image = pygame.image.load("media/fuego.png")
        self.explosion_image = pygame.transform.scale(self.explosion_image, (25, 25))
        self.explosion_rects = []
        self.tanque_propietario = tanque_propietario
        self.paredes = paredes
        self.damage_cooldown = 1000
        self.last_damage_time = {}

    def blitme(self):
        if not self.exploded:
            self.screen.blit(self.image, self.rect)
        elif self.exploded and pygame.time.get_ticks() < self.explosion_end_time:
            self.dibujar_explosion()

    def update(self):
        if pygame.time.get_ticks() >= self.explosion_time and not self.exploded:
            self.explotar()
            self.exploded = True
            self.explosion_end_time = pygame.time.get_ticks() + 2000
        elif self.exploded and pygame.time.get_ticks() >= self.explosion_end_time:
            self.activo = False

    def explotar(self):
        print(f"Explosión en forma de cruz iniciada en ({self.rect.centerx}, {self.rect.centery})")
        self.dibujar_explosion()
        sonido_quemarse = pygame.mixer.Sound("media/explosion_mina.mp3")
        sonido_quemarse.set_volume(1)
        sonido_quemarse.play()

    def dibujar_explosion(self):
        self.explosion_rects = []
        screen_width, screen_height = self.screen.get_size()
        x, y = self.rect.center

        for i in range(x - 12, -25, -25):
            rect = pygame.Rect(i, y - 12, 25, 25)
            if any(pared.rect.colliderect(rect) for pared in self.paredes):
                break
            self.screen.blit(self.explosion_image, rect)
            self.explosion_rects.append(rect)

        for i in range(x + 12, screen_width, 25):
            rect = pygame.Rect(i, y - 12, 25, 25)
            if any(pared.rect.colliderect(rect) for pared in self.paredes):
                break
            self.screen.blit(self.explosion_image, rect)
            self.explosion_rects.append(rect)

        for i in range(y - 12, -25, -25):
            rect = pygame.Rect(x - 12, i, 25, 25)
            if any(pared.rect.colliderect(rect) for pared in self.paredes):
                break
            self.screen.blit(self.explosion_image, rect)
            self.explosion_rects.append(rect)

        for i in range(y + 12, screen_height, 25):
            rect = pygame.Rect(x - 12, i, 25, 25)
            if any(pared.rect.colliderect(rect) for pared in self.paredes):
                break
            self.screen.blit(self.explosion_image, rect)
            self.explosion_rects.append(rect)

    def aplicar_dano(self, tanque, dano):
        current_time = pygame.time.get_ticks()
        if tanque not in self.last_damage_time:
            self.last_damage_time[tanque] = 0
        if current_time - self.last_damage_time[tanque] >= self.damage_cooldown:
            tanque.vida -= dano
            self.last_damage_time[tanque] = current_time
            sonido_quemarse = pygame.mixer.Sound("media/quemarse.mp3")
            sonido_quemarse.set_volume(1)
            sonido_quemarse.play()