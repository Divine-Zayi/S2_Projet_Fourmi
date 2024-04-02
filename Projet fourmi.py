
#Code inspiré du site : http://pascal.ortiz.free.fr/contents/tkinter/projets_tkinter/langton/langton.html

import tkinter as tk
SIDE = 700
WIDTH = SIDE
HEIGHT = SIDE
DIM = 100
UNIT = SIDE // DIM
largeur_case = WIDTH // 7
hauteur_case = HEIGHT // 7
COLOR_OFF = 'snow'
COLOR_ON = 'gray16'
def make_grid():
    for j in range(nwidth):
        canvas.create_line((j * UNIT, 0), (j * UNIT, HEIGHT))
    for i in range(nheight):
        canvas.create_line((0, i * UNIT), (WIDTH, i * UNIT))


root = tk.Tk()
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT,
             background=COLOR_OFF)
canvas.grid(column=0,row=0,rowspan=2)

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
#root = tk.Tk()
#canvas=tk.Canvas(root,bg=COLOR_OFF, height=HEIGHT, width=WIDTH)
#canvas.pack(side='left')



#Fonction qui change l couleur de la case actuelle
def case_courante(i,j):
    if (i+j)%2 == 0:#Si la case est blanche
        couleur = COLOR_ON
    else : 
        couleur = COLOR_ON  #Si la case est noir elle devient blanche
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
# fenetre = tk.Tk()
        root.title("Simulation de la fourmi")

# Création du bouton pour démarrer
bouton_demarrer = tk.Button(root, text="Démarrer", command=bouger and case_courante and demarrer_simulation)
bouton_demarrer.grid(column=1, row=0)  # Ajouter un espace horizontal de 10 pixels et un espace vertical de 5 pixels

# Création du bouton pour arrêter 
bouton_arreter = tk.Button(root, text="Arrêter", command=root.quit)
bouton_arreter.grid(column=1, row=1)

# Lancement de la boucle principale de la fenêtre

def draw_arrow(i, j, drn):       #Définiton de la fourmi et et de la direction
    sep = CASE // 8
    east = (sep, CASE // 2)
    west = (CASE - sep, CASE // 2)
    north = (CASE // 2, sep)
    south = (CASE // 2, CASE - sep)
    x, y = j * CASE, i * CASE
    if drn == (0, 1):
        A = (x + east[0], y + east[1])
        B = (x + west[0], y + west[1])
    elif drn ==  (-1, 0):
        A = (x + south[0], y + south[1])
        B = (x + north[0], y + north[1])
    elif drn ==  (0, -1):
        B = (x + east[0], y + east[1])
        A = (x + west[0], y + west[1])
    else:
        B = (x + south[0], y + south[1])
        A = (x + north[0], y + north[1])
    return cnv.create_line(
        A,
        B,
        width=ARROW_WIDTH,
        arrow='last',
        fill='red',
        arrowshape=(18, 30, 8))


boutton_ajout = tk.Button(fenetre, text="Ajouter une fourmi", command=add_ant)
boutton_ajout.pack()


#Il manque l'animation de la fourmi, la fourmi, et les touches de contrôle pour créer le mouvement




root.mainloop() # Lancement de la boucle principale LAISSER A LA FIN
#Interface graphique crée
