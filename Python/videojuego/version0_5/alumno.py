import pygame

# Clase para manipular al alumno
class Alumno:
    # Constructor
    def __init__(self,screen,esc_alumnos_config):
        self.screen = screen
        self.esc_alumnos_config = esc_alumnos_config
        # Se cargan la imagen y obtiene el rect, para representar un rectangulo
        self.image = pygame.image.load("../media/pikachu.png")
        self.image_rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # Inicializar la posición
        self.image_rect.centerx = self.screen_rect.centerx
        self.image_rect.bottom = self.screen_rect.bottom

        #Centros del rectangulo, utilizando variables flotantes. Esto permite controlar la velocidad porque por defecto self.image_rect.center y self.image_rect.center alamacenan valores enteros.
        self.image_rect_centerx = float(self.image_rect.centerx)
        self.image_rect_centery = float(self.image_rect.centery)
        #Velocidad del alumno obtenida de las configuraciones
        self.alumno_speed = self.esc_alumnos_config.alumno_speed
        # Banderas de movimiento del alumno
        self.is_moving_right = False
        self.is_moving_left = False
        self.is_moving_up = False
        self.is_moving_down = False

    def update(self):
        if self.is_moving_right and self.image_rect.right < self.screen_rect.right:
            self.image_rect.centerx += self.alumno_speed
        if self.is_moving_left and self.image_rect.left > 0:
            self.image_rect.centerx -= self.alumno_speed
        if self.is_moving_up and self.image_rect.top > 0:
            self.image_rect.centery -= self.alumno_speed
        if self.is_moving_down and self.image_rect.bottom < self.screen_rect.bottom:
            self.image_rect.centery += self.alumno_speed

        self.image_rect.centerx = self.image_rect_centerx
        self.image_rect.centery = self.image_rect_centery

    # Métod0 que dibuja al alumno en su ubicación
    def blitme(self):
        self.screen.blit(self.image,self.image_rect)