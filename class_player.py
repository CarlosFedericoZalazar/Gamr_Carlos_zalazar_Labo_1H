from configuraciones import reescalar_imagen
from auxiliar import obtener_rectangulo
from constantes import *
import pygame

class Player:
    def __init__(self, tamaño, animaciones, posicion_inicial, velocidad_x, velocidad_y) -> None:
        # CONFECCION
        self.ancho = tamaño[0]
        self.alto = tamaño[1]
        # GRAVEDAD
        self.gravedad = 5
        self.potencia_salto = -40
        self.limite_velocidad_caida = 25
        self.esta_saltando = False
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
        self.tiempo_trascurrido = 0

    def reescalar_animaciones(self):
        for clave in self.animaciones:
            reescalar_imagen(self.animaciones[clave], (self.ancho, self.alto))

    def animar(self, pantalla, que_animacion: str):
        animacion = self.animaciones[que_animacion]
        largo = len(animacion)

        if self.contador_pasos >= largo:
            self.contador_pasos = 0
        
        pantalla.blit(animacion[self.contador_pasos], self.lados['main'])
        self.contador_pasos += 1

    def mover_x_y(self, velocidad, movimiento_x=True):
        for lado in self.lados:
            if movimiento_x:
                self.lados[lado].x += velocidad

    def update(self, pantalla, delta_ms, piso):

        if self.back and self.que_hace == 'quieto':
            self.que_hace = 'quieto_atras'
        if self.back and self.que_hace == 'ataque':
            self.que_hace = 'ataque_atras'
        # BUSCARLE LA VUELTA PARA METER LAS ANIMACIONES EN UNA FUNCION
        match self.que_hace:
            case 'caminar_derecha':
                if not self.esta_saltando:
                    self.animar(pantalla, 'caminar_derecha')
                self.mover_x_y(self.velocidad_x)
                self.back = False
            case 'caminar_izquierda':
                if not self.esta_saltando:
                    self.animar(pantalla, 'caminar_izquierda')
                self.mover_x_y(self.velocidad_x * -1)
                self.back = True
            case 'quieto':
                if not self.esta_saltando:
                    self.animar(pantalla, 'quieto')
            case 'quieto_atras':
                if not self.esta_saltando:
                    self.animar(pantalla, 'quieto_atras')
            case 'saltar':
                if not self.esta_saltando:
                    self.esta_saltando = True
                    self.desplazamiento_y = self.potencia_salto
                    
            case 'ataque':
                self.animar(pantalla, 'ataque')
            case 'ataque_atras':
                self.animar(pantalla, 'ataque_atras')
        
        self.aplicar_gravedad(pantalla, piso)

    # GRAVEDAD DEL PERSONAJE
    def aplicar_gravedad(self, pantalla, piso):
        if self.esta_saltando:
            if not self.back:
                self.animar(pantalla, 'saltar')
            else:
                self.animar(pantalla, 'saltar_atras')

            for lado in self.lados:
                self.lados[lado].y += self.desplazamiento_y

            if self.desplazamiento_y < self.limite_velocidad_caida:
                self.desplazamiento_y += self.gravedad

        if self.lados['bottom'].colliderect(piso['main']):
            print('hola mundo')
            self.esta_saltando = False
            self.desplazamiento_y = 0
            self.lados['main'].bottom = piso['main'].top + 5
            
