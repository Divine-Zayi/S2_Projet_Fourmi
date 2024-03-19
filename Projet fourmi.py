#Code inspiré du site : http://pascal.ortiz.free.fr/contents/tkinter/projets_tkinter/langton/langton.html

import tkinter as tk
SIDE = 1000
WIDTH = SIDE
HEIGHT = SIDE
DIM = 100
UNIT = SIDE // DIM
COLOR_OFF = 'snow'
COLOR_ON = 'gray16'
def make_grid():
    for j in range(nwidth):
        cnv.create_line((j * UNIT, 0), (j * UNIT, HEIGHT))
    for i in range(nheight):
        cnv.create_line((0, i * UNIT), (WIDTH, i * UNIT))


root = tk.Tk()
cnv = tk.Canvas(root, width=WIDTH, height=HEIGHT,
             background=COLOR_OFF)
cnv.pack()

nwidth = WIDTH // UNIT
nheight = HEIGHT // UNIT

make_grid()

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


#Boutons

import tkinter as tk

# Fonction pour démarrer la simulation
def demarrer_simulation():
    # Remplacer cette fonction par votre logique de simulation
    width, height = 10, 10  # Taille de la grille pour commencer
    grille = [[" "] * width for _ in range(height)]
    x, y = width // 2, height // 2
    grille[y][x] = "#"  # Position initiale de la fourmi
    for ligne in grille:
        print(" ".join(ligne))

# Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Simulation de la fourmi")

# Création du bouton pour démarrer
bouton_demarrer = tk.Button(fenetre, text="Démarrer", command=demarrer_simulation)
bouton_demarrer.pack(padx=10, pady=5)  # Ajouter un espace horizontal de 10 pixels et un espace vertical de 5 pixels

# Création du bouton pour arrêter 
bouton_arreter = tk.Button(fenetre, text="Arrêter", command=fenetre.quit)
bouton_arreter.pack(padx=10, pady=5) 

# Lancement de la boucle principale de la fenêtre
fenetre.mainloop()




grille.mainloop() # Lancement de la boucle principale LAISSER A LA FIN
#Interface graphique crée






