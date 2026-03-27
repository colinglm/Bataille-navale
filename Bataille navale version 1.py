import random

# Fonction pour créer la grille de jeu
def creer():
    L = []
    for i in range(11):  # On initialise une grille vide de 11 lignes
        C = []
        for j in range(11):  # On ajoute des 0 partout
            C.append(0)
        L.append(C)
    
    # Ajouter les labels de lignes (A-J)
    for i in range(1, 11):
        L[i][0] = chr(65 + i - 1)  # On utilise la table ASCII pour ajouter plus rapidement les indices de lignes(A-J)
    # On ajoute les indices de colonnes (1-10)
    for i in range(1, 11):
        L[0][i] = i
    return L

# Fonction pour afficher la grille de jeu
# Les symboles visuels permettent de représenter l'état des cases :
# ' ' pour une case vide, '+' pour une partie touchée, '*' pour une tentative ratée, et 'X' pour un bateau coulé
def affich(L):
    print("Bataille navale :\n")
    for i in range(11):  
        aff = []  # Liste qui nous servira d'affichage
        for j in range(11): 
            if i > 0:  # Si ce n'est pas la première ligne (indicateur de colonnes)
                if L[i][j] in [0, 1, 2, 3, 4, 5]:
                    aff.append(" ")  # Case vide ou bateau non touché
                    aff.append("|")  # Séparateur vertical
                elif L[i][j] in [21, 31, 41, 51]:
                    aff.append("+")  # Partie touchée d'un bateau
                    aff.append("|")
                else:
                    aff.append(str(L[i][j]))  # Autres cas (comme les indices ou '*' pour raté)
                    aff.append("|")
            elif i == 0:  # Première ligne (indicateurs de colonnes)
                if L[i][j] == 0:
                    aff.append(" ")  # Case vide dans le coin supérieur gauche
                    aff.append("|")
                else:
                    aff.append(str(L[i][j]))  # Numéros de colonnes
                    aff.append("|")
        print(" ".join(aff))  # Afficher la ligne construite
        print("-" * 44)  # Ligne de séparation horizontale

# Fonction pour placer aléatoirement les bateaux sur la grille
def placer(L):
    # Barque (taille 1)
    placed = False
    while not placed:  # Répéter jusqu'à ce qu'un emplacement valide soit trouvé
        xb = random.randint(1, 10)  # Choisir une ligne aléatoire
        yb = random.randint(1, 10)  # Choisir une colonne aléatoire
        if L[xb][yb] == 0:  # Vérifier que la case est vide
            L[xb][yb] = 1  # Placer la barque
            placed = True

    # Torpilleur (taille 2)
    placed = False
    while not placed:
        xt = random.randint(1, 9)  # Limiter les bornes pour éviter de sortir de la grille
        yt = random.randint(1, 9)
        direction = random.randint(0, 1)  # Choisir une direction : 0 pour horizontal, 1 pour vertical
        if direction == 1:  # Placement vertical
            if L[xt][yt] == 0 and L[xt + 1][yt] == 0:  # Vérifier deux cases consécutives
                L[xt][yt] = 2
                L[xt + 1][yt] = 2
                placed = True
        else:  # Placement horizontal
            if L[xt][yt] == 0 and L[xt][yt + 1] == 0:
                L[xt][yt] = 2
                L[xt][yt + 1] = 2
                placed = True

    # Sous-marin (taille 3)
    placed = False
    while not placed:
        xs1 = random.randint(1, 8)  
        ys1 = random.randint(1, 8)
        rands = random.randint(0, 1) 
        if rands == 1:  # Placement vertical
            if L[xs1][ys1] == 0 and L[xs1 + 1][ys1] == 0 and L[xs1 + 2][ys1] == 0:
                L[xs1][ys1] = 3
                L[xs1 + 1][ys1] = 3
                L[xs1 + 2][ys1] = 3
                placed = True
        else:  # Placement horizontal
            if L[xs1][ys1] == 0 and L[xs1][ys1 + 1] == 0 and L[xs1][ys1 + 2] == 0:
                L[xs1][ys1] = 3
                L[xs1][ys1 + 1] = 3
                L[xs1][ys1 + 2] = 3
                placed = True

    # Croiseur (taille 4)
    placed = False
    while not placed:
        xtp1 = random.randint(1, 7) 
        ytp1 = random.randint(1, 7)
        rands = random.randint(0, 1) 
        if rands == 1:  # Placement vertical
            if L[xtp1][ytp1] == 0 and L[xtp1 + 1][ytp1] == 0 and L[xtp1 + 2][ytp1] == 0 and L[xtp1 + 3][ytp1] == 0:
                L[xtp1][ytp1] = 4
                L[xtp1 + 1][ytp1] = 4
                L[xtp1 + 2][ytp1] = 4
                L[xtp1 + 3][ytp1] = 4
                placed = True
        else:  # Placement horizontal
            if L[xtp1][ytp1] == 0 and L[xtp1][ytp1 + 1] == 0 and L[xtp1][ytp1 + 2] == 0 and L[xtp1][ytp1 + 3] == 0:
                L[xtp1][ytp1] = 4
                L[xtp1][ytp1 + 1] = 4
                L[xtp1][ytp1 + 2] = 4
                L[xtp1][ytp1 + 3] = 4
                placed = True

    # Porte-avion (taille 5)
    placed = False
    while not placed:
        xpa1 = random.randint(1, 6) 
        ypa1 = random.randint(1, 6)
        rands = random.randint(0, 1)  
        if rands == 1:  # Placement vertical
            if L[xpa1][ypa1] == 0 and L[xpa1 + 1][ypa1] == 0 and L[xpa1 + 2][ypa1] == 0 and L[xpa1 + 3][ypa1] == 0 and L[xpa1 + 4][ypa1] == 0:
                L[xpa1][ypa1] = 5
                L[xpa1 + 1][ypa1] = 5
                L[xpa1 + 2][ypa1] = 5
                L[xpa1 + 3][ypa1] = 5
                L[xpa1 + 4][ypa1] = 5
                placed = True
        else:  # Placement horizontal
            if L[xpa1][ypa1] == 0 and L[xpa1][ypa1 + 1] == 0 and L[xpa1][ypa1 + 2] == 0 and L[xpa1][ypa1 + 3] == 0 and L[xpa1][ypa1 + 4] == 0:
                L[xpa1][ypa1] = 5
                L[xpa1][ypa1 + 1] = 5
                L[xpa1][ypa1 + 2] = 5
                L[xpa1][ypa1 + 3] = 5
                L[xpa1][ypa1 + 4] = 5
                placed = True

# Fonction pour effectuer un tir sur la grille
def jouer(grille, i, j, compteurs):
    # Les compteurs servent à suivre l'état de chaque type de bateau touché
    if grille[i][j] == 0:  # Case vide, tir raté
        grille[i][j] = '*'
        print("Manqué")
    elif grille[i][j] == 1:  # Barque
        grille[i][j] = 'X'
        compteurs['barque'] += 1
        print("Touché et coulé !")
    elif grille[i][j] == 2:  # Torpilleur
        grille[i][j] = 21
        compteurs['torp'] += 1
        print("Touché")
        if compteurs['torp'] == 2:  # Si toutes les parties du torpilleur sont touchées
            for x in range(11):
                for y in range(11):
                    if grille[x][y] == 21:
                        grille[x][y] = "X"
            print("et coulé !")
    elif grille[i][j] == 3:  # Sous-marin
        grille[i][j] = 31
        compteurs['sousm'] += 1
        print("Touché")
        if compteurs['sousm'] == 3:  # Si toutes les parties du sous-marin sont touchées
            for x in range(11):
                for y in range(11):
                    if grille[x][y] == 31:
                        grille[x][y] = "X"
            print("et coulé !")
    elif grille[i][j] == 4:  # Croiseur
        grille[i][j] = 41
        compteurs['crois'] += 1
        print("Touché")
        if compteurs['crois'] == 4:  # Si toutes les parties du croiseur sont touchées
            for x in range(11):
                for y in range(11):
                    if grille[x][y] == 41:
                        grille[x][y] = "X"
            print("et coulé !")
    elif grille[i][j] == 5:  # Porte-avion
        grille[i][j] = 51
        compteurs['porta'] += 1
        print("Touché")
        if compteurs['porta'] == 5:  # Si toutes les parties du porte-avion sont touchées
            for x in range(11):
                for y in range(11):
                    if grille[x][y] == 51:
                        grille[x][y] = "X"
            print("et coulé !")

# Fonction pour demander une tentative au joueur
def coup():
    while True:
        print("Dans quelle ligne et quelle colonne ?")
        ligne = input("ligne A-J:").upper()
        colonne = input("Colonne 1-10:")
        if len(ligne) == 1 and ligne in "ABCDEFGHIJ" and colonne.isdigit() and 1 <= int(colonne) <= 10: #On verifie que le coup est bien valide
            return ord(ligne) - 64, int(colonne)  # Convertir la lettre en numéro de ligne
        else:
            print("Veuillez réessayer")

# Fonction principale pour lancer le jeu
def lancer_jeu():
    grille = creer()  # Créer la grille
    placer(grille)  # Placer les bateaux

    compteurs = {  # Initialiser les compteurs pour chaque type de bateau
        'barque': 0,
        'torp': 0,
        'sousm': 0,
        'crois': 0,
        'porta': 0
    }

    partie_terminee = False

    while not partie_terminee:
        affich(grille)  # Afficher la grille
        i, j = coup()  # Obtenir les coordonnées du joueur
        jouer(grille, i, j, compteurs)  # Effectuer un tir
        if all(compteurs[k] == v for k, v in {'barque': 1, 'torp': 2, 'sousm': 3, 'crois': 4, 'porta': 5}.items()):
            for x in range(11):
                for y in range(11):
                    if grille[x][y] in [21, 31, 41, 51]:
                        grille[x][y] = "X"
            affich(grille)
            print("Tous les bateaux ont été coulés !")
            partie_terminee = True

    print("Partie terminée")

lancer_jeu()
