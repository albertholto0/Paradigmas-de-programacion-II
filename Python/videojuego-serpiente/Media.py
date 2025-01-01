# Se importan las bibliotecas necesarias.
import pygame

"""Clase que tiene los efectos de sonido en el juego. """
class Media:
    def __init__(self, snake_game_configurations, screen):
        # Se crean los objetos de las configuraciones del juego y de la pantalla.
        self.snake_game_configurations = snake_game_configurations
        self.screen = screen

        ####################### MÚSICA Y SONIDOS #######################
        # Se carga la música de fondo del juego.
        pygame.mixer.music.load("../media/aula.unsij.edu.mx/moodle/draftfile.php/19888/user/draft/583940223/music.mp3")
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.65)

        # Se carga el sonido de inicio de la pantalla.
        self.start_sound = pygame.mixer.Sound("../media/aula.unsij.edu.mx/moodle/draftfile.php/19888/user/draft/583940223/start_sound.wav")

        # Se carga el sonido cuando la serpiente come.
        self.eaten_sound = pygame.mixer.Sound("../media/aula.unsij.edu.mx/moodle/draftfile.php/19888/user/draft/466922176/eaten_sound.wav")

        # Se carga el sonido de fin del juego.
        self.game_over_sound = pygame.mixer.Sound("../media/aula.unsij.edu.mx/moodle/draftfile.php/19888/user/draft/583940223/game_over_sound.wav")

        ####################### IMÁGENES #######################
        # Se obtienen valores de la pantalla y se obtiene su rect.
        self.screen_width = self.snake_game_configurations.screen_width
        self.screen_height = self.snake_game_configurations.screen_height
        self.screen_rect = self.screen.get_rect()

        # Se carga el fondo del videojuego, se reescala al tamaño de la pantalla y se obtiene su rect.
        self.background_image = pygame.image.load("../media/background.jpg")
        self.background_image = pygame.transform.scale(self.background_image, (self.screen_width, self.screen_height))
        self.background_rect = self.background_image.get_rect()

        # Se carga la imagen del fin del juego, se obtiene su rect y se ajusta la posición.
        self.game_over_image = pygame.image.load("../media/game_over_image.png")
        self.game_over_rect = self.game_over_image.get_rect()
        self.game_over_rect.centerx = self.screen_rect.centerx
        self.game_over_rect.top = self.screen_height // 12.5

        # Se carga la imagen de los créditos finales.
        self.credits_image = pygame.image.load("../media/credits.png")
        self.credits_rect = self.credits_image.get_rect()
        self.credits_rect.centerx = self.screen_rect.centerx
        self.credits_rect.bottom = self.screen_height // 12.5

        ####################### MARCADOR #######################
        # Se obtienen las configuraciones del marcador.
        self.scoreboard_text_color = self.snake_game_configurations.scoreboard_text_color
        self.scoreboard_font_type = self.snake_game_configurations.scoreboard_font_type
        self.scoreboard_font_size = self.snake_game_configurations.scoreboard_font_size

        # Se genera un marcador inicial de 0.
        # Se ajusta la fuente del juego, se convierte a una imagen con la función render y se obtiene el rect.
        self.font = pygame.font.SysFont(self.scoreboard_font_type, self.scoreboard_font_size)
        self.scoreboard_image = self.font.render("0", True, self.scoreboard_text_color)
        self.scoreboard_rect = self.scoreboard_image.get_rect()

        # Se ajusta la posición del texto.
        self.scoreboard_rect.x = self.screen_width * 0.05
        self.scoreboard_rect.y = self.screen_height * 0.05

    """ Método para reproducir el sonido de inicio de la pantalla. """
    def play_start_sound(self):
        self.start_sound.play()

    """ Método para reproducir el sonido cuando la serpiente come. """
    def play_eaten_sound(self):
        self.eaten_sound.play()

    """ Método para reproducir el sonido de fin del juego. """
    def play_game_over_sound(self):
        self.game_over_sound.play()

    """ Método que dibuja el fondo de pantalla."""
    def blit_background(self):
        self.screen.blit(self.background_image, self.background_rect)

    """ Método que dibuja el mensaje de fin del juego."""
    def blit_game_over(self):
        self.screen.blit(self.game_over_image, self.game_over_rect)

    """ Método que dibuja los créditos del juego."""
    def blit_credits(self):
        self.screen.blit(self.credits_image, self.credits_rect)

    """ Método que actualiza y dibuja el marcador."""
    def update_scoreboard(self, score):
        # Se convierte el score a texto.
        score_text = "Puntos: " + str(score)

        # Se convierte a una imagen con la función render y se obtiene el rect.
        self.font = pygame.font.SysFont(self.scoreboard_font_type, self.scoreboard_font_size)
        self.scoreboard_image = self.font.render(score_text, True, self.scoreboard_text_color)
        self.scoreboard_rect = self.scoreboard_image.get_rect()

        # Se ajusta la posición del texto, en este caso, se deja un espacio del tamaño de un bloque de la serpiente.
        self.scoreboard_rect.x = self.snake_game_configurations.snake_block_size
        self.scoreboard_rect.y = self.snake_game_configurations.snake_block_size

        # Se dibuja la pantalla.
        self.screen.blit(self.scoreboard_image, self.scoreboard_rect)
