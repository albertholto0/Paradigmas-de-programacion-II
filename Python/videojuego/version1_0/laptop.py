import pygame
from pygame.sprite import Sprite

class Laptop (Sprite):
    # Se define el constructor de la laptop que hereda del constructor del Sprite
    def __init__(self,esc_alumnos_config,screen,alumno):
        # Se llama al constructor de la clase Sprite
        super(Laptop,self).__init__()
        # Se asignan los objetos de las configuraciones, la pantalla y del alumno
        self.esc_alumnos_config = esc_alumnos_config
        self.screen = screen
        self.alumno = alumno
        # Se carga la imagen y obtiene el Rect (Se usa para representar coordenadas rectangulares)
        self.image = pygame.image.load("../media/rayo.png")
        self.image_rect = self.image.get_rect()
        self.alumno_rect = self.alumno.image_rect
        # Posición inicial del arma, centrado con el alumno
        self.image_rect.centerx = self.alumno_rect.centerx
        self.image_rect.bottom = self.alumno_rect.top
        # Centros del rectangulo usando variables flotantes. Esto permite controlar la velocidad porque por defecto, self.laptop_rect almacenan valores enteros
        self.image_rect_centerx = float(self.image_rect.centerx)
        self.image_rect_centery = float(self.image_rect.centery)
        # Velocidad de la laptop obtenida de las configuraciones
        self.laptop_speed = self.esc_alumnos_config.laptop_speed

        # Al salir dispara la laptop, se debe actualizar unicamente la posicion del eje Y. Por lo tanto se debe restar un valor para que la direccipon sea hacia arriba

    def update_pos(self):
        self.image_rect.centery -= self.laptop_speed
    def blitme(self):
        self.screen.blit(self.image, self.image_rect)



