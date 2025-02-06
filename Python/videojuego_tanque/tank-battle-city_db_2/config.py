import random

class Config:
    def __init__(self):
        self.game_title = "Tank Battle"
        self.screen_width = 1080
        self.screen_height = 720
        self.background_image_path = "media/fondo.jpg"
        self.fps = 30
        self.tank_speed = 9
        self.bala_speed = 20
        self.paredes = self.seleccionar_paredes_aleatorias()

    def seleccionar_paredes_aleatorias(self):
        patrones = [
            [
                [300, 100, 50, 200],  # Pared vertical izquierda superior
                [700, 100, 50, 200],  # Pared vertical derecha superior
                [300, 500, 50, 200],  # Pared vertical inferior izquierda
                [700, 500, 50, 200],  # Pared vertical inferior derecha
                [425, 300, 200, 50]  # Pared horizontal central
            ],
            [
                [280, 100, 50, 200],  # Pared vertical izquierda superior
                [700, 100, 50, 200],  # Pared vertical derecha superior
                [300, 500, 50, 200],  # Pared vertical inferior izquierda
                [700, 500, 50, 200],  # Pared vertical inferior derecha
                [400, 300, 200, 50],  # Pared horizontal central
                [170, 250, 50, 150],  # Pared vertical izquierda pequeña
                [810, 250, 50, 150],  # Pared vertical derecha pequeña
                [500, 150, 50, 150],  # Pared vertical central superior
                [550, 450, 50, 150],  # Pared vertical central inferior
                [500, 100, 200, 50]  # Pared horizontal superior
            ],
            [
                [150, 100, 50, 200],  # Pared vertical izquierda superior
                [900, 100, 50, 200],  # Pared vertical derecha superior
                [150, 460, 50, 200],  # Pared vertical izquierda inferior
                [900, 460, 50, 200],  # Pared vertical derecha inferior
                [470, 350, 200, 50],  # Pared horizontal central
                [360, 200, 50, 150],  # Pared vertical izquierda central
                [730, 200, 50, 150],  # Pared vertical derecha central
                [470, 550, 200, 50],  # Pared horizontal inferior
            ],
            [
                [330, 150, 50, 150],  # Pared vertical izquierda
                [700, 150, 50, 150],  # Pared vertical derecha
                [330, 450, 50, 150],  # Pared vertical inferior izquierda
                [700, 450, 50, 150],  # Pared vertical inferior derecha
                [440, 320, 200, 50],  # Pared horizontal central
                [440, 100, 200, 50],  # Pared horizontal superior
                [440, 600, 200, 50],  # Pared horizontal inferior

            ],
        ]

        indice_patron = random.randint(0, len(patrones) - 1)
        patron_seleccionado = patrones[indice_patron]
        print(f"Patrón seleccionado: {indice_patron + 1}")

        return patron_seleccionado