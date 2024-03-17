#Code inspiré du site : http://pascal.ortiz.free.fr/contents/tkinter/projets_tkinter/langton/langton.html

import tkinter as tk

HEIGHT = 500
WIDTH = 500
SIDE = 500
UNIT= SIDE // 7
largeur_case = WIDTH // 7
hauteur_case = HEIGHT // 7
Color_OFF= 'old lace'
Color_ON='grey 16'
#items[i][j]= plateau dessiner par deplacement de la fourmi, 
#items==0 case blanche = déplacement droite
#pos=position de la fourmi (i,j)
#drn = direction N=Nord,S=Sud,E=Est,O=Ouest
#r = nouvelle position de la fourmi

#Fonction qui détermine la nouvelle position et direction de la fourmi
def bouger ( pos,drn,items):
    i,j=pos
    if items[i][j]==0:
        if drn =='N':
            r= (i,j+1), 'E'#j+1 monte vers le haut et je tourne à droite soit l'est
        elif drn=='S':
             r= (i, j-1), 'O' #j-1 descend case du bas et je tourne à droite soit l'ouest
        elif drn == 'E':
            r= (i+1,j),'S' # i+1 je tourne vers l'est et je tourne à droite soit le sud
        elif drn == 'O':
            r= (i-1,j), 'N' # i-1 je tourne vers l'ouest et je tourne à droite soit le nord
    else: #La case tombée est noir => tourne à gauche ( inverse coordonée case clair)
        if drn == 'N':
            r = (i,j-1),'O' #Je tourne à gauche
        elif drn == 'S':
            r = (i,j+1), 'E'
        elif drn == 'E':
            r = (i-1,j),'N'
        elif drn == 'O':
            r= ( i+1,j),'S'
    return r
grille = tk.Tk()
canvas=tk.Canvas(grille,bg=Color_OFF, height=HEIGHT, width=WIDTH)
canvas.pack(side='left')



#Fonction qui change l couleur de la case actuelle
def case_courante(i,j):
    if (i+j)%2 == 0:#Si la case est blanche
        couleur = Color_ON
    else : 
        couleur = Color_OFF  #Si la case est noir elle devient blanche
    carré = canvas.create_rectangle((i * largeur_case, j * hauteur_case),
                                     ((i + 1) * largeur_case, (j + 1) * hauteur_case), fill=couleur)
    return carré

#Fonction qui dessine les cases
#ndrn=r de la fonction bouger =  nouvelle pos et direction
def dessin(pos,drn,items):
    (ii,jj),ndrn = bouger(pos, drn,items)
    i,j=pos
    carré= items[i][j]

    if carré == 0 : #Case claire
        carré= dessin(i,j)
        items[i][j] = carré
    else : #Case noire, le carré sombre est supprimé
        canvas.delete(carré)
        items[i][j] = 0
    return (ii,jj),ndrn


#Il manque l'animation de la fourmi, la fourmi, et les touches de contrôle pour créer le mouvement




grille.mainloop() # Lancement de la boucle principale
#Interface graphique crée









