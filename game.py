import turtle

def init(n):
    config = list(range(1, n+1))
    config.reverse()
    plateau = [[],[],[]]
    plateau[0] = list(config)
    return plateau

#print(init(3))

def nombre_disques(plateau, numtour):
    return len(plateau[numtour])

print(nombre_disques(init(3),0))


def disque_superieur(plateau, numtour):
    if (len(plateau[numtour]) == 0):
        return -1
    return plateau[numtour][0]

print(disque_superieur(init(2),0))

def position_disque(plateau, numdisque):
    i, j = 0, 0
    while (i != 2):
        while (j != len(plateau)):
            if (plateau[i][j] == numdisque):
                return i, j
            j += 1
        i += 1
    return -1

print(position_disque(init(5),5))

def verifier_deplacement(plateau, nt1, nt2):
    if (len(plateau[nt1]) == 0):
        return False
    else:
        if (len(plateau[nt2]) == 0):
            return True
        elif (len(plateau[nt2] != 0)):
            if (disque_superieur(plateau,nt1) < disque_superieur(plateau,nt2)):
               return True
            else:
                return False

def verifier_victoire(plateau, n):
    i = 0
    while (i != n-1): 
        if (plateau[3][i] > plateau[3][i+1]):
            val = True
        else:
            val = False
        i += 1
    return val



    #################### PARTIE GRAPHIQUE ####################

def dessine_plateau(n):
    turtle.up()
    turtle.goto(-300,-200)
    turtle.down()

    i = 0
    if n == 1:
        longueur = 20
    else:
        longueur = (40 + 30*n)
    while (i != 2):
        turtle.forward(longueur*n + 20*n+1)
        turtle.right(90)
        turtle.forward(20)
        turtle.right(90)
        i += 1
    i = 0

    while (i != n):
        turtle.forward(20 + longueur/2 )
        turtle.left(90)
        turtle.forward(longueur/2)
        turtle.right(90)
        turtle.forward(6)
        turtle.right(90)
        turtle.forward(longueur/2)
        turtle.right(90)
        turtle.forward(6)
        turtle.right(180)
        turtle.forward(longueur/2)
    
        i += 1

#dessine_plateau(3)

def dessine_disque(nd, plateau, n):
    turtle.up()
    turtle.goto(-300,-200)
    turtle.forward(20 + 15*(n-nd))
    turtle.left(90)
    turtle.forward(20 + 20*(n-nd))
    turtle.right(90)

    turtle.down()

    turtle.forward(40 + 30*nd)
    turtle.right(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(40 + 30*nd)
    turtle.right(90)
    turtle.forward(20)
    turtle.right(90)

#dessine_disque(3,0,3)
#dessine_disque(2,0,3)
#dessine_disque(1,0,3)

def efface_disque(nd, plateau, n):
    turtle.color("White")
    turtle.up()
    turtle.goto(-300,-200)
    turtle.forward(20 + 15*(n-nd))
    turtle.left(90)
    turtle.forward(20 + 20*(n-nd))
    turtle.right(90)

    turtle.down()

    turtle.forward(40 + 30*nd)
    turtle.right(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(40 + 30*nd)
    turtle.right(90)
    turtle.forward(20)
    turtle.right(90)

#efface_disque(3,0,3)
#efface_disque(2,0,3)
#efface_disque(1,0,3)