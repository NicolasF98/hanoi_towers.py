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

#print(nombre_disques(init(3),0))


def disque_superieur(plateau, numtour):
    if (len(plateau[numtour]) == 0):
        return -1
    return plateau[numtour][0]

#print(disque_superieur(init(2),0))

def position_disque(plateau, numdisque):
    i, j = 0, 0
    while (i != 2):
        while (j != len(plateau)):
            if (plateau[i][j] == numdisque):
                return i, j
            j += 1
        i += 1
    return -1

#print(position_disque(init(5),5))

def verifier_deplacement(plateau, nt1, nt2):
    if (len(plateau[nt1]) == 0):
        return False
    else:
        if (len(plateau[nt2]) == 0):
            return True
        elif (len(plateau[nt2]) != 0):
            if (disque_superieur(plateau,nt1) < disque_superieur(plateau,nt2)):
               return True
            else:
                return False
p = [[2],[3],[1]]
#print(verifier_deplacement(p,0,2))


def verifier_victoire(plateau, n):
    p = [[], [], [1,2,3]]
    p1 = [[], [], [3,2,1]]
    i = 1
    while (i <= n):
        p[2].append(i)
        i += 1
    if (p == plateau or p1 == plateau):
        return True
    return False

    #################### PARTIE GRAPHIQUE ####################
    # reste à ajouter des couleurs, ainsi qu'une image de fond

def dessine_plateau(n):
    turtle.speed('fastest')
    #position initial
    turtle.up()
    turtle.goto(-300,-200)
    turtle.down()

    #plateau
    turtle.forward( (20*4) + ((40 + (30*(n-1)))*3) + (6*3))
    turtle.right(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward( (20*4) + ((40 + (30*(n-1)))*3) + (6*3))
    turtle.right(90)
    turtle.forward(20)
    turtle.right(90)

    #tours
    i = 0
    while(i != 3):
        turtle.forward(20 + ((40 + (30*(n-1)))/2))
        turtle.left(90)
        turtle.forward(20 + (40 + (30*(n-1)))/2)
        turtle.right(90)
        turtle.forward(6)
        turtle.right(90)
        turtle.forward( 20 + (40 + (30*(n-1)))/2 )
        turtle.left(90)
        turtle.forward((40 + (30*(n-1)))/2 )
        i += 1

#print(dessine_plateau(3))

def dessine_disque(nd, plateau, n):
    turtle.color('black')
    #turtle.speed('fastest')
    i, j, sortie = 0, 0, 0
    while (i < 3 and sortie == 0):
        while (j < len(plateau[i]) and sortie == 0):
            if (nd == plateau[i][j]):
                coord_x = (20 + 15*(n-nd)) + (40 + (30*n))*i
                if (len(plateau[i]) == 1):
                    coord_y = 0
                elif (len(plateau[i]) == 2):
                    coord_y = 20*(n-nd)
                else:
                    coord_y = (20 * (n-nd))
                sortie = 1
            j += 1
        j = 0
        i += 1

    turtle.up()
    turtle.goto((-300) + coord_x, (-200) + coord_y)
    turtle.down()
    
    turtle.left(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward((40 + (30*(nd-1))))
    turtle.right(90)
    turtle.forward(20)
    turtle.left(90)

#p = [[],[1,2,3],[]]
#p = [[],[],[1,2,3]]
#p = [[1,2,3],[],[]]
#dessine_disque(2, p, 3)
#dessine_disque(3, p, 3)
#dessine_disque(1, p, 3)

def efface_disque(nd, plateau, n):
    turtle.color('white')
    #turtle.speed('fastest')
    i, j, sortie = 0, 0, 0
    while (i < 3 and sortie == 0):
        while (j < len(plateau[i]) and sortie == 0):
            if (nd == plateau[i][j]):
                coord_x = (20 + 15*(n-nd)) + (40 + (30*n))*i
                if (len(plateau[i]) == 1):
                    coord_y = 0
                else:
                    coord_y = (20 * (n-nd))
                sortie = 1
            j += 1
        j = 0
        i += 1

    turtle.up()
    turtle.goto((-300) + coord_x, (-200) + coord_y)
    turtle.down()
    
    turtle.left(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward((40 + (30*(nd-1))))
    turtle.right(90)
    turtle.forward(20)
    turtle.left(90)

def dessine_config(plateau, n):
    i, j = 0, 0
    while (i < 3):
        while (j < len(plateau[i])):
            if (len(plateau[i]) != 0):
                dessine_disque(plateau[i][j], plateau, n)
            j += 1
        j = 0
        i += 1

#p = [[],[1,2,3],[]]
#dessine_config(p, 3)

def efface_tout(plateau, n):
    turtle.color('white')
    i, j = 0, 0
    while (i < 3):
        while (j < len(plateau[i])):
            if (len(plateau[i]) != 0):
                dessine_disque(plateau[i][j], plateau, n)
            j += 1
        i += 1

    #################### PARTIE INTERACTION JOUEUR ####################

def lire_coords(plateau):
    valide = 0
    coords = []
    while (valide != 1):
        t_dep = int(input("Choisis tour de départ: "))
        if (0 <= t_dep <= 2 and ((len(plateau[t_dep]) != 0))):
            valide = 1
    coords.append(t_dep)
    while (valide != 0):
        t_arriv = int(input("Choisis tour d'arrivée: "))
        if (0 <= t_arriv <= 2):
            if (len(plateau[t_arriv]) == 0):
                valide = 0
            elif (plateau[t_dep][len(plateau[t_dep])-1] < plateau[t_arriv][len(plateau[t_arriv])-1]):
                valide = 0
    coords.append(t_arriv)
    return coords

def jouer_un_coup(plateau, n):
    coords = lire_coords(plateau)
    val = plateau[coords[0]][0]
    efface_disque(val, plateau,n)
    plateau[coords[0]].remove(val)
    plateau[coords[1]].append(val)
    dessine_disque(val, plateau, n )

#jouer_un_coup(p,3)
#p = [[1,2,3],[],[]]
#p = [[],[1,2,3],[]]
#p = [[2],[1],[3]]
#dessine_config(p, 3)

def boucle_jeu(plateau, n):
    win = verifier_victoire(plateau,n)
    cpt = 0 #compteur de coups joué
    cpt_max = 10 #on initialise le nbr de coup max à 10
    while ((win != True) and (cpt < cpt_max)):
        jouer_un_coup(plateau,n)
        print(plateau)
        win = verifier_victoire(plateau,n)
        cpt += 1
    print("Formidable ! tu as gagné en:",cpt,", tu es vraiment beaucoup trop fort.")

def main():
    n = int(input("Avec combien de disque souhaite tu jouer ?"))
    liste_plateau = init(n)
    dessine_plateau(n)
    dessine_config(liste_plateau, n)
    boucle_jeu(liste_plateau, n)

main()