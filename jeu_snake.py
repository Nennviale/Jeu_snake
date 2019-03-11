import random
def print_state(matrice, x, y):
    print(f"La pomme se trouve en ({x}, {y})")
    i = 0
    for sousliste in matrice:
        j = 0
        for element in sousliste:
            if element == True:
                print('1', end='')
            elif x == i and y == j: 
                print ('P', end= '')
            else:
                print('-', end='')
            j = j+1
        i = i+1
        print ('')
    return 


def trouve_personnage(plateau):
    i = 0
    for ligne in plateau:
        j = 0
        for case in ligne:
            if case == True:
                print(f"({i}, {j})")
                return [i, j]
            else:
                j = j + 1
        i = i + 1
    
    return

def pomme_sur_personnage(plateau, x, y):
    i = 0
    for ligne in plateau:
        j = 0
        for case in ligne:
            if case == True and x==i and y ==j:    
                print (' La pomme est sur le personnage')

                return True
            else:
                j = j + 1
        i = i + 1
    
    return False

def move_personnage_droite(plateau):
    i, j = trouve_personnage(plateau)

    ligne = plateau[i]

    if j + 1 < len(ligne):
        ligne[j + 1] = True
    else:
        ligne[0] = True

    ligne[j] = False


    return plateau

def move_personnage_gauche(plateau):
    i, j = trouve_personnage(plateau)

    ligne = plateau[i]

    if j - 1 >= 0:
        ligne[j - 1] = True
    else:
        ligne[len(ligne) - 1] = True

    ligne[j] = False


    return plateau


def move_personnage_haut(plateau):
    i, j = trouve_personnage(plateau)

    if i - 1 >= 0:
        plateau[i - 1][j] = True
    else:
        plateau[len(plateau) - 1][j] = True

    plateau[i][j] = False



    return plateau

def move_personnage_bas(plateau):
    i, j = trouve_personnage(plateau)

    if i + 1 < len(plateau):
        plateau[i + 1][j] = True
    else:
        plateau[0][j] = True

    plateau[i][j] = False


    return plateau

state =[
    [False, False, False, False, False, False, False, False, ],
    [False, False, False, False, False, False, False, False, ],
    [False, False, False, False, False, False, False, False, ],
    [False, False, False, False, False, False, False, False, ],
    [False, False, False, False, False, False, False, False, ],
    [False, False, True, False, False, False, False, False, ],
    [False, False, False, False, False, False, False, False, ],
    [False, False, False, False, False, False, False, False, ],
    [False, False, False, False, False, False, False, False, ],
    [False, False, False, False, False, False, False, False, ],
]

from kbhit import KBHit
kb = KBHit()

print('Hit any key, or ESC to exit')
x = 0
y = 0

import time
 
# Wait for 5 seconds
time.sleep(5)

while True:


    if kb.kbhit():
        if pomme_sur_personnage(state, x, y): 
            x = random.randint(0, 9)
            y = random.randint(0, 7)
        # Affiche le plateau
        print_state(state,x ,y)   

        # Recupere la touche enfoncee
        c = kb.getch()
        c_ord = ord(c)
        print(c)
        print(c_ord)

        # Action suivant la touche enfoncee
        if c_ord == 27: # ESC
            break
        if c_ord == 97: # a
            print("gauche")
            move_personnage_gauche(state)
        if c_ord == 100: # d
            print("droite")
            move_personnage_droite(state)
        if c_ord == 119: # w
            print("haut")
            move_personnage_haut(state)
        if c_ord == 115: # s
            print("bas")
            move_personnage_bas(state)
        # Affiche le plateau
        print_state(state,x ,y) 
kb.set_normal_term()