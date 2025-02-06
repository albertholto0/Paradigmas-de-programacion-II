import pygame
from pygame.sprite import Sprite

class Bala(Sprite):
    def __init__(self, tank_config, screen, tanque):
        super(Bala, self).__init__()

        self.tank_config = tank_config
        self.screen = screen
        self.tanque = tanque

        self.bala_image = pygame.image.load("media/bala.png")
        self.bala_rect = self.bala_image.get_rect()
        self.screen_rect = screen.get_rect()

        self.origen = tanque

        if self.tanque.direction == 'right':
            self.bala_rect.centerx = self.tanque.image_rect.right
            self.bala_rect.centery = self.tanque.image_rect.centery
        elif self.tanque.direction == 'left':
            self.bala_rect.centerx = self.tanque.image_rect.left
            self.bala_rect.centery = self.tanque.image_rect.centery
        elif self.tanque.direction == 'up':
            self.bala_rect.centerx = self.tanque.image_rect.centerx
            self.bala_rect.bottom = self.tanque.image_rect.top
        elif self.tanque.direction == 'down':
            self.bala_rect.centerx = self.tanque.image_rect.centerx
            self.bala_rect.top = self.tanque.image_rect.bottom

        self.bala_rect_centerx = float(self.bala_rect.centerx)
        self.bala_rect_centery = float(self.bala_rect.centery)
        self.bala_speed = self.tank_config.bala_speed
        self.direction = self.tanque.direction

        self.rotate_bala_image()

    def update_pos(self):
        if self.direction == 'up':
            self.bala_rect_centery -= self.bala_speed
        elif self.direction == 'down':
            self.bala_rect_centery += self.bala_speed
        elif self.direction == 'left':
            self.bala_rect_centerx -= self.bala_speed
        elif self.direction == 'right':
            self.bala_rect_centerx += self.bala_speed

        self.bala_rect.centerx = self.bala_rect_centerx
        self.bala_rect.centery = self.bala_rect_centery

    def blitme(self):
        self.screen.blit(self.bala_image, self.bala_rect)

    def rotate_bala_image(self):
        if self.direction == 'right':
            self.bala_image = pygame.transform.rotate(pygame.image.load("media/bala.png"), 270)
        elif self.direction == 'left':
            self.bala_image = pygame.transform.rotate(pygame.image.load("media/bala.png"), 90)
        elif self.direction == 'up':
            self.bala_image = pygame.image.load("media/bala.png")
        elif self.direction == 'down':
            self.bala_image = pygame.transform.rotate(pygame.image.load("media/bala.png"), 180)

        self.bala_rect = self.bala_image.get_rect(center=self.bala_rect.center)

    def eliminar_bala(self):
        self.kill()