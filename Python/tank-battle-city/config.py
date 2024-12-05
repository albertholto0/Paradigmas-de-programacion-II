"""
Clase para las configuraciones del juego.
"""
class Config:

    """Constructor"""
    def __init__(self):
        self.game_title = "Tank Battle"  # Título del juego.
        self.screen_width = 1080  # Largo de la pantalla.
        self.screen_height = 720  # Alto de la pantalla.
        self.background_color = (0,0,0)  # Color de fondo.

        # Configuraciones del alumno
        self.tank_speed = 0.5  # Velocidad del movimiento del alumno. Colocar float.

        # Configuraciones de la laptop (arma)
        self.bala_speed = 0.45