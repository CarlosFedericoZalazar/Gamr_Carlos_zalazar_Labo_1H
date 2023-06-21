from configuraciones import *

def animaciones_player():
    diccionario_animaciones = {}
    
    diccionario_animaciones['quieto'] = player_stay
    diccionario_animaciones['quieto_atras'] = player_stay_back
    diccionario_animaciones['ataque'] = player_attack
    diccionario_animaciones['ataque_atras'] = player_attack_back
    diccionario_animaciones['caminar_derecha'] = player_walk_right
    diccionario_animaciones['caminar_izquierda'] = player_walk_left
    diccionario_animaciones['saltar'] = player_jump
    diccionario_animaciones['saltar_atras'] = player_jump_back
    return diccionario_animaciones

def animaciones_anemys():
    diccionario_animaciones = {}
    
    diccionario_animaciones['quieto'] = enemy_stay
    diccionario_animaciones['quieto_atras'] = enemy_stay_back
    diccionario_animaciones['ataque'] = enemy_attack
    diccionario_animaciones['ataque_atras'] = enemy_attack_back
    diccionario_animaciones['caminar_derecha'] = enemy_walk_right
    diccionario_animaciones['caminar_izquierda'] = enemy_walk_left
    diccionario_animaciones['saltar'] = enemy_jump
    diccionario_animaciones['saltar_atras'] = enemy_jump_back
    return diccionario_animaciones

def obtener_rectangulo(principal)->dict:
    diccionario = {}
    diccionario['main'] = principal
    diccionario['bottom'] = pygame.Rect(principal.left, principal.bottom -6, principal.width, 6)
    diccionario['right'] = pygame.Rect(principal.right -2, principal.top, 2, principal.height)
    diccionario['left'] = pygame.Rect(principal.left, principal.top, 2, principal.height)
    diccionario['top'] = pygame.Rect(principal.left, principal.top, principal.width, 6)
    return diccionario



    