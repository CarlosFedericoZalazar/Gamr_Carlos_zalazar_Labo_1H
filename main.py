import pygame, sys
from constantes import *
from configuraciones import *
from pygame.locals import *
from class_player import *
from auxiliar import animaciones
from modo import * # PARA VER LOS RECTANGULOS

pygame.init()

# FONDO PRUEBA
fondo = pygame.image.load(PATH_FONDO + 'fondo.png')
fondo = pygame.transform.scale(fondo, SIZE_SCREEN)
# PERSONAJE PRUEBA
personaje = pygame.image.load(PATH_IMG + 'player\WALK\_WALK_000.png')
personaje = pygame.transform.scale(personaje, (150,150))
rect_personaje = personaje.get_rect
posicion_inicial = (100,ALTO_PANTALLA / 2)
# ANIMACIONES
player_animaciones = animaciones()


while True:
    RELOJ.tick(FPS)
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)    

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                print('izquierda')
            if evento.key == pygame.K_RIGHT:
                print('derecha')
            if evento.key == pygame.K_UP:
                print('arriba')
            if evento.key == pygame.K_DOWN:
                print('abajo')
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT:
                contador = 0
            if evento.key == pygame.K_RIGHT:
                print('derecha_up')
            if evento.key == pygame.K_UP:
                print('arriba_up')
            if evento.key == pygame.K_DOWN:
                print('abajo_up')

                
    PANTALLA.blit(fondo,(0,0))
    PANTALLA.blit(personaje, (150,200))
    pygame.display.flip()