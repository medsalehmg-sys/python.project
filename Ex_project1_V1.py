# project 1: Version 1:

# On charge tkinter : la bibliothèque qui permet de faire des fenêtres.
# Le * veut dire "prends tout" (Tk, Frame, Label, Button, Menu...).
from tkinter import *

# ---------------------------------------------------------
# 1. LA FENÊTRE
# ---------------------------------------------------------
window = Tk()                          # crée la fenêtre principale
window.title("XO game")                # texte dans la barre du haut
window.geometry("800x600")             # taille au départ : 800 de large, 600 de haut
window.config(background="black")     # couleur de fond de la fenêtre
window.minsize(400, 300)               # taille minimum possible
window.maxsize(1200, 900)              # taille maximum possible
window.iconbitmap(r"c:\Users\EL-ITKAN\Downloads\logo_xo.ico")   # icône en haut à gauche

# ---------------------------------------------------------
# 2. LE TITRE
# ---------------------------------------------------------
# Un Frame est une boîte invisible qui contient d'autres éléments.
# Le premier paramètre (window) dit où on met la boîte.
frame = Frame(window, background="black")
frame.pack()   # pack() AFFICHE la boîte. Sans lui, elle reste invisible.

# Un Label affiche du texte. Il est rangé dans la boîte "frame".
general_title = Label(frame, text=" Welcome to XO game", font=("Arial", 30, "bold"),
                      background="black", foreground="white")
general_title.pack(pady=10, padx=20)   # pady = espace en haut/bas, padx = à gauche/droite

# ---------------------------------------------------------
# 3. LA BOÎTE DU PLATEAU
# ---------------------------------------------------------
# Une deuxième boîte (violette) qui contiendra les 9 boutons.
# pack() la place SOUS la première boîte.
frame_2 = Frame(window, background="purple")
frame_2.pack()

# ---------------------------------------------------------
# 4. LES VARIABLES DU JEU
# ---------------------------------------------------------
# La "pancarte" : elle dit à qui est le tour. On commence par X.
tour = "X"

# Les 8 façons de gagner. Les chiffres sont les numéros des cases :
#  0 | 1 | 2
#  3 | 4 | 5
#  6 | 7 | 8
combinaisons = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),   # les 3 lignes
    (0, 3, 6), (1, 4, 7), (2, 5, 8),   # les 3 colonnes
    (0, 4, 8), (2, 4, 6)               # les 2 diagonales
]

# ---------------------------------------------------------
# 5. LES FONCTIONS
# ---------------------------------------------------------

# restart : remet le jeu à zéro (appelée par le menu "Restart").
def restart():
    global tour                                      # permet de MODIFIER la variable tour qui est dehors
    tour = "X"                                       # X recommence
    general_title.config(text=" Welcome to XO game") # on remet le titre d'origine
    for b in casier:                                 # on passe sur les 9 boutons...
        b.config(text="")                            # ...et on efface leur texte
    # Remarque : "casier" est créé plus bas, mais ce n'est pas grave.
    # Python ne le cherche qu'au moment où on APPELLE restart (au clic sur le menu).

# verification_victory : regarde s'il y a 3 symboles alignés.
def verification_victory():
    for x, y, z in combinaisons:            # on prend les trios gagnants un par un
        t1 = casier[x].cget("text")         # cget("text") LIT le texte d'une case : "X", "O" ou ""
        t2 = casier[y].cget("text")
        t3 = casier[z].cget("text")
        # Deux conditions : la 1re case n'est pas vide, ET les 3 cases sont identiques.
        # Le == compare. Le != veut dire "est différent de".
        if t1 != "" and t1 == t2 == t3:
            general_title.config(text="Le joueur " + t1 + " a gagné !")   # le titre affiche le gagnant

# clic : appelée à chaque clic sur une case. "b" est le bouton cliqué.
def clic(b):
    global tour                              # on va modifier la pancarte tour
    if b.cget("text") == "":                 # si la case est VIDE...
        b.config(text=tour)                  # ...on y écrit X ou O (selon le tour)
        if tour == "X":                      # puis on change le tour :
            tour = "O"                       # X devient O
        else:
            tour = "X"                       # O devient X
    verification_victory()                   # à chaque clic, on regarde si quelqu'un a gagné

# ---------------------------------------------------------
# 6. CRÉATION DES 9 BOUTONS
# ---------------------------------------------------------
casier = []                                  # une liste vide : la "boîte" qui gardera les 9 boutons
for i in range(3):                           # i = numéro de la ligne : 0, 1, 2
    for j in range(3):                       # j = numéro de la colonne : 0, 1, 2  (3 x 3 = 9 tours)
        # on crée un bouton vide, rangé dans frame_2
        bouton = Button(frame_2, text="", font=("Arial", 35, "bold"), fg="red")
        # grid place le bouton dans la grille, à sa ligne et sa colonne
        bouton.grid(row=i, column=j)
        # command = ce qui se passe au clic.
        # lambda "attend" le clic, puis appelle clic(b) avec CE bouton.
        # Le "b=bouton" fige le bon bouton pour chaque tour de la boucle.
        bouton.config(command=lambda b=bouton: clic(b))
        # on range le bouton dans la liste : il reçoit son numéro, de 0 à 8
        casier.append(bouton)

# ---------------------------------------------------------
# 7. LE MENU
# ---------------------------------------------------------
menu_bar = Menu(window)                                  # la barre de menu en haut de la fenêtre
file_menu = Menu(menu_bar, tearoff=0, font=("Arial", 15, "bold"))   # la liste déroulante (tearoff=0 enlève les pointillés)
# add_command ajoute une ligne cliquable. command=... : la fonction à lancer (SANS parenthèses)
file_menu.add_command(label="Restart", font=("Arial", 15, "bold"), command=restart)
file_menu.add_command(label="Quit", font=("Arial", 15, "bold"), command=window.quit)
# add_cascade accroche la liste à la barre, sous le nom "setting"
menu_bar.add_cascade(label="setting", menu=file_menu, font=("Arial", 25, "bold"))
window.config(menu=menu_bar)                             # installe la barre sur la fenêtre

# ---------------------------------------------------------
# 8. LANCEMENT
# ---------------------------------------------------------
# Garde la fenêtre ouverte et attend les clics. Elle doit toujours être en DERNIER.
window.mainloop()