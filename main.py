import pygame, sys, random
from constantes import *
from pygame.locals import *
from class_player import *
from class_enemy import *
from class_plataforma import *
from auxiliar import animaciones_player, animaciones_anemys
from modo import * # PARA VER LOS RECTANGULOS

#############################################################################

def actualizar_pantalla(pantalla, player: Player, fondo, delta_ms, list_plataforma):
    player.tiempo_trascurrido += delta_ms
    if player.tiempo_trascurrido >= 60:
        player.tiempo_trascurrido = 0
        PANTALLA.blit(fondo,(0,0))
        
        # for enemy in enemy_list:
        #     enemy.update(pantalla, delta_ms, list_plataforma)
        # plataformas
        for plataforma in list_plataforma:
            plataforma.update(pantalla)
           
        # jugador
        player.update(pantalla, delta_ms, list_plataforma)
#############################################################################

pygame.init()

# FONDO PRUEBA
fondo = pygame.image.load(PATH_FONDO + 'fondo_bosque.png')
fondo = pygame.transform.scale(fondo, SIZE_SCREEN)

# PLATAFORMA 
piso_surface = pygame.Surface((ANCHO_PANTALLA + 100,20))

lista_plataforma = []
plataforma_bosque = pygame.image.load(PATH_PLATAFORMAS + '\\bosque\\tile_montain.png')
plataforma_montain = Plataforma((100,200), plataforma_bosque, (1000,400),0,0, False)
lista_plataforma.append(plataforma_montain)
plataforma_bosque = pygame.image.load(PATH_PLATAFORMAS + '\\bosque\\tile_3.png')
plataforma_tile_3 = Plataforma((100,200), plataforma_bosque, (500,500),0,0, False)
lista_plataforma.append(plataforma_tile_3)
plataforma_bosque = pygame.image.load(PATH_PLATAFORMAS + '\\bosque\\tile_3.png')
plataforma_tile_4 = Plataforma((100,200), plataforma_bosque, (500,300),0,0, False)
lista_plataforma.append(plataforma_tile_4)
# plataforma_rect = pygame.Rect(plataforma_bosque.get_rect())
# plataforma_rect.x = 500
# plataforma_rect.y = 500
# plataforma_lados = obtener_rectangulo(plataforma_rect)




# ANIMACIONES
player_animaciones = animaciones_player()
enemys_animaciones = animaciones_anemys()
# PERSONAJE POSTA
posicion_inicial = (100,550)
player = Player(TAMAÑO_PERSONAJE,player_animaciones, posicion_inicial,VELOCIDAD_X,VELOCIDAD_Y)
plataforma_base = Plataforma((100,200), piso_surface, (0,player.lados['bottom'].top),0,0, True)
lista_plataforma.append(plataforma_base)
# ENEMIGO
# numero_aleatorio = random.randint(1, 5)
# y_random = random.randint(TOPE_Y[0], TOPE_Y[1])


# enemy_list = []

# for i in range(numero_aleatorio):
#     y_random = random.randint(TOPE_Y[0], TOPE_Y[1])
#     x_random = random.randint(100, 300)
#     enemy_list.append(Enemy(TAMAÑO_ENEMIGO,enemys_animaciones, (ANCHO_PANTALLA + x_random, y_random ),3,10))
    
while True:
    delta_ms = RELOJ.tick(FPS)    
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif evento.type == KEYDOWN:
            if evento.key == pygame.K_TAB:
                cambiar_modo()    

        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            player.que_hace = 'caminar_derecha'
        elif keys[pygame.K_LEFT]:
            player.que_hace = 'caminar_izquierda'
        elif keys[pygame.K_UP]:
            player.que_hace = 'saltar'         
        elif keys[pygame.K_SPACE]:
            player.que_hace = 'ataque'
        else:
            player.que_hace = 'quieto'
        # for enemigo in enemy_list:
        #     enemigo.que_hace = 'caminar_izquierda'
        

    actualizar_pantalla(PANTALLA, player, fondo, delta_ms,  lista_plataforma)
    #PANTALLA.blit(plataforma_bosque, lista_plataforma[0].lados['main'])
    
    # MOSTRAMOS LOS LADOS MODO PROGRAMADOR  
    if get_modo():
        #pygame.draw.rect(PANTALLA, 'Red', player.lados['bottom'], 3)
        
        for lado in player.lados:
            for plataforma in lista_plataforma:
                pygame.draw.rect(PANTALLA, 'Orange', plataforma.lados['top'], 3)
                pygame.draw.rect(PANTALLA, 'White', plataforma.lados['bottom'], 3)
                pygame.draw.rect(PANTALLA, 'Red', player.lados['bottom'], 3)
            if not lado == 'bottom':
                pygame.draw.rect(PANTALLA, 'Blue', player.lados[lado], 3)
                for plataforma in lista_plataforma:
                    pygame.draw.rect(PANTALLA, 'Yellow', plataforma.lados['main'], 3)
                # for enemy in enemy_list:
                #     pygame.draw.rect(PANTALLA, 'Pink', enemy.lados[lado], 3)
            pygame.draw.rect(PANTALLA, 'Red', player.lados['top'], 3)
    pygame.display.update()