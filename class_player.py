from configuraciones import reescalar_imagen 
from auxiliar import obtener_rectangulo
from constantes import *
import pygame

class Player:
    def __init__(self, tamaño, animaciones, posicion_inicial, velocidad_x, velocidad_y) -> None:
        # CONFECCION
        self.ancho = tamaño[0]
        self.alto = tamaño[1]
        # ANIMACIONES
        self.contador_pasos = 0
        self.que_hace = 'quieto'
        self.back = False
        self.animaciones = animaciones
        self.reescalar_animaciones()
        # RECTANGULOS
        rectangulo = pygame.Rect(self.animaciones['caminar_derecha'][0].get_rect())
        rectangulo.x = posicion_inicial[0]
        rectangulo.y = posicion_inicial[1]
        self.lados = obtener_rectangulo(rectangulo)
        # MOVIMIENTO 
        self.velocidad_x = velocidad_x
        self.velocidad_y = velocidad_y
        self.desplazamiento_y = 0

    def reescalar_animaciones(self):
        for clave in self.animaciones:
            reescalar_imagen(self.animaciones[clave], (self.ancho, self.alto))

    def animar(self, pantalla, que_animacion:str):
        animacion = self.animaciones[que_animacion]
        largo = len(animacion)

        if self.contador_pasos >= largo:
            self.contador_pasos = 0
        
        pantalla.blit(animacion[self.contador_pasos], self.lados['main'])
        self.contador_pasos += 1

    def mover_x_y(self, velocidad, movimiento_x = True):
        for lado in self.lados:
            if movimiento_x:
                self.lados[lado].x += velocidad
            else:
                if self.lados[lado].y < TOPE_Y[0]:
                    self.lados[lado].y = self.lados[lado].y + 10
                elif self.lados[lado].y > TOPE_Y[1]:
                    self.lados[lado].y = self.lados[lado].y - 10
                else:
                    self.lados[lado].y += velocidad

    def update(self, pantalla):
        if self.back and self.que_hace == 'quieto':
            self.que_hace = 'quieto_atras'
        


        match self.que_hace:
            case 'caminar_derecha':
                self.animar(pantalla, 'caminar_derecha')
                self.mover_x_y(self.velocidad_x)
                self.back = False
            case 'caminar_izquierda':
                self.animar(pantalla, 'caminar_izquierda')
                self.mover_x_y(self.velocidad_x * -1)
                self.back = True
            case 'quieto':
                self.animar(pantalla, 'quieto')
            case 'quieto_atras':
                self.animar(pantalla, 'quieto_atras')
            case 'caminar_arriba':
                if self.back and self.que_hace == 'caminar_arriba':
                    self.animar(pantalla, 'caminar_izquierda')
                else:
                    self.animar(pantalla, 'caminar_derecha')
                self.mover_x_y(self.velocidad_y * -1, False)
            case 'caminar_abajo':
                if self.back and self.que_hace == 'caminar_abajo':
                    self.animar(pantalla, 'caminar_izquierda')
                else:
                    self.animar(pantalla, 'caminar_derecha')
                self.mover_x_y(self.velocidad_y, False)