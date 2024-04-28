#Code inspiré du site : http://pascal.ortiz.free.fr/contents/tkinter/projets_tkinter/langton/langton.html et aide à la correction par chatgpt

import tkinter as tk
SIDE = 600
WIDTH = 600
HEIGHT = 600
DIM = 20
UNIT = SIDE // DIM
CASE = SIDE // 30
ARROW_WIDTH = CASE // 15
largeur_case = WIDTH // 7
hauteur_case = HEIGHT // 7
DELAY = 100 # Delai entre chaque animation 
COLOR_OFF = 'snow'
#COLOR_ON = 'gray16'
fourmi = None
canvas_fourmi=None

#Création d'une fonction pour mettre à jour la vitesse
def màj_vitesse(value):
    global DELAY
    DELAY = int(value)

#Position initiale de la fourmi à modifier d'ailleurs pur qu'elle soit au milieu
position = (DIM//2,DIM//2) #fourmi au centre de la grille
# position = (0,1) #fourmi au centre de la grille
direction = 'E'
grille = [[0]*DIM for _ in range(DIM)]




#Création de la grille 
def make_grid():
    for j in range(DIM):
        for i in range(DIM):
            x1 = j* UNIT
            y1 = i * UNIT
            x2 = x1 + UNIT
            y2 = y1 + UNIT
            canvas.create_rectangle(x1,y1,x2,y2,fill = COLOR_OFF)
        
    

#Initialisation de l'interface graphique
root = tk.Tk()
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT,
             background=COLOR_OFF)
canvas.grid(column=0,row=0,rowspan=2)
nwidth = WIDTH // UNIT
nheight = HEIGHT // UNIT
make_grid()

#Dessin de la fourmi
def dessin_fourmi(i, j, drn):
    x = j * UNIT + UNIT // 2
    y =i * UNIT + UNIT // 2  # Centrer la fourmi dans la case
    size = UNIT // 2
    if drn == 'N':
        return canvas.create_polygon(x, y - size, x - size, y + size, x + size, y + size, fill='purple')
    elif drn == 'S':
        return canvas.create_polygon(x, y + size, x - size, y - size, x + size, y - size, fill='purple')
    elif drn == 'E':
        return canvas.create_polygon(x + size, y, x - size, y - size, x - size, y + size, fill='purple')
    elif drn == 'O':
        return canvas.create_polygon(x - size, y, x + size, y - size, x + size, y + size, fill='purple')



#Fonction qui détermine la nouvelle position et direction de la fourmi
def bouger ( pos,drn,items):
    i,j=pos
    if items[i][j]==0:
        if drn =='N':
            r = (i-1,j), 'E'#j+1 monte vers le haut et je tourne à droite soit l'est
        elif drn=='S':
             r= (i+1, j), 'O' #j-1 descend case du bas et je tourne à droite soit l'ouest
        elif drn == 'E':
            r= (i,j+1),'S' # i+1 je tourne vers l'est et je tourne à droite soit le sud
        elif drn == 'O':
            r= (i,j-1), 'N' # i-1 je tourne vers l'ouest et je tourne à droite soit le nord
    else: #La case tombée est noir => tourne à gauche ( inverse coordonée case clair)
        if drn == 'N':
            r = (i-1,j),'O' #Je tourne à gauche
        elif drn == 'S':
            r = (i+1,j), 'E'
        elif drn == 'E':
            r = (i,j+1),'N'
        elif drn == 'O':
            r= ( i,j-1),'S'
    return r



#def case_courante(i,j):
    #if (i+j)%2 == 0:#Si la case est blanche
        #couleur = COLOR_ON
    #else : 
        #couleur = COLOR_ON  #Si la case est noir elle devient blanche
    #carré = canvas.create_rectangle((i * largeur_case, j * hauteur_case),
                                     #((i + 1) * largeur_case, (j + 1) * hauteur_case), fill=couleur)
    #return carré#Fonc

#Fonction qui dessine les cases
def dessin(pos,drn,items):
    global canvas_fourmi
    (ii,jj),ndrn = bouger(pos, drn,items)
    i,j=pos
    canvas.delete(canvas_fourmi)
    canvas_fourmi=dessin_fourmi(ii,jj,ndrn)
    if items[i][j] == 0: 
        # items[i][j] = dessin_fourmi(i,j,drn)

        # canvas.delete(items[i][j])
        items[i][j] = 1
        canvas.create_rectangle(j*UNIT, i * UNIT, (j+1)* UNIT, (i+1)* UNIT, fill='black') # colorier la case en blanche
    else :
        # canvas.delete(items[i][j])
        items[i][j] = 0
        canvas.create_rectangle(j*UNIT, i * UNIT, (j+1)* UNIT, (i+1)* UNIT, fill='white') # colorier la case en blanche
    return (ii, jj), ndrn



 #Liste historique pour stocker les étapes, je la mets endehors poru qu'elle soit accessible aux fonctions
historique = []

#Modifier la vitesse
#Création du curseur vitesse en utilisant l'outl scale
#Création d'une fonction pour mettre à jour la vitesse
def màj_vitesse(value):
    global DELAY
    DELAY = int(value)

#Création du curseur de vitesse
curseur_vitesse = tk.Scale(root,from_ = 50, to = 1500, orient = "horizontal",label='Speed', command=màj_vitesse)
curseur_vitesse.grid(column=1,row=3)

def faire_bouger_fourmi_essai():
    global position, direction, grille
    #position, direction = bouger(position,direction,grille)
    position, direction = dessin(position, direction,grille)

    #Répetition de la fonction apres le délai
    if not stop : 
        root.after(DELAY, faire_bouger_fourmi_essai)


#Fonction qui démarre la simulation
def démarrer():
    global stop, historique
    stop= False
    #Clear va effacer l'historique précedente
    historique.clear()
    faire_bouger_fourmi_essai()

#Fonction qui arrête la simulation
def arrêter():
    global stop
    stop = True
   
#Fonction du bouton suivant pour paser à la prochaine étape en gros c'est comme la fonction bouger sauf ue je crée un bouton suivant pour passer l'étape
def suivant():
    global position, direction, grille, historique
    #Ajout de l'historique des mouvement dans la grille
    historique.append([row[:] for row in grille])
    # position, direction = bouger(position,direction,grille)
    position, direction = dessin(position, direction, grille)


#Fonction qui définie la grille dessiner à partir de l'historique 
def dessiner_grille(grille):
    canvas.delete("all")#On efface tous
    for i in range( DIM):
        for j in range(DIM):
            x1 = j* UNIT
            y1 = i * UNIT
            x2 = x1 + UNIT
            y2 = y1 + UNIT
            
            


 #Fonction pour pouvoir revenir en arrière d'une étape
def revenir_en_arrière():
    global grille, historique
    if historique : 
        grille = historique.pop() #supprimer la grille d'avant 
        dessiner_grille(grille) #Nouvelle grille à definir

#Fonction qui dessine les cases
# def dessin(pos, drn, items):
#     (ii, jj), ndrn = bouger(pos, drn, items)
#     i, j = pos
#     if items[i][j] == 0:
#         items[i][j] = dessin_fourmi(i, j, drn)
#         canvas.itemconfig(items[i][j], fill='black')  # Colorier la case en noir
#     else:
#         canvas.delete(items[i][j])
#         items[i][j] = 0
#         canvas.create_rectangle(j * UNIT, i * UNIT, (j + 1) * UNIT, (i + 1) * UNIT, fill='white')  # Colorier la case en blanc
#     return (ii, jj), ndrn



# Création du bouton pour démarrer
bouton_demarrer = tk.Button(root, text="Démarrer", command= démarrer)
bouton_demarrer.grid(column=1, row=0)

#Création du bouton arrêter 
bouton_arreter = tk.Button(root, text="Arrêter", command= arrêter)
bouton_arreter.grid(column=1,row=1)

#Création du bouton suivant
bouton_suivant = tk.Button(root, text="Suivant", command= suivant)
bouton_suivant.grid(column=1,row=2)

#Creation bouton revenir en arrière
bouton_arrière = tk.Button(root,text="Revenir en arrière", command= revenir_en_arrière)
bouton_arrière.grid(column=2,row=1)

i,j=position
canvas_fourmi=dessin_fourmi(i,j,direction)




root.title("Simulation de la fourmi")



root.mainloop() # Lancement de la boucle principale LAISSER A LA FIN

