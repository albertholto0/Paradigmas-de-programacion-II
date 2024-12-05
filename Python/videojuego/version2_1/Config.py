"""
Clase para las configuraciones del juego.
"""
class Config:

    ''' Constructor. '''
    def __init__(self):
        # Configuraciones de la pantalla.
        self.game_title = "Escape de los alumnos"  # Título del juego.
        self.screen_width = 1080  # Largo de la pantalla.
        self.screen_height = 720  # Alto de la pantalla.
        self.background_color = (20, 200, 200)  # Color de fondo.

        # Configuraciones del alumno.
        self.alumno_speed = 0.5  # Velocidad del movimiento del alumno. Colocar float.

        # Configuraciones de la laptop (arma).
        self.laptop_speed = 0.45  # Velocidad del movimiento de la laptop.
        self.max_laptops = 5  # Número máximo de laptops que puede arrojar el alumno.

        # Configuraciones del hacker (enemigo).
        self.hacker_speed = 0.2  # Velocidad del movimiento del hacker.
