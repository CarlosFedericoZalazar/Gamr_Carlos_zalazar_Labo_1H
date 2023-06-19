import pygame
from constantes import *

def reescalar_imagen(lista_imagenes, tamaño):
    for i in range(len(lista_imagenes)):
        lista_imagenes[i] = pygame.transform.scale(lista_imagenes[i], tamaño)


def girar_imagenes(lista_imagenes, flip_x, flip_y):
    lista_girada = []
    for imagen in lista_imagenes:
        lista_girada.append(pygame.transform.flip(imagen, flip_x, flip_y))
    return lista_girada


player_stay = [pygame.image.load(PATH_IMG + 'player\IDLE\_IDLE_000.png'),
                pygame.image.load(PATH_IMG + 'player\IDLE\_IDLE_001.png'),
                pygame.image.load(PATH_IMG + 'player\IDLE\_IDLE_002.png'),
                pygame.image.load(PATH_IMG + 'player\IDLE\_IDLE_003.png'),
                pygame.image.load(PATH_IMG + 'player\IDLE\_IDLE_004.png'),
                pygame.image.load(PATH_IMG + 'player\IDLE\_IDLE_005.png')]

player_walk_right = [pygame.image.load(PATH_IMG + 'player\WALK\_WALK_000.png'),
                pygame.image.load(PATH_IMG + 'player\WALK\_WALK_001.png'),
                pygame.image.load(PATH_IMG + 'player\WALK\_WALK_002.png'),
                pygame.image.load(PATH_IMG + 'player\WALK\_WALK_003.png'),
                pygame.image.load(PATH_IMG + 'player\WALK\_WALK_004.png'),
                pygame.image.load(PATH_IMG + 'player\WALK\_WALK_005.png')]

player_jump = [pygame.image.load(PATH_IMG + 'player\JUMP\_JUMP_000.png'),
                pygame.image.load(PATH_IMG + 'player\JUMP\_JUMP_001.png'),
                pygame.image.load(PATH_IMG + 'player\JUMP\_JUMP_002.png'),
                pygame.image.load(PATH_IMG + 'player\JUMP\_JUMP_003.png'),
                pygame.image.load(PATH_IMG + 'player\JUMP\_JUMP_004.png'),
                pygame.image.load(PATH_IMG + 'player\JUMP\_JUMP_005.png'),
                pygame.image.load(PATH_IMG + 'player\JUMP\_JUMP_006.png')]

player_attack = [pygame.image.load(PATH_IMG + 'player\ATTACK\_ATTACK_000.png'),
                    pygame.image.load(PATH_IMG + 'player\ATTACK\_ATTACK_001.png'),
                    pygame.image.load(PATH_IMG + 'player\ATTACK\_ATTACK_002.png'),
                    pygame.image.load(PATH_IMG + 'player\ATTACK\_ATTACK_003.png'),
                    pygame.image.load(PATH_IMG + 'player\ATTACK\_ATTACK_004.png'),
                    pygame.image.load(PATH_IMG + 'player\ATTACK\_ATTACK_005.png'),
                    pygame.image.load(PATH_IMG + 'player\ATTACK\_ATTACK_006.png')]

player_die = [pygame.image.load(PATH_IMG + 'player\HURT\_HURT_000.png'),
                pygame.image.load(PATH_IMG + 'player\HURT\_HURT_001.png'),
                pygame.image.load(PATH_IMG + 'player\HURT\_HURT_002.png'),
                pygame.image.load(PATH_IMG + 'player\HURT\_HURT_003.png'),
                pygame.image.load(PATH_IMG + 'player\HURT\_HURT_004.png'),
                pygame.image.load(PATH_IMG + 'player\HURT\_HURT_005.png'),
                pygame.image.load(PATH_IMG + 'player\HURT\_HURT_006.png')]

player_die = [pygame.image.load(PATH_IMG + 'player\DIE\_DIE_000.png'),
                pygame.image.load(PATH_IMG + 'player\DIE\_DIE_001.png'),
                pygame.image.load(PATH_IMG + 'player\DIE\_DIE_002.png'),
                pygame.image.load(PATH_IMG + 'player\DIE\_DIE_003.png'),
                pygame.image.load(PATH_IMG + 'player\DIE\_DIE_004.png'),
                pygame.image.load(PATH_IMG + 'player\DIE\_DIE_005.png'),
                pygame.image.load(PATH_IMG + 'player\DIE\_DIE_006.png')]

player_walk_left = girar_imagenes(player_walk_right, True, False)
player_jump_back = girar_imagenes(player_jump, True, False)
player_attack_back = girar_imagenes(player_attack, True, False)
player_stay_back = girar_imagenes(player_stay, True, False)