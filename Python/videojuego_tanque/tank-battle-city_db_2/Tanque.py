import pygame
import time


class Tanque:
    def __init__(self, screen, tank_config, image_path="media/tanque_verde.png", position=None, nombre=""):
        self.screen = screen
        self.tank_config = tank_config
        self.nombre = nombre
        self.image = pygame.image.load(image_path)
        self.image_original = self.image
        self.image_rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.vida = 100
        self.max_balas = 15
        self.balas_disparadas = 0
        # Puntuacion
        self.puntuacion = 0
        # Minas
        self.minas_disponibles = 3
        self.max_minas = 3
        self.tiempo_ultima_mina = time.time()
        self.retraso_mina = 5

        if position:
            self.image_rect.centerx, self.image_rect.centery = position
        else:
            self.image_rect.centerx = self.screen_rect.centerx
            self.image_rect.bottom = self.screen_rect.bottom

        self.image_rect_centerx = float(self.image_rect.centerx)
        self.image_rect_centery = float(self.image_rect.centery)

        self.tank_speed = self.tank_config.tank_speed

        # Banderas de movimiento
        self.is_moving_right = False
        self.is_moving_left = False
        self.is_moving_up = False
        self.is_moving_down = False

        self.direction = 'down'

    def actualizar_minas(self):
        tiempo_actual = time.time()
        if tiempo_actual - self.tiempo_ultima_mina >= self.retraso_mina:
            if self.minas_disponibles < self.max_minas:
                self.minas_disponibles += 1
                self.tiempo_ultima_mina = tiempo_actual

    def update_pos(self, otro_tanque, paredes):
        if self.vida <= 0:
            return
        self.actualizar_minas()
        prev_rect = self.image_rect.copy()

        if self.is_moving_right and not self.collides_with_other_tank(otro_tanque, "right") and \
                not self.collides_with_walls(paredes, "right") and self.image_rect.right < self.screen_rect.right:
            self.image_rect_centerx += self.tank_speed
            self.direction = 'right'
        elif self.is_moving_left and not self.collides_with_other_tank(otro_tanque, "left") and \
                not self.collides_with_walls(paredes, "left") and self.image_rect.left > self.screen_rect.left:
            self.image_rect_centerx -= self.tank_speed
            self.direction = 'left'
        elif self.is_moving_up and not self.collides_with_other_tank(otro_tanque, "up") and \
                not self.collides_with_walls(paredes, "up") and self.image_rect.top > self.screen_rect.top:
            self.image_rect_centery -= self.tank_speed
            self.direction = 'up'
        elif self.is_moving_down and not self.collides_with_other_tank(otro_tanque, "down") and \
                not self.collides_with_walls(paredes, "down") and self.image_rect.bottom < self.screen_rect.bottom:
            self.image_rect_centery += self.tank_speed
            self.direction = 'down'

        self.image_rect.centerx = self.image_rect_centerx
        self.image_rect.centery = self.image_rect_centery

        self.rotate_image()

    def collides_with_walls(self, paredes, direction):
        temp_rect = self.image_rect.copy()
        if direction == "right":
            temp_rect.centerx += self.tank_speed
        elif direction == "left":
            temp_rect.centerx -= self.tank_speed
        elif direction == "up":
            temp_rect.centery -= self.tank_speed
        elif direction == "down":
            temp_rect.centery += self.tank_speed

        for pared in paredes:
            if temp_rect.colliderect(pared.rect):
                return True
        return False

    def collides_with_other_tank(self, otro_tanque, direction):
        temp_rect = self.image_rect.copy()

        if direction == "right":
            temp_rect.centerx += self.tank_speed
        elif direction == "left":
            temp_rect.centerx -= self.tank_speed
        elif direction == "up":
            temp_rect.centery -= self.tank_speed
        elif direction == "down":
            temp_rect.centery += self.tank_speed

        return temp_rect.colliderect(otro_tanque.image_rect)

    def rotate_image(self):
        if self.direction == 'right':
            self.image = pygame.transform.rotate(self.image_original, 270)
        elif self.direction == 'left':
            self.image = pygame.transform.rotate(self.image_original, 90)
        elif self.direction == 'up':
            self.image = self.image_original
        elif self.direction == 'down':
            self.image = pygame.transform.rotate(self.image_original, 180)

        self.image_rect = self.image.get_rect(center=self.image_rect.center)

    def blitme(self):
        self.screen.blit(self.image, self.image_rect)