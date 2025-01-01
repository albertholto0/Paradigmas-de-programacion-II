"""
Clase para las configuraciones del juego.
"""

class Configurations:
    def __init__(self):
        # Configuraciones de la pantalla.
        self.game_title = "Juego de la serpiente"  # Título del juego.
        self.fps = 10  # FPS del juego.
        self.screen_width = 1080  # Ancho.
        self.screen_height = 720  # Alto.
        """NUEVO. Se eliminó el color de fondo de la pantalla y se agregaron las configuraciones del marcador."""
        self.scoreboard_text_color = (171, 250, 1)  # Color del texto del marcador.
        self.scoreboard_font_type = "Kimono"  # Tipo de fuente.
        self.scoreboard_font_size = 48  # Tamaño de la fuente.

        # Configuraciones de la serpiente.
        self.snake_block_size = 45  # Tamaño de cada bloque de la serpiente.
        self.snake_head_color = "black"  # Color de la cabeza de la serpiente.
        self.snake_body_color = "blue"  # Color del cuerpo de la serpiente.

        # Configuraciones de la comida.
        self.food_block_size = self.snake_block_size  # Tamaño del bloque de la comida, en este caso, igual al de la serpiente.
        self.food_color = "red"  # Color del bloque de la comida.