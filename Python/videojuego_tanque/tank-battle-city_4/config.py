class Config:
    """Constructor"""
    def __init__(self):
        self.game_title = "Tank Battle"  # Título del juego.
        self.screen_width = 1080  # Largo de la pantalla.
        self.screen_height = 720  # Alto de la pantalla.
        self.background_image_path = "media/fondo.jpg"  # Ruta de la imagen de fondo.
        self.fps = 30

        self.tank_speed = 7

        self.bala_speed = 16