import pygame, sys
from constantes import *
from configuraciones import *
from pygame.locals import *
from class_player import *
from auxiliar import animaciones
from modo import * # PARA VER LOS RECTANGULOS

#############################################################################

def actualizar_pantalla(pantalla, un_personaje: Player, fondo):
    PANTALLA.blit(fondo,(0,0))
    # plataformas
    player.update(pantalla)
#############################################################################

pygame.init()

# FONDO PRUEBA
fondo = pygame.image.load(PATH_FONDO + 'fondo.png')
fondo = pygame.transform.scale(fondo, SIZE_SCREEN)

# PERSONAJE PRUEBA
# personaje = pygame.image.load(PATH_IMG + 'player\WALK\_WALK_000.png')
# personaje = pygame.transform.scale(personaje, (150,150))
# rect_personaje = personaje.get_rect
posicion_inicial = (100,ALTO_PANTALLA / 2)

# ANIMACIONES
player_animaciones = animaciones()

# PERSONAJE POSTA
player = Player(TAMAÑO_PERSONAJE,player_animaciones, posicion_inicial,15)


while True:
    RELOJ.tick(FPS)
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif evento.type == KEYDOWN:
            if evento.key == pygame.K_TAB:
                cambiar_modo()    

        # if evento.type == pygame.KEYDOWN:
        #     if evento.key == pygame.K_LEFT:
        #         player.que_hace = 'caminar_izquierda'
        #     elif evento.key == pygame.K_RIGHT:
        #         player.que_hace = 'caminar_derecha'

        # if evento.type == pygame.KEYUP:
        #     if evento.key == pygame.K_LEFT:
        #         contador = 0
        #     if evento.key == pygame.K_RIGHT:
        #         print('derecha_up')
        #     if evento.key == pygame.K_UP:
        #         print('arriba_up')
        #     if evento.key == pygame.K_DOWN:
        #         print('abajo_up')

        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            player.que_hace = 'caminar_derecha'
        elif keys[pygame.K_LEFT]:
            player.que_hace = 'caminar_izquierda'
        elif keys[pygame.K_UP]:
            player.que_hace = 'salta'
        else:
            player.que_hace = 'quieto'

    actualizar_pantalla(PANTALLA, player, fondo)
    # MOSTRAMOS LOS LADOS MODO PROGRAMADOR
    if get_modo():
        for lado in player.lados:
            pygame.draw.rect(PANTALLA, 'Blue', player.lados[lado], 3)

    pygame.display.update()