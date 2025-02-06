import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
ANCHO = 800
ALTO = 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Pong")

# Colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)

# Configuración de las paletas y la pelota
PALETA_ANCHO = 10
PALETA_ALTO = 100
PELOTA_TAMANO = 20

# Velocidades
VELOCIDAD_PALETA = 5
VELOCIDAD_PELOTA_X = 4
VELOCIDAD_PELOTA_Y = 4

# Inicializar posiciones y velocidades
paleta1 = pygame.Rect(30, ALTO // 2 - PALETA_ALTO // 2, PALETA_ANCHO, PALETA_ALTO)
paleta2 = pygame.Rect(ANCHO - 30 - PALETA_ANCHO, ALTO // 2 - PALETA_ALTO // 2, PALETA_ANCHO, PALETA_ALTO)
pelota = pygame.Rect(ANCHO // 2 - PELOTA_TAMANO // 2, ALTO // 2 - PELOTA_TAMANO // 2, PELOTA_TAMANO, PELOTA_TAMANO)
velocidad_pelota_x = VELOCIDAD_PELOTA_X
velocidad_pelota_y = VELOCIDAD_PELOTA_Y

# Puntuación
puntuacion1 = 0
puntuacion2 = 0
fuente = pygame.font.Font(None, 74)

# Bucle principal del juego
reloj = pygame.time.Clock()
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Movimiento de las paletas
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_w] and paleta1.top > 0:
        paleta1.y -= VELOCIDAD_PALETA
    if teclas[pygame.K_s] and paleta1.bottom < ALTO:
        paleta1.y += VELOCIDAD_PALETA
    if teclas[pygame.K_UP] and paleta2.top > 0:
        paleta2.y -= VELOCIDAD_PALETA
    if teclas[pygame.K_DOWN] and paleta2.bottom < ALTO:
        paleta2.y += VELOCIDAD_PALETA

    # Movimiento de la pelota
    pelota.x += velocidad_pelota_x
    pelota.y += velocidad_pelota_y

    # Colisiones con las paredes superior e inferior
    if pelota.top <= 0 or pelota.bottom >= ALTO:
        velocidad_pelota_y *= -1

    # Colisiones con las paletas
    if pelota.colliderect(paleta1) or pelota.colliderect(paleta2):
        velocidad_pelota_x *= -1

    # Puntuación
    if pelota.left <= 0:
        puntuacion2 += 1
        pelota.x = ANCHO // 2 - PELOTA_TAMANO // 2
        pelota.y = ALTO // 2 - PELOTA_TAMANO // 2
        velocidad_pelota_x = VELOCIDAD_PELOTA_X
        velocidad_pelota_y = VELOCIDAD_PELOTA_Y
    if pelota.right >= ANCHO:
        puntuacion1 += 1
        pelota.x = ANCHO // 2 - PELOTA_TAMANO // 2
        pelota.y = ALTO // 2 - PELOTA_TAMANO // 2
        velocidad_pelota_x = -VELOCIDAD_PELOTA_X
        velocidad_pelota_y = VELOCIDAD_PELOTA_Y

    # Dibujar elementos en la pantalla
    pantalla.fill(NEGRO)
    pygame.draw.rect(pantalla, BLANCO, paleta1)
    pygame.draw.rect(pantalla, BLANCO, paleta2)
    pygame.draw.ellipse(pantalla, BLANCO, pelota)
    pygame.draw.aaline(pantalla, BLANCO, (ANCHO // 2, 0), (ANCHO // 2, ALTO))

    # Mostrar puntuación
    texto_puntuacion = fuente.render(f"{puntuacion1}  {puntuacion2}", True, BLANCO)
    pantalla.blit(texto_puntuacion, (ANCHO // 2 - 50, 10))

    # Actualizar pantalla
    pygame.display.flip()
    reloj.tick(60)