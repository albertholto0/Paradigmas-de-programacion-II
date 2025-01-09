#import random

class Config:
    """Constructor"""
    def __init__(self):
        self.game_title = "Tank Battle"
        self.screen_width = 1080
        self.screen_height = 720
        self.background_image_path = "media/fondo.jpg"
        self.fps = 30

        self.tank_speed = 7

        self.bala_speed = 17
        #self.paredes = self.generar_paredes_aleatorias()

        """
        self.paredes = [
            [300, 100, 50, 200],  # Pared vertical izquierda
            [700, 100, 50, 200],  # Pared vertical derecha
            [300, 500, 50, 200],  # Pared vertical inferior izquierda
            [700, 500, 50, 200],  # Pared vertical inferior derecha
            [425, 300, 200, 50],  # Pared horizontal central
        ]
        """

        self.paredes = [
            [300, 100, 50, 200],  # Pared vertical izquierda
            [700, 100, 50, 200],  # Pared vertical derecha
            [300, 500, 50, 200],  # Pared vertical inferior izquierda
            [700, 500, 50, 200],  # Pared vertical inferior derecha
            [400, 300, 200, 50],  # Pared horizontal central
            [200, 250, 50, 150],  # Pared vertical izquierda pequeña
            [800, 250, 50, 150],  # Pared vertical derecha pequeña
            [500, 150, 50, 150],  # Pared vertical central
            [550, 450, 50, 150],  # Pared vertical inferior
            [500, 100, 200, 50],  # Pared horizontal superior
        ]

    """
    def generar_paredes_aleatorias(self):
        paredes = []
        num_paredes = random.randint(5, 10)  # Generamos entre 5 y 10 paredes

        for _ in range(num_paredes):
            # Determinamos si la pared será vertical u horizontal
            orientacion = random.choice(['vertical', 'horizontal'])

            if orientacion == 'vertical':
                x = random.randint(0, self.screen_width - 50)
                y = random.randint(0, self.screen_height - 200)
                width = 50
                height = random.randint(100, 200)
            else:
                x = random.randint(0, self.screen_width - 200)
                y = random.randint(0, self.screen_height - 50)
                width = random.randint(100, 200)
                height = 50

            paredes.append((x, y, width, height))

        return paredes
    """