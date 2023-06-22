import pygame
from auxiliar import obtener_rectangulo

class Plataforma():
    def __init__(self, tamaño, tile, posicion_inicial, velocidad_x, velocidad_y) -> None:
        # TAMAÑO
        self.ancho = tamaño[0]
        self.alto = tamaño[1]
        #self.plataforma = reescalar_imagen(tile)
        # RECTANGULOS
        rectangulo = pygame.Rect(tile.get_rect())
        rectangulo.x = posicion_inicial[0]
        rectangulo.y = posicion_inicial[1]
        self.lados = obtener_rectangulo(rectangulo)
        # MOVIMIENTO
        self.velocidad_x = velocidad_x
        self.velocidad_y = velocidad_y


        def reescalar_imagen(self, tile):
            imagen = pygame.transform.scale(tile, (tamaño))
