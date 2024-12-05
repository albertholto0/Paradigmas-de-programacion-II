# Se importan las bibliotecas requeridas.
import pygame

""" Clase para controlar al alumno."""
class Alumno:

    """ Constructor para inicializar al alumno y establecer su posición inicial en la pantalla ."""
    def __init__(self, screen, esc_alumnos_config):

        # Se crean los objetos de la pantalla y de las configuraciones del juego.
        self.screen = screen
        self.esc_alumnos_config = esc_alumnos_config

        # Se carga la imagen y obtiene el Rect (se utiliza para representar coordenadas rectangulares).
        self.image = pygame.image.load("../media/pikachu.png")
        self.image_rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Posición inicial del alumno (en el eje-x y en el eje-y).
        self.image_rect.centerx = self.screen_rect.centerx
        self.image_rect.bottom = self.screen_rect.bottom

        # Centros del rectángulo utilizando variables flotantes. Esto permite controlar la velocidad porque,
        # por defecto, self.image_rect.center y self.image_rect.center almacenan valores enteros.
        self.image_rect_centerx = float(self.image_rect.centerx)
        self.image_rect_centery = float(self.image_rect.centery)

        # Velocidad del alumno obtenida de las configuraciones.
        self.alumno_speed = self.esc_alumnos_config.tank_speed

        # Banderas de movimiento del alumno (derecha, izquierda, arriba y abajo).
        self.is_moving_right = False
        self.is_moving_left = False
        self.is_moving_up = False
        self.is_moving_down = False

    """ Método para actualizar la posición del alumno."""
    def update_pos(self):
        # Notar que no se utiliza if-elif para no tener prioridad en algún movimiento.
        # Parte superior izquierda: (x = 0 , y = 0)
        # Parte superior derecha: (x = 1080, y = 0)
        # Parte inferior izquierda: (x = 0 , y = 1080)
        # Parte inferior derecha: (x = 1080, y = 1080)

        # Si la bandera de movimiento a la derecha es verdadera y la parte derecha del Rect del alumno
        # es menor que la del Rect de la pantalla, entonces se suma un valor para este movimiento.
        if self.is_moving_right and (self.image_rect.right < self.screen_rect.right):
            self.image_rect_centerx += self.alumno_speed

        # Si la bandera de movimiento a la izquierda es verdadera y la parte izquierda del Rect del alumno
        # es mayor que la del Rect de la pantalla, entonces se suma un valor para este movimiento.
        if self.is_moving_left and (self.image_rect.left > self.screen_rect.left):
            self.image_rect_centerx -= self.alumno_speed

        # Si la bandera de movimiento hacia arriba es verdadera y la parte superior del Rect del alumno
        # es mayor que la del Rect de la pantalla, entonces se resta un valor para este movimiento.
        if self.is_moving_up and (self.image_rect.top > self.screen_rect.top):
            self.image_rect_centery -= self.alumno_speed

        # Si la bandera de movimiento hacia abajo es verdadera y la parte inferior del Rect del alumno
        # es menor que la del Rect de la pantalla, entonces se suma un valor para este movimiento.
        if self.is_moving_down and (self.image_rect.bottom < self.screen_rect.bottom):
            self.image_rect_centery += self.alumno_speed

        # Actualización de la posición del centro del rectángulo.
        self.image_rect.centerx = self.image_rect_centerx
        self.image_rect.centery = self.image_rect_centery

    """ Mét0do que dibuja el alumno en la pantalla en su ubicación actual."""
    def blitme(self):
        self.screen.blit(self.image, self.image_rect)