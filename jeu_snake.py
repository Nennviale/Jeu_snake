def print_state(matrice):
    for sousliste in matrice:
        for element in sousliste:
            if element == True:
                print('1', end='')
            else:
                print('-', end='')
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

def move_personnage_droite(plateau):
    i, j = trouve_personnage(plateau)

    ligne = plateau[i]

    if j + 1 < len(ligne):
        ligne[j + 1] = True
    else:
        ligne[0] = True

    ligne[j] = False

    print_state(plateau)

    return plateau

def move_personnage_gauche(plateau):
    i, j = trouve_personnage(plateau)

    ligne = plateau[i]

    if j - 1 >= 0:
        ligne[j - 1] = True
    else:
        ligne[len(ligne) - 1] = True

    ligne[j] = False

    print_state(plateau)

    return plateau


def move_personnage_haut(plateau):
    i, j = trouve_personnage(plateau)

    if i - 1 >= 0:
        plateau[i - 1][j] = True
    else:
        plateau[len(plateau) - 1][j] = True

    plateau[i][j] = False

    print_state(plateau)

    return plateau

def move_personnage_bas(plateau):
    i, j = trouve_personnage(plateau)

    if i + 1 < len(plateau):
        plateau[i + 1][j] = True
    else:
        plateau[0][j] = True

    plateau[i][j] = False

    print_state(plateau)

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
print_state(state)

from kbhit import KBHit
kb = KBHit()

print('Hit any key, or ESC to exit')

while True:

    if kb.kbhit():
        # Affiche le plateau
        print_state(state)

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

kb.set_normal_term()