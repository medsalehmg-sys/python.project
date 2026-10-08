# ============================================================
# 1. IMPORTER LES OUTILS
# ============================================================

from random import randint, choice
# randint() : choisit un nombre entier aléatoire
# choice()  : choisit un élément aléatoire dans une collection

from tkinter import *
# tkinter permet de créer une interface graphique :
# fenêtre, bouton, texte, zone de saisie...
import string
# string contient des groupes de caractères déjà prêts :
# lettres, chiffres, symboles...


# ============================================================
# 2. FONCTION POUR GÉNÉRER LE PASSWORD
# ============================================================

def generate_password():
    # Cette fonction sera exécutée quand on clique sur "Generate"

    password_min = 6
    # Longueur minimale du password = 6 caractères

    password_max = 12
    # Longueur maximale du password = 12 caractères


    all_chrcs = string.ascii_letters + string.punctuation + string.digits
    # On crée une collection contenant :
    #
    # ascii_letters  → a b c ... z A B C ... Z
    # punctuation    → ! " # $ % & ...
    # digits         → 0 1 2 3 4 5 6 7 8 9
    #
    # Le + permet d'assembler ces trois groupes.


    password = "".join(
        choice(all_chrcs)
        for x in range(randint(password_min, password_max))
    )

    # Regardons cette partie doucement :
    #
    # randint(6, 12)
    # → choisit un nombre entre 6 et 12
    # → par exemple : 8
    #
    # range(8)
    # → permet de répéter l'opération 8 fois
    #
    # choice(all_chrcs)
    # → choisit UN caractère au hasard
    # → par exemple : A
    #
    # Puis on recommence :
    # A → 7 → @ → k → P → 2 → ! → x
    #
    # "".join(...)
    # → assemble tous les caractères
    #
    # Résultat :
    # A7@kP2!x


    password_entry.delete(0, END)
    # Supprime l'ancien password dans la zone Entry
    #
    # 0   → commencer au début
    # END → jusqu'à la fin


    password_entry.insert(0, password)
    # Insère le nouveau password dans la zone Entry
    #
    # 0        → position de départ
    # password → le nouveau password


# ============================================================
# 3. CRÉER LA FENÊTRE
# ============================================================

window = Tk()
# Crée la fenêtre principale de notre programme


window.title("Password Generator")
# Donne le titre "Password Generator" à la fenêtre


window.geometry("720x480")
# Définit la taille de la fenêtre :
# largeur = 720 pixels
# hauteur = 480 pixels


window.config(background="gray")
# Définit la couleur de fond de la fenêtre : gris


# ============================================================
# 4. CRÉER UN FRAME
# ============================================================

frame = Frame(window, background="gray")
# Un Frame est comme une boîte dans la fenêtre.
# Il permet d'organiser les différents éléments.


# ============================================================
# 5. CRÉER LA ZONE POUR L'IMAGE
# ============================================================

width = 300
height = 300
# Dimensions du Canvas


image = PhotoImage(
    file=r"c:\Users\EL-ITKAN\Downloads\logo_cadenas_noir.png"
).subsample(3)

# PhotoImage charge l'image depuis l'ordinateur.
# subsample(3) réduit la taille de l'image.


canvas = Canvas(
    frame,
    width=width,
    height=height,
    background="gray",
    bd=0,
    highlightthickness=0
)

# Canvas crée une zone graphique.
# On pourra mettre l'image à l'intérieur.


canvas.create_image(
    width / 2,
    height / 2,
    image=image
)

# Place l'image au centre du Canvas.
#
# width / 2  → milieu horizontal
# height / 2 → milieu vertical


canvas.grid(row=0, column=0, sticky=W)
# Place le Canvas dans la grille.
#
# row=0    → ligne 0
# column=0 → colonne 0
# sticky=W → place l'élément vers la gauche


# ============================================================
# 6. CRÉER LA PARTIE DROITE
# ============================================================
right_frame = Frame(frame, bg="gray")
# Crée une deuxième boîte pour mettre :
# le titre, la zone du password et le bouton.


# ============================================================
# 7. TITRE "PASSWORD"
# ============================================================

label_title = Label(
    right_frame,
    text="Password",
    background="black",
    fg="white",
    font=("Latex", 30)
)

# Label permet d'afficher du texte.
#
# text="Password" → texte affiché
# background      → couleur du fond
# fg              → couleur du texte
# font            → police et taille


label_title.pack()
# Place le Label dans right_frame.


# ============================================================
# 8. ZONE POUR AFFICHER LE PASSWORD
# ============================================================

password_entry = Entry(
    right_frame,
    background="black",
    fg="white",
    font=("Latex", 30)
)

# Entry crée une zone de texte.
# C'est ici que le password sera affiché.


password_entry.pack()
# Place la zone Entry dans right_frame.


# ============================================================
# 9. BOUTON GENERATE
# ============================================================

generate_password_button = Button(
    right_frame,
    text="Generate",
    background="black",
    fg="white",
    font=("Latex", 30),
    command=generate_password
)

# Button crée un bouton.
#
# text="Generate" → texte du bouton
#
# command=generate_password
# → quand l'utilisateur clique sur le bouton,
#   Python exécute la fonction generate_password()


generate_password_button.pack(fill=X)
# Place le bouton.
#
# fill=X → le bouton prend toute la largeur disponible.


# ============================================================
# 10. PLACER LA PARTIE DROITE
# ============================================================

right_frame.grid(row=0, column=1, sticky=W)

# On place right_frame à droite du Canvas.
#
# column=0 → image
# column=1 → partie droite


# ============================================================
# 11. AFFICHER LE FRAME PRINCIPAL
# ============================================================

frame.pack(expand=YES)

# Place le Frame dans la fenêtre.
# expand=YES permet au Frame d'utiliser l'espace disponible.


# ============================================================
# 12. CRÉER LA BARRE DE MENU
# ============================================================

menu_bar = Menu(window)
# Crée la barre de menu principale.


file_menu = Menu(menu_bar, tearoff=0)
# Crée un menu appelé "File".


file_menu.add_command(
    label="New",
    command=generate_password
)

# Ajoute "New" dans le menu.
#
# Si on clique sur "New",
# la fonction generate_password() est exécutée.


file_menu.add_command(
    label="Exit",
    command=window.quit
)

# Ajoute "Exit".
#
# Si on clique sur "Exit",
# window.quit ferme la fenêtre.


menu_bar.add_cascade(
    label="File",
    menu=file_menu
)

# Ajoute le menu "File" dans la barre principale.


window.config(menu=menu_bar)
# Dit à la fenêtre d'utiliser notre barre de menu.


# ============================================================
# 13. GARDER LA FENÊTRE OUVERTE
# ============================================================

window.mainloop()

# mainloop() garde la fenêtre ouverte
# et attend les actions de l'utilisateur :
#
# clic sur Generate
# clic sur New
# clic sur Exit
# etc.