import random

# Fonction pour créer une grille de jeu
# La fonction creer reste inchangée
def creer():
    L = []
    for i in range(11): 
        C = []
        for j in range(11): 
            C.append(0) 
        L.append(C)
    
    for i in range(1, 11):
        L[i][0] = chr(65 + i - 1)
    for i in range(1, 11):
        L[0][i] = i
    return L

def affich(L): #nouvelle fonction affiche pour pouvoir afficher la grille du joueur pour voir son placement de bateaux
    # Affichage de la grille de bataille navale
    print("Bataille navale :\n")
    print("GRILLE JOUEUR")
    # Créer l'affichage ligne par ligne
    for i in range(0, 11):
        aff = []  # Liste pour la ligne actuelle
        for j in range(0, 11):
            
            if i > 0 and j > 0:  # On ne s'intéresse qu'aux indices positifs
                if L[i][j] == 0:
                    aff.append(" ")  # Case vide
                    aff.append("|")
                elif L[i][j] == 1:
                    aff.append("B")  # Barque (taille 1)
                    aff.append("|")
                elif L[i][j] == 2:
                    aff.append("T")  # Torpilleur (taille 2)
                    aff.append("|")
                elif L[i][j] == 3:
                    aff.append("S")  # Sous-marin (taille 3)
                    aff.append("|")
                elif L[i][j] == 4:
                    aff.append("C")  # Croiseur (taille 4)
                    aff.append("|")
                elif L[i][j] == 5:
                    aff.append("P")  # Porte-avion (taille 5)
                    aff.append("|")
                else:
                    aff.append(str(L[i][j]))  # En cas d'autre valeur (drapeaux, etc.)
                    aff.append("|")
            else:  # Pour la première ligne et la première colonne
                if L[i][j] == 0:
                    aff.append(" ")  # Case vide
                    aff.append("|")
                else:
                    aff.append(str(L[i][j]))  # Afficher la valeur (1-10 ou autres)
                    aff.append("|")
        
        # Afficher la ligne avec les séparateurs
        print(" ".join(aff))
        print("-" * 44)  # Séparateur après chaque ligne

def affichdouble(L,L1):
    # Affichage des deux grilles : celles du joueur et celle de l'ordinateur 
    print("Bataille navale :\n")
    print("GRILLE ORDINATEUR                               GRILLE JOUEUR")
    
    # Créer l'affichage ligne par ligne
    for i in range(0,11):
        aff = [] # Liste pour la ligne premiere grille
        aff1= [] # liste pour la ligne deuxième grille
        for j in range(11):
            if i>0:
                if L[i][j] in [0,1,2,3,4,5]:  
                    aff.append(" ")  
                    aff.append("|")
                elif L[i][j] in [21,31,41,51]:
                    aff.append("+")  
                    aff.append("|") 
                else:
                    aff.append((str(L[i][j])))  
                    aff.append("|")  
            elif i==0:
                if L[i][j]==0:  
                    aff.append(" ")  
                    aff.append("|") 
                else:
                    aff.append((str(L[i][j])))  
                    aff.append("|")  
            if i > 0:
                if L1[i][j] == 0:
                    aff1.append(" ")  # Case vide
                    aff1.append("|")
                elif L1[i][j]in[21,31,41,51]:
                    aff1.append("+")  
                    aff1.append("|")
                    
                elif L1[i][j] == 1:
                    aff1.append("B")  # Barque (taille 1)
                    aff1.append("|")
                elif L1[i][j] == 2:
                    aff1.append("T")  # Torpilleur (taille 2)
                    aff1.append("|")
                elif L1[i][j] == 3:
                    aff1.append("S")  # Sous-marin (taille 3)
                    aff1.append("|")
                elif L1[i][j] == 4:
                    aff1.append("C")  # Croiseur (taille 4)
                    aff1.append("|")
                elif L1[i][j] == 5:
                    aff1.append("P")  # Porte-avion (taille 5)
                    aff1.append("|")
                else:
                    aff1.append(str(L1[i][j]))  
                    aff1.append("|")
            else:  # Pour la première ligne et la première colonne
                if L1[i][j] == 0:
                    aff1.append(" ")  # Case vide
                    aff1.append("|")
                else:
                    aff1.append(str(L1[i][j]))  # Afficher la valeur (1-10 ou autres)
                    aff1.append("|")  
        
        
        
        # Afficher la ligne avec les séparateurs
        print(" ".join(aff) + "    " + " ".join(aff1))  # Séparation entre les deux grilles
        print("-" * 44 + "    " + "-" * 44)  # Séparateur après chaque ligne
 
    # Placement des bateaux de l'ordinateur
def placerordi(L):
 # Barque (taille 1)
     placed = False
     while placed!=True:
         xb = random.randint(1, 10)
         yb = random.randint(1, 10)
         if L[xb][yb] == 0:  # Si la case est libre
             L[xb][yb] = 1
             placed = True
     
     # Torpilleur (taille 2)
     placed = False
     while  placed!=True:
         xt = random.randint(1, 9)
         yt = random.randint(1, 9)
         direction = random.randint(0, 1)  # 0: horizontal, 1: vertical
         
         # Vérification de l'espace pour le torpilleur
         if direction == 1:  # Placement vertical
             if  L[xt][yt] == 0 and L[xt + 1][yt] == 0:
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
     while  placed !=True:
         xs1 = random.randint(1, 8)
         ys1 = random.randint(1, 8)
         rands = random.randint(0, 1)
         
         if rands == 1:  # Placement vertical
             if   L[xs1][ys1] == 0 and L[xs1 + 1][ys1] == 0 and L[xs1 + 2][ys1] == 0:
                 L[xs1][ys1] = 3
                 L[xs1 + 1][ys1] = 3
                 L[xs1 + 2][ys1] = 3
                 placed = True
         else:  # Placement horizontal
             if  L[xs1][ys1] == 0 and L[xs1][ys1 + 1] == 0 and L[xs1][ys1 + 2] == 0:
                 L[xs1][ys1] = 3
                 L[xs1][ys1 + 1] = 3
                 L[xs1][ys1 + 2] = 3
                 placed = True

     # Croiseur (taille 4)
     placed = False
     while  placed !=True:
         xtp1 = random.randint(1, 7)
         ytp1 = random.randint(1, 7)
         rands = random.randint(0, 1)
         
         if rands == 1:  # Placement vertical
             if  L[xtp1][ytp1] == 0 and L[xtp1 + 1][ytp1] == 0 and L[xtp1 + 2][ytp1] == 0 and L[xtp1 + 3][ytp1] == 0:
                 L[xtp1][ytp1] = 4
                 L[xtp1 + 1][ytp1] = 4
                 L[xtp1 + 2][ytp1] = 4
                 L[xtp1 + 3][ytp1] = 4
                 placed = True
         else:  # Placement horizontal
             if  L[xtp1][ytp1] == 0 and L[xtp1][ytp1 + 1] == 0 and L[xtp1][ytp1 + 2] == 0 and L[xtp1][ytp1 + 3] == 0:
                 L[xtp1][ytp1] = 4
                 L[xtp1][ytp1 + 1] = 4
                 L[xtp1][ytp1 + 2] = 4
                 L[xtp1][ytp1 + 3] = 4
                 placed = True
     
     # Porte-avion (taille 5)
     placed = False
     while placed !=True:
         xpa1 = random.randint(1, 6)
         ypa1 = random.randint(1, 6)
         rands = random.randint(0, 1)
         
         if rands == 1:  # Placement vertical
             if  L[xpa1][ypa1] == 0 and L[xpa1 + 1][ypa1] == 0 and L[xpa1 + 2][ypa1] == 0 and L[xpa1 + 3][ypa1] == 0 and L[xpa1 + 4][ypa1] == 0:
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

def placerbateaux(L):
    # Placement de la barque (taille 1)
    placed = False
    while not placed:
        # Demander la ligne (A-J)
        ligne = input("Où voulez-vous placer la barque (ligne A-J) ? ").upper()
        if len(ligne) != 1 or not ('A' <= ligne <= 'J'):
            print("Ligne invalide. Veuillez entrer une lettre de A à J.")
            continue
        xb = ord(ligne) - ord('A') + 1

        # Demander la colonne (1-10)
        yb = input("Dans quelle colonne (1-10) ? ")
        if not yb.isdigit() or not (1 <= int(yb) <= 10):
            print("Colonne invalide. Veuillez entrer un nombre entre 1 et 10.")
            continue
        yb = int(yb)

        # Vérifier que la case est libre
        if L[xb][yb] == 0:
            L[xb][yb] = 1
            placed = True
        else:
            print("Case occupée, essayez à nouveau.")
    affich(L)  # Affichage après placement de la barque

    # Placement du torpilleur (taille 2)
    placed = False
    while not placed:
        # Demander la ligne (A-J)
        ligne = input("Où voulez-vous placer le torpilleur (ligne A-J) ? ").upper()
        if len(ligne) != 1 or not ('A' <= ligne <= 'J'):
            print("Ligne invalide. Veuillez entrer une lettre de A à J.")
            continue
        xt = ord(ligne) - ord('A') + 1

        # Demander la colonne (1-10)
        yt = input("Dans quelle colonne (1-10) ? ")
        if not yt.isdigit() or not (1 <= int(yt) <= 10):
            print("Colonne invalide. Veuillez entrer un nombre entre 1 et 10.")
            continue
        yt = int(yt)

        # Demander la direction (0: horizontal, 1: vertical)
        direction = input("Direction ? 0: horizontal, 1: vertical : ")
        if not direction.isdigit() or int(direction) not in [0, 1]:
            print("Direction invalide. Veuillez entrer 0 pour horizontal ou 1 pour vertical.")
            continue
        direction = int(direction)

        # Vérifier l'espace pour le torpilleur
        if direction == 1:  # Placement vertical
            if xt + 1 <= 10 and L[xt][yt] == 0 and L[xt + 1][yt] == 0:
                L[xt][yt] = 2
                L[xt + 1][yt] = 2
                placed = True
        else:  # Placement horizontal
            if yt + 1 <= 10 and L[xt][yt] == 0 and L[xt][yt + 1] == 0:
                L[xt][yt] = 2
                L[xt][yt + 1] = 2
                placed = True
        if not placed:
            print("Espace invalide ou occupé. Essayez à nouveau.")
    affich(L)  # Affichage après placement du torpilleur

    # Placement du sous-marin (taille 3)
    placed = False
    while not placed:
        # Demander la ligne (A-J)
        ligne = input("Où voulez-vous placer le sous-marin (ligne A-J) ? ").upper()
        if len(ligne) != 1 or not ('A' <= ligne <= 'J'):
            print("Ligne invalide. Veuillez entrer une lettre de A à J.")
            continue
        xs = ord(ligne) - ord('A') + 1

        # Demander la colonne (1-10)
        ys = input("Dans quelle colonne (1-10) ? ")
        if not ys.isdigit() or not (1 <= int(ys) <= 10):
            print("Colonne invalide. Veuillez entrer un nombre entre 1 et 10.")
            continue
        ys = int(ys)

        # Demander la direction (0: horizontal, 1: vertical)
        direction = input("Direction ? 0: horizontal, 1: vertical : ")
        if not direction.isdigit() or int(direction) not in [0, 1]:
            print("Direction invalide. Veuillez entrer 0 pour horizontal ou 1 pour vertical.")
            continue
        direction = int(direction)

        # Vérifier l'espace pour le sous-marin
        if direction == 1:  # Placement vertical
            if xs + 2 <= 10 and L[xs][ys] == 0 and L[xs + 1][ys] == 0 and L[xs + 2][ys] == 0:
                L[xs][ys] = 3
                L[xs + 1][ys] = 3
                L[xs + 2][ys] = 3
                placed = True
        else:  # Placement horizontal
            if ys + 2 <= 10 and L[xs][ys] == 0 and L[xs][ys + 1] == 0 and L[xs][ys + 2] == 0:
                L[xs][ys] = 3
                L[xs][ys + 1] = 3
                L[xs][ys + 2] = 3
                placed = True
        if not placed:
            print("Espace invalide ou occupé. Essayez à nouveau.")
    affich(L)  # Affichage après placement du sous-marin

    # Placement du croiseur (taille 4)
    placed = False
    while not placed:
        # Demander la ligne (A-J)
        ligne = input("Où voulez-vous placer le croiseur (ligne A-J) ? ").upper()
        if len(ligne) != 1 or not ('A' <= ligne <= 'J'):
            print("Ligne invalide. Veuillez entrer une lettre de A à J.")
            continue
        xc = ord(ligne) - ord('A') + 1

        # Demander la colonne (1-10)
        yc = input("Dans quelle colonne (1-10) ? ")
        if not yc.isdigit() or not (1 <= int(yc) <= 10):
            print("Colonne invalide. Veuillez entrer un nombre entre 1 et 10.")
            continue
        yc = int(yc)

        # Demander la direction (0: horizontal, 1: vertical)
        direction = input("Direction ? 0: horizontal, 1: vertical : ")
        if not direction.isdigit() or int(direction) not in [0, 1]:
            print("Direction invalide. Veuillez entrer 0 pour horizontal ou 1 pour vertical.")
            continue
        direction = int(direction)

        # Vérifier l'espace pour le croiseur
        if direction == 1:  # Placement vertical
            if xc + 3 <= 10 and L[xc][yc] == 0 and L[xc + 1][yc] == 0 and L[xc + 2][yc] == 0 and L[xc + 3][yc] == 0:
                L[xc][yc] = 4
                L[xc + 1][yc] = 4
                L[xc + 2][yc] = 4
                L[xc + 3][yc] = 4
                placed = True
        else:  # Placement horizontal
            if yc + 3 <= 10 and L[xc][yc] == 0 and L[xc][yc + 1] == 0 and L[xc][yc + 2] == 0 and L[xc][yc + 3] == 0:
                L[xc][yc] = 4
                L[xc][yc + 1] = 4
                L[xc][yc + 2] = 4
                L[xc][yc + 3] = 4
                placed = True
        if not placed:
            print("Espace invalide ou occupé. Essayez à nouveau.")
    affich(L)  # Affichage après placement du croiseur

    # Placement du porte-avion (taille 5)
    placed = False
    while not placed:
        # Demander la ligne (A-J)
        ligne = input("Où voulez-vous placer le porte-avion (ligne A-J) ? ").upper()
        if len(ligne) != 1 or not ('A' <= ligne <= 'J'):
            print("Ligne invalide. Veuillez entrer une lettre de A à J.")
            continue
        xp = ord(ligne) - ord('A') + 1

        # Demander la colonne (1-10)
        yp = input("Dans quelle colonne (1-10) ? ")
        if not yp.isdigit() or not (1 <= int(yp) <= 10):
            print("Colonne invalide. Veuillez entrer un nombre entre 1 et 10.")
            continue
        yp = int(yp)

        # Demander la direction (0: horizontal, 1: vertical)
        direction = input("Direction ? 0: horizontal, 1: vertical : ")
        if not direction.isdigit() or int(direction) not in [0, 1]:
            print("Direction invalide. Veuillez entrer 0 pour horizontal ou 1 pour vertical.")
            continue
        direction = int(direction)

        # Vérifier l'espace pour le porte-avion
        if direction == 1:  # Placement vertical
            if xp + 4 <= 10 and L[xp][yp] == 0 and L[xp + 1][yp] == 0 and L[xp + 2][yp] == 0 and L[xp + 3][yp] == 0 and L[xp + 4][yp] == 0:
                L[xp][yp] = 5
                L[xp + 1][yp] = 5
                L[xp + 2][yp] = 5
                L[xp + 3][yp] = 5
                L[xp + 4][yp] = 5
                placed = True
        else:  # Placement horizontal
            if yp + 4 <= 10 and L[xp][yp] == 0 and L[xp][yp + 1] == 0 and L[xp][yp + 2] == 0 and L[xp][yp + 3] == 0 and L[xp][yp + 4] == 0:
                L[xp][yp] = 5
                L[xp][yp + 1] = 5
                L[xp][yp + 2] = 5
                L[xp][yp + 3] = 5
                L[xp][yp + 4] = 5
                placed = True
        if not placed:
            print("Espace invalide ou occupé. Essayez à nouveau.")
    affich(L)


def coup():
    while True:
        print("Dans quelle ligne et qulle colonne ?")
        ligne=input("ligne A-J:")
        ligne=ligne.upper()
        colonne=input("Colonnne 1-10:")
        if len(ligne) == 1 and ligne in "ABCDEFGHIJ" and colonne.isdigit() and 1 <= int(colonne) and int(colonne) <=10:#conditions pour que le coup soit valide
            return ord(ligne)-64, int(colonne)
        else:
            print("veuillez réessayer")
   

def coupordinateur():
    ligne=random.choice("ABCDEFGHIJ")
    colonne=random.randint(1,10)
    x=ord(ligne)-64
    y=colonne
    return x,y
        


def jouer(grille, i, j,compteurs):
    barque,torp, sousm, crois, porta = compteurs['barque'], compteurs['torp'], compteurs['sousm'], compteurs['crois'], compteurs['porta']
    # mise en place du dictionnaire compteurs car sinon on arrive pas compter correctement quand il faut changer les cases + en X car les compteurs se remettaient a 0 a chaque appel de la focntion
    if grille[i][j] == 0:  # L'eau, pas de navire
        grille[i][j] = '*'  # Marquer l'eau comme touchée
        print("Manqué")
    elif grille[i][j] == 1 :  # Barque
        grille[i][j] = 'X'
        compteurs['barque']+=1
        print("Touché et coulé !")
    elif grille[i][j] == 2:  # Torpilleur
        grille[i][j] = 21
        compteurs['torp'] += 1
        print("Touché")
        if compteurs['torp'] == 2:
            for x in range(11):
                for y in range(11):
                    if grille[x][y] == 21:
                        grille[x][y] = "X"
            print("et coulé !")
    elif grille[i][j] == 3:  # Sous-marin
        grille[i][j] = 31
        compteurs['sousm']+= 1
        print("Touché")
        if compteurs['sousm'] == 3:
            for x in range(11):
                for y in range(11):
                    if grille[x][y] == 31:
                        grille[x][y] = "X"
            print("et coulé !")
    elif grille[i][j] == 4:  # Croiseur
        grille[i][j] = 41
        compteurs['crois'] += 1
        print("Touché")
        if compteurs['crois'] == 4:
            for x in range(11):
                for y in range(11):
                    if grille[x][y] == 41:
                        grille[x][y] = "X"
            print("et coulé !")
    elif grille[i][j] == 5:  # Porte-avion
        grille[i][j] = 51
        compteurs['porta'] += 1
        print("Touché")
        if compteurs['porta'] == 5:
            for x in range(11):
                for y in range(11):
                    if grille[x][y] == 51:
                        grille[x][y] = "X"
            print("et coulé !")

    return torp, sousm, crois, porta
    

def jouerordi(grille_joueur, i, j, compteurso):
    """
    Fonction qui gère les tirs de l'ordinateur sur la grille du joueur.
    Lorsque l'ordinateur touche un bateau, le compteur correspondant est incrémenté.
    Si le bateau est coulé, toutes ses parties sont remplacées par 'X'.
    """
    
    # Récupération des compteurs de bateaux
    barque, torp, sousm, crois, porta = compteurso['barque'], compteurso['torp'], compteurso['sousm'], compteurso['crois'], compteurso['porta']
    
    # Vérification du type de case (eau, barque, torpilleur, sous-marin, croiseur, porte-avion)
    if grille_joueur[i][j] == 0:  # L'eau, pas de navire (O pour eau)
        grille_joueur[i][j] = '*'  # Marquer l'eau comme touchée
        print("Manqué")
    elif grille_joueur[i][j] == 1:  # Barque
        grille_joueur[i][j] = "X"  # Marquer comme touché et coulé
        compteurso['barque'] += 1  # Incrémenter le compteur pour la barque
        print("Touché et coulé !")
    elif grille_joueur[i][j] == 2:  # Torpilleur
        grille_joueur[i][j] =21  # Marquer comme touché (temporairement '21')
        compteurso['torp'] += 1  # Incrémenter le compteur pour le torpilleur
        print("Touché")
        if compteurso['torp'] == 2:  # Si toutes les parties du torpilleur sont touchées
            # Remplacer toutes les parties du torpilleur par 'X'
            for x in range(11):
                for y in range(11):
                    if grille_joueur[x][y] == 21:
                        grille_joueur[x][y] = "X"
            print("et coulé !")
    elif grille_joueur[i][j] == 3:  # Sous-marin
        grille_joueur[i][j] = 31  # Marquer comme touché (temporairement '31')
        compteurso['sousm'] += 1  # Incrémenter le compteur pour le sous-marin
        print("Touché")
        if compteurso['sousm'] == 3:  # Si toutes les parties du sous-marin sont touchées
            # Remplacer toutes les parties du sous-marin par 'X'
            for x in range(11):
                for y in range(11):
                    if grille_joueur[x][y] == 31:
                        grille_joueur[x][y] = "X"
            print("et coulé !")
    elif grille_joueur[i][j] == 4:  # Croiseur
        grille_joueur[i][j] = 41  # Marquer comme touché (temporairement '41')
        compteurso['crois'] += 1  # Incrémenter le compteur pour le croiseur
        print("Touché")
        if compteurso['crois'] == 4:  # Si toutes les parties du croiseur sont touchées
            # Remplacer toutes les parties du croiseur par 'X'
            for x in range(11):
                for y in range(11):
                    if grille_joueur[x][y] == 41:
                        grille_joueur[x][y] = "X"
            print("et coulé !")
    elif grille_joueur[i][j] == 5:  # Porte-avion
        grille_joueur[i][j] = 51  # Marquer comme touché (temporairement '51')
        compteurso['porta'] += 1  # Incrémenter le compteur pour le porte-avion
        print("Touché")
        if compteurso['porta'] == 5:  # Si toutes les parties du porte-avion sont touchées
            # Remplacer toutes les parties du porte-avion par 'X'
            for x in range(11):
                for y in range(11):
                    if grille_joueur[x][y] == 51:
                        grille_joueur[x][y] = "X"
            print("et coulé !")

    # Retourner les compteurs mis à jour
    return torp,sousm,crois,porta


def lancerjeu2():
    L=creer()
    L1=creer()
    affich(L)
    placerbateaux(L)
    placerordi(L1)
    affichdouble(L1,L)
    partie_terminee=False
    partie_termineeord=False
    compteurs = {
         'barque': 0,
         'torp': 0,
         'sousm': 0,
         'crois': 0,
         'porta': 0
     } 
    compteurso = {
         'barque': 0,
         'torp': 0,
         'sousm': 0,
         'crois': 0,
         'porta': 0
     } 
    while partie_terminee!=True and partie_termineeord!=True:
        i,j=coup()
        partie_terminee=jouer(L1,i,j,compteurs)
        affichdouble(L1,L)
        x,y=coupordinateur()
        while L[x][y]=="*" or L[x][y] in [21,31,41,51] or L[x][y]=="X":
            x,y=coupordinateur()
        partie_termineeord=jouerordi(L,x,y,compteurso)
        affichdouble(L1,L)
        if all(compteurs[k] == v for k, v in {'barque':1,'torp': 2, 'sousm': 3, 'crois': 4, 'porta': 5}.items()) :
            affichdouble(L1,L)
            partie_terminee = True
            print("Tous les bateaux ont été coulés, victoire du joueur !")
        
        elif all(compteurso[k] == v for k, v in {'barque':1,'torp': 2, 'sousm': 3, 'crois': 4, 'porta': 5}.items()):
            affichdouble(L1,L)
            
            partie_termineeord=True
            print("Tous les bateaux ont été coulés, victoire de l'ordinateur!")
    print("Partie terminée")
    
lancerjeu2()
   
    
    
    
    
    
    
    
    
    
    