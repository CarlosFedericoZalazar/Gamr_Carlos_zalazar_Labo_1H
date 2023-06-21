import pygame, sys, random
from constantes import *
from pygame.locals import *
from class_player import *
from class_enemy import *
from auxiliar import animaciones_player, animaciones_anemys
from modo import * # PARA VER LOS RECTANGULOS

#############################################################################

def actualizar_pantalla(pantalla, player: Player, fondo, delta_ms, enemy_list, lados_piso):
    player.tiempo_trascurrido += delta_ms
    if player.tiempo_trascurrido >= 60:
        player.tiempo_trascurrido = 0
        PANTALLA.blit(fondo,(0,0))
        
        for enemy in enemy_list:
            enemy.update(pantalla, delta_ms, lados_piso)
        # plataformas
        player.update(pantalla, delta_ms, lados_piso)
#############################################################################

pygame.init()

# FONDO PRUEBA
fondo = pygame.image.load(PATH_FONDO + 'fondo.png')
fondo = pygame.transform.scale(fondo, SIZE_SCREEN)

# PLATAFORMA 
plataforma_bosque = pygame.image.load(PATH_PLATAFORMAS + '\\bosque\\tile_3.png')
plataforma_rect = pygame.Rect(plataforma_bosque.get_rect())
plataforma_rect.x = 500
plataforma_rect.y = 500
plataforma_lados = obtener_rectangulo(plataforma_rect)
posicion_inicial = (100,500)

# ANIMACIONES
player_animaciones = animaciones_player()
enemys_animaciones = animaciones_anemys()
# PERSONAJE POSTA
player = Player(TAMAÑO_PERSONAJE,player_animaciones, posicion_inicial,VELOCIDAD_X,VELOCIDAD_Y)

# ENEMIGO
numero_aleatorio = random.randint(1, 5)
y_random = random.randint(TOPE_Y[0], TOPE_Y[1])

# SUPERFICIE
piso = pygame.Rect(0,0,ANCHO_PANTALLA,20)
piso.top = player.lados['main'].bottom

lados_piso = obtener_rectangulo(piso)

enemy_list = []

for i in range(numero_aleatorio):
    y_random = random.randint(TOPE_Y[0], TOPE_Y[1])
    x_random = random.randint(100, 300)
    enemy_list.append(Enemy(TAMAÑO_ENEMIGO,enemys_animaciones, (ANCHO_PANTALLA + x_random, y_random ),3,10))
    
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
        for enemigo in enemy_list:
            enemigo.que_hace = 'caminar_izquierda'
        

    actualizar_pantalla(PANTALLA, player, fondo, delta_ms, enemy_list, lados_piso)
    PANTALLA.blit(plataforma_bosque, (500, 500))
    # MOSTRAMOS LOS LADOS MODO PROGRAMADOR  
    if get_modo():
        pygame.draw.rect(PANTALLA, 'Red', player.lados['bottom'], 3)
        
        for lado in player.lados:
            pygame.draw.rect(PANTALLA, 'Orange', plataforma_lados[lado], 3)
            if not lado == 'bottom':
                pygame.draw.rect(PANTALLA, 'Blue', player.lados[lado], 3)
                pygame.draw.rect(PANTALLA, 'Yellow', lados_piso['top'], 3)
                for enemy in enemy_list:
                    pygame.draw.rect(PANTALLA, 'Pink', enemy.lados[lado], 3)
    
    pygame.display.update()