import pygame

class Tanque:
    """ Constructor para inicializar al tanque y establecer su posición inicial en la pantalla. """
    def __init__(self, screen, tank_config, image_path="media/tanque_verde.png", position=None):
        self.screen = screen
        self.tank_config = tank_config
        self.image = pygame.image.load(image_path)
        self.image_original = self.image
        self.image_rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.vida = 100

        if position:
            self.image_rect.centerx, self.image_rect.centery = position
        else:
            self.image_rect.centerx = self.screen_rect.centerx
            self.image_rect.bottom = self.screen_rect.bottom

        self.image_rect_centerx = float(self.image_rect.centerx)
        self.image_rect_centery = float(self.image_rect.centery)

        self.tank_speed = self.tank_config.tank_speed

        # Flags de movimiento
        self.is_moving_right = False
        self.is_moving_left = False
        self.is_moving_up = False
        self.is_moving_down = False

        self.direction = 'down'

    def update_pos(self, otro_tanque):
        """ Actualiza la posición del tanque y verifica colisiones con otro tanque y los bordes de la pantalla. """
        if self.vida <= 0:
            return  # Si la vida es 0, no se mueve el tanque

        prev_rect = self.image_rect.copy()  # Guardamos la posición previa del tanque

        # Verificamos la posible colisión antes de mover al tanque
        if self.is_moving_right and not self.collides_with_other_tank(otro_tanque, "right") and self.image_rect.right < self.screen_rect.right:
            self.image_rect_centerx += self.tank_speed
            self.direction = 'right'
        elif self.is_moving_left and not self.collides_with_other_tank(otro_tanque, "left") and self.image_rect.left > self.screen_rect.left:
            self.image_rect_centerx -= self.tank_speed
            self.direction = 'left'
        elif self.is_moving_up and not self.collides_with_other_tank(otro_tanque, "up") and self.image_rect.top > self.screen_rect.top:
            self.image_rect_centery -= self.tank_speed
            self.direction = 'up'
        elif self.is_moving_down and not self.collides_with_other_tank(otro_tanque, "down") and self.image_rect.bottom < self.screen_rect.bottom:
            self.image_rect_centery += self.tank_speed
            self.direction = 'down'

        # Actualizamos el rectángulo con la nueva posición
        self.image_rect.centerx = self.image_rect_centerx
        self.image_rect.centery = self.image_rect_centery

        # Aseguramos que la imagen del tanque se rote correctamente según la dirección
        self.rotate_image()

    def collides_with_other_tank(self, otro_tanque, direction):
        """ Verifica si el tanque se movería hacia otro tanque. """
        temp_rect = self.image_rect.copy()

        # Dependiendo de la dirección, movemos temporalmente el rectángulo y verificamos la colisión
        if direction == "right":
            temp_rect.centerx += self.tank_speed
        elif direction == "left":
            temp_rect.centerx -= self.tank_speed
        elif direction == "up":
            temp_rect.centery -= self.tank_speed
        elif direction == "down":
            temp_rect.centery += self.tank_speed

        # Usamos el rectángulo de la imagen para la colisión
        return temp_rect.colliderect(otro_tanque.image_rect)

    def rotate_image(self):
        """ Rota la imagen del tanque según la dirección del movimiento """
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
        """ Dibuja el tanque en la pantalla. """
        self.screen.blit(self.image, self.image_rect)