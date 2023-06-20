from configuraciones import reescalar_imagen 
from auxiliar import obtener_rectangulo
import pygame

class Player:
    def __init__(self, tamaño, animaciones, posicion_inicial, velocidad) -> None:
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
        self.velocidad = velocidad
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

    def mover(self, velocidad):
        for lado in self.lados:
            self.lados[lado].x += velocidad

    def update(self, pantalla):
        if self.back and self.que_hace == 'quieto':
            self.que_hace = 'quieto_atras'
        match self.que_hace:
            case 'caminar_derecha':
                self.animar(pantalla, 'caminar_derecha')
                self.mover(self.velocidad)
                self.back = False
            case 'caminar_izquierda':
                self.animar(pantalla, 'caminar_izquierda')
                self.mover(self.velocidad * -1)
                self.back = True
            case 'quieto':
                self.animar(pantalla, 'quieto')
            case 'quieto_atras':
                self.animar(pantalla, 'quieto_atras')