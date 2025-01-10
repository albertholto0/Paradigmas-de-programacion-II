import pygame
from pygame.sprite import Sprite

class Mina(Sprite):
    def __init__(self, screen, x, y, tanque_propietario, paredes):
        super(Mina, self).__init__()
        self.screen = screen
        self.image = pygame.image.load("media/bomba.png")  # Imagen de la mina
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.explosion_time = pygame.time.get_ticks() + 2000  # Tiempo actual más 3 segundos
        self.exploded = False  # Bandera para verificar si ha explotado
        self.explosion_end_time = None  # Tiempo en que la explosión termina
        self.activo = True  # Bandera para verificar si la mina sigue activa
        self.explosion_image = pygame.image.load("media/fuego.png")  # Imagen de la explosión
        self.explosion_image = pygame.transform.scale(self.explosion_image, (25, 25))
        self.explosion_rects = []  # Rectángulos de colisión de la explosión
        self.tanque_propietario = tanque_propietario  # Tanque que dejó la mina
        self.paredes = paredes  # Lista de paredes en el juego
        self.damage_cooldown = 1000  # Tiempo mínimo entre aplicaciones de daño (ms)
        self.last_damage_time = {}  # Almacena el último daño aplicado a cada tanque

    def blitme(self):
        if not self.exploded:
            self.screen.blit(self.image, self.rect)
        elif self.exploded and pygame.time.get_ticks() < self.explosion_end_time:
            self.dibujar_explosion()

    def update(self):
        # Comprobar si han pasado 3 segundos desde la creación
        if pygame.time.get_ticks() >= self.explosion_time and not self.exploded:
            self.explotar()
            self.exploded = True
            self.explosion_end_time = pygame.time.get_ticks() + 2000  # Explosión dura 1 segundo
        elif self.exploded and pygame.time.get_ticks() >= self.explosion_end_time:
            self.activo = False  # Marcar la mina como inactiva después de que la explosión termine

    def explotar(self):
        print(f"Explosión en forma de cruz iniciada en ({self.rect.centerx}, {self.rect.centery})")
        self.dibujar_explosion()
        sonido_quemarse = pygame.mixer.Sound("media/explosion_mina.mp3")
        sonido_quemarse.set_volume(1)
        sonido_quemarse.play()

    def dibujar_explosion(self):
        self.explosion_rects = []  # Resetear rectángulos de colisión antes de crear nuevos
        screen_width, screen_height = self.screen.get_size()
        x, y = self.rect.center

        # Dibujar la explosión en forma de cruz usando la imagen
        # Hacia la izquierda
        for i in range(x - 12, -25, -25):
            rect = pygame.Rect(i, y - 12, 25, 25)
            if any(pared.rect.colliderect(rect) for pared in self.paredes):
                break
            self.screen.blit(self.explosion_image, rect)
            self.explosion_rects.append(rect)

        # Hacia la derecha
        for i in range(x + 12, screen_width, 25):
            rect = pygame.Rect(i, y - 12, 25, 25)
            if any(pared.rect.colliderect(rect) for pared in self.paredes):
                break
            self.screen.blit(self.explosion_image, rect)
            self.explosion_rects.append(rect)

        # Hacia arriba
        for i in range(y - 12, -25, -25):
            rect = pygame.Rect(x - 12, i, 25, 25)
            if any(pared.rect.colliderect(rect) for pared in self.paredes):
                break
            self.screen.blit(self.explosion_image, rect)
            self.explosion_rects.append(rect)

        # Hacia abajo
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