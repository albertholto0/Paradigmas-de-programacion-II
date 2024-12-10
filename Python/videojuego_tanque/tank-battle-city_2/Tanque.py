import pygame

class Tanque:
    """ Constructor para inicializar al tanque y establecer su posición inicial en la pantalla. """
    def __init__(self, screen, tank_config, image_path="media/tanque_verde.png"):
        # Se crean los objetos de la pantalla y de las configuraciones del juego.
        self.screen = screen
        self.tank_config = tank_config

        # Se carga la imagen y obtiene el Rect (se utiliza para representar coordenadas rectangulares).
        self.image = pygame.image.load(image_path)  # Cargar la imagen una vez
        self.image_original = self.image  # Guardar una referencia a la imagen original
        self.image_rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

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

        # Dirección inicial del tanque
        self.direction = 'up'  # Agregar 'direction' aquí para evitar el error

    """ Método para actualizar la posición del tanque. """
    def update_pos(self):
        # Se actualiza la posición del tanque según las teclas presionadas.
        if self.is_moving_right and (self.image_rect.right < self.screen_rect.right):
            self.image_rect_centerx += self.tank_speed
            self.direction = 'right'  # Actualiza la dirección cuando se mueve a la derecha

        if self.is_moving_left and (self.image_rect.left > self.screen_rect.left):
            self.image_rect_centerx -= self.tank_speed
            self.direction = 'left'  # Actualiza la dirección cuando se mueve a la izquierda

        if self.is_moving_up and (self.image_rect.top > self.screen_rect.top):
            self.image_rect_centery -= self.tank_speed
            self.direction = 'up'  # Actualiza la dirección cuando se mueve hacia arriba

        if self.is_moving_down and (self.image_rect.bottom < self.screen_rect.bottom):
            self.image_rect_centery += self.tank_speed
            self.direction = 'down'  # Actualiza la dirección cuando se mueve hacia abajo

        self.image_rect.centerx = self.image_rect_centerx
        self.image_rect.centery = self.image_rect_centery

        # Cambiar la rotación del tanque en función de la dirección
        self.rotate_image()

    def rotate_image(self):
        """Metodo para rotar la imagen del tanque según la dirección de movimiento."""
        if self.direction == 'right':
            self.image = pygame.transform.rotate(self.image_original, 270)  # Rotar 270° hacia la derecha
        elif self.direction == 'left':
            self.image = pygame.transform.rotate(self.image_original, 90)  # Rotar 90° hacia la izquierda
        elif self.direction == 'up':
            self.image = self.image_original  # Mantener la imagen en su posición original
        elif self.direction == 'down':
            self.image = pygame.transform.rotate(self.image_original, 180)  # Rotar 180° hacia abajo

        self.image_rect = self.image.get_rect(center=self.image_rect.center)

    """ Mét0d0 que dibuja el tanque en la pantalla en su ubicación actual. """
    def blitme(self):
        self.screen.blit(self.image, self.image_rect)
