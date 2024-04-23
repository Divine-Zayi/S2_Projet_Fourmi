#Code inspiré du site : http://pascal.ortiz.free.fr/contents/tkinter/projets_tkinter/langton/langton.html

import tkinter as tk
SIDE = 700
WIDTH = 700
HEIGHT = 700
DIM = 100
UNIT = SIDE // DIM
CASE = SIDE // 30
ARROW_WIDTH = CASE // 100
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


def draw_arrow(i, j, drn):       #Définiton de la fourmi et et de la direction
    sep= CASE // 8
    S = (CASE // 2, CASE- sep ) 
    E = (sep, CASE // 2)
    O = (CASE - sep, CASE // 2)
    N = (CASE // 2, sep)
    StopAsyncIteration = (CASE // 2, CASE - sep)
    x, y = j * CASE, i * CASE
    if drn == (0, 1):
        A = (x + E[0], y + E[1])
        B = (x + O[0], y + O[1])
    elif drn ==  (-1, 0):
        A = (x + S[0], y + S[1])
        B = (x + N[0], y + N[1])
    elif drn ==  (0, -1):
        B = (x + E[0], y + E[1])
        A = (x + O[0], y + O[1])
    else:
        B = (x + S[0], y + S[1])
        A = (x + N[0], y + N[1])
    return canvas.create_line(
        A,
        B,
        width=ARROW_WIDTH,
        arrow='last',
        fill='red',
        arrowshape=(8, 10, 5))
print(draw_arrow(0,0,'N')) #Changer dimension Grille et Fourmi


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



#Fonction qui change la couleur de la case actuelle
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

#Fonction qui démarre la simulation
def démarrer_arreter(event):
    global stop 
    stop=not stop




 #Fonction intitialisation de la boucle
#def init():
    #global pos, drn, items,arr
    #cnv.delete("all")
    #cnv.focus_set()
    #make_grid()


# Fonction pour démarrer la simulation
def demarrer_simulation():
    # Remplacer cette fonction par votre logique de simulation
    width, height = 10, 10  # Taille de la grille pour commencer
    grille = [[" "] * width for _ in range(height)]
    x, y = width // 2, height // 2
    grille[y][x] = "#"  # Position initiale de la fourmi
    for ligne in grille:
        print(" ".join(ligne))
        




root.title("Simulation de la fourmi")

# Création du bouton pour démarrer
bouton_demarrer = tk.Button(root, text="Démarrer", command= démarrer_arreter)
bouton_demarrer.grid(column=1, row=0)  # Ajouter un espace horizontal de 10 pixels et un espace vertical de 5 pixels

# Création du bouton pour arrêter 
bouton_arreter = tk.Button(root, text="Arrêter", command=root.quit)
bouton_arreter.grid(column=1, row=1)

#Création du bouton pour ajouter une foumi

def add_ant():
   #"""Ajouter une nouvelle fourmi."""
    global position, direction, arrow
    position = (10, 10)  # Position initiale de la nouvelle fourmi
    direction = "UP"  # Direction initiale de la nouvelle fourmi
    arrow = cnv.create_text(position[0] * 30, position[1] * 30, text="", font=("Arial", 30), fill="pink")

boutton_ajout = tk.Button(root, text=" Ajouter une fourmi ", command=add_ant)
boutton_ajout.pack(column=1, row=2)

bouton_fermer = tk.Button(root, text="Fermer", command=root.destroy)
bouton_fermer.grid(column=1, row=3) #commande corrigé par le chatGPT
# Lancement de la boucle principale de la fenêtre



