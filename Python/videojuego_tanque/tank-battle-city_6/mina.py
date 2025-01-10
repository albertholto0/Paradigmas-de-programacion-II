import pygame
from pygame.sprite import Sprite

class Mina(Sprite):
    def __init__(self, screen, x, y, tanque_propietario):
        super(Mina, self).__init__()
        self.screen = screen
        self.image = pygame.image.load("media/bomba.png")  # Imagen de la mina
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.explosion_time = pygame.time.get_ticks() + 3000  # Tiempo actual más 3 segundos
        self.exploded = False  # Bandera para verificar si ha explotado
        self.explosion_end_time = None  # Tiempo en que la explosión termina
        self.activo = True  # Bandera para verificar si la mina sigue activa
        self.explosion_image = pygame.image.load("media/fuego.png")  # Imagen de la explosión
        self.explosion_image = pygame.transform.scale(self.explosion_image, (25, 25))
        self.explosion_rects = []  # Rectángulos de colisión de la explosión
        self.tanque_propietario = tanque_propietario  # Tanque que dejó la mina
        self.damage_cooldown = 1500  # Tiempo mínimo entre aplicaciones de daño (ms)
        self.last_damage_time = {}  # Almacena el último daño aplicado a cada tanque

    def blitme(self):
        if not self.exploded:
            self.screen.blit(self.image, self.rect)
        elif self.exploded and pygame.time.get_ticks() < self.explosion_end_time:
            self.dibujar_explosion()

    def update(self):
        if pygame.time.get_ticks() >= self.explosion_time and not self.exploded:
            self.explotar()
            self.exploded = True
            self.explosion_end_time = pygame.time.get_ticks() + 3000
        elif self.exploded and pygame.time.get_ticks() >= self.explosion_end_time:
            self.activo = False

    def explotar(self):
        print(f"Explosión en forma de cruz iniciada en ({self.rect.centerx}, {self.rect.centery})")
        sonido_explosion_mina = pygame.mixer.Sound("media/explosion_mina.mp3")
        sonido_explosion_mina.set_volume(1)
        sonido_explosion_mina.play()
        self.dibujar_explosion()

    def dibujar_explosion(self):
        self.explosion_rects = []
        screen_width, screen_height = self.screen.get_size()
        x, y = self.rect.center

        # Dibujar la explosión en forma de cruz usando la imagen
        for i in range(0, screen_width, 25):
            self.screen.blit(self.explosion_image, (i, y - 12))
            self.explosion_rects.append(pygame.Rect(i, y - 12, 25, 25))
        for i in range(0, screen_height, 25):
            self.screen.blit(self.explosion_image, (x - 12, i))
            self.explosion_rects.append(pygame.Rect(x - 12, i, 25, 25))

    def aplicar_dano(self, tanque):
        current_time = pygame.time.get_ticks()
        if tanque not in self.last_damage_time:
            self.last_damage_time[tanque] = 0  # Inicializar si no existe
        if current_time - self.last_damage_time[tanque] >= self.damage_cooldown:
            tanque.vida -= 20
            self.last_damage_time[tanque] = current_time
