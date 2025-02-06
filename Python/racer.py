import pygame
import random

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
ANCHO = 800
ALTO = 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Rad Racer")

# Colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
VERDE = (0, 128, 0)
GRIS = (128, 128, 128)
ROJO = (255, 0, 0)

# Configuración del coche y obstáculos
COCHE_ANCHO = 50
COCHE_ALTO = 80
OBSTACULO_ANCHO = 50
OBSTACULO_ALTO = 50

# Velocidades
VELOCIDAD_COCHE = 5
VELOCIDAD_OBSTACULO = 5

# Inicializar posiciones
coche = pygame.Rect(ANCHO // 2 - COCHE_ANCHO // 2, ALTO - COCHE_ALTO - 20, COCHE_ANCHO, COCHE_ALTO)
obstaculos = []
tiempo_ultimo_obstaculo = pygame.time.get_ticks()

# Puntuación
puntuacion = 0
fuente = pygame.font.Font(None, 36)

# Bucle principal del juego
reloj = pygame.time.Clock()
ejecutando = True
while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    # Movimiento del coche
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT] and coche.left > 0:
        coche.x -= VELOCIDAD_COCHE
    if teclas[pygame.K_RIGHT] and coche.right < ANCHO:
        coche.x += VELOCIDAD_COCHE

    # Generar obstáculos
    tiempo_actual = pygame.time.get_ticks()
    if tiempo_actual - tiempo_ultimo_obstaculo > 2000:  # Cada 2 segundos
        x = random.randint(0, ANCHO - OBSTACULO_ANCHO)
        y = -OBSTACULO_ALTO
        obstaculos.append(pygame.Rect(x, y, OBSTACULO_ANCHO, OBSTACULO_ALTO))
        tiempo_ultimo_obstaculo = tiempo_actual

    # Mover obstáculos
    for obstaculo in obstaculos:
        obstaculo.y += VELOCIDAD_OBSTACULO
        if obstaculo.top > ALTO:
            obstaculos.remove(obstaculo)
            puntuacion += 1

    # Colisiones
    for obstaculo in obstaculos:
        if coche.colliderect(obstaculo):
            ejecutando = False

    # Dibujar elementos en la pantalla
    pantalla.fill(VERDE)  # Fondo verde (césped)
    pygame.draw.rect(pantalla, GRIS, (0, ALTO // 2, ANCHO, ALTO // 2))  # Carretera
    pygame.draw.rect(pantalla, BLANCO, coche)  # Coche
    for obstaculo in obstaculos:
        pygame.draw.rect(pantalla, ROJO, obstaculo)  # Obstáculos

    # Mostrar puntuación
    texto_puntuacion = fuente.render(f"Puntuación: {puntuacion}", True, BLANCO)
    pantalla.blit(texto_puntuacion, (10, 10))

    # Actualizar pantalla
    pygame.display.flip()
    reloj.tick(60)

# Fin del juego
pygame.quit()