from configuraciones import reescalar_imagen 
from auxiliar import obtener_rectangulo
import pygame

class Player:
    def __init__(self, tamaño, animaciones) -> None:
        # CONFECCION
        self.ancho = tamaño[0]
        self.alto = tamaño[1]
        # ANIMACIONES
        self.contador_pasos = 0
        self.que_hace = 'quieto'
        self.animaciones = animaciones
        self.reescalar_animaciones()

    def reescalar_animaciones(self):
        for clave in self.animaciones:
            reescalar_imagen(self.animaciones[clave], (self.ancho, self.alto))