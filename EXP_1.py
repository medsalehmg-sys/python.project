# ==================================================
# 1. IMPORTER LES OUTILS
# ==================================================

from random import randint, choice
# randint()  → choisit un nombre entier aléatoire
# choice()   → choisit un élément aléatoire

from tkinter import *
# On importe les outils de Tkinter
# Tkinter sert à créer une interface graphique.

import string
# La bibliothèque string contient des lettres, chiffres,
# symboles, etc.


# ==================================================
# 2. CRÉER LA FONCTION QUI GÉNÈRE LE MOT DE PASSE
# ==================================================

def generate_password():
    # def = définir une fonction
    # generate_password = nom de notre fonction
    #
    # Cette fonction sera exécutée lorsqu'on clique
    # sur le bouton "Generate".

    password_min = 6
    # Longueur minimale du mot de passe = 6 caractères

    password_max = 12
    # Longueur maximale = 12 caractères

    all_chrcs = string.ascii_letters + string.punctuation + string.digits
    # On crée une grande chaîne contenant :
    #
    # ascii_letters → lettres A-Z et a-z
    # punctuation   → ! @ # $ % ...
    # digits        → 0 1 2 3 4 ...
    #
    # Exemple :
    # A B C ... z ! @ # ... 0 1 2 ...
    #
    # Tout est stocké dans la variable "all_chrcs"


    password = "".join(
        choice(all_chrcs)
        for x in range(randint(password_min, password_max))
    )

    # C'est la partie la plus difficile.
    #
    # randint(6, 12)
    # → choisit une longueur aléatoire
    #   par exemple : 8
    #
    # range(8)
    # → donne :
    #   0 1 2 3 4 5 6 7
    #
    # Donc on répète l'opération 8 fois.
    #
    # choice(all_chrcs)
    # → choisit un caractère au hasard.
    #
    # Exemple :
    # A
    # 7
    # @
    # k
    # 2
    # #
    # P
    # 9
    #
    # "".join(...)
    # → rassemble tous ces caractères.
    #
    # Résultat :
    # A7@k2#P9


    password_entry.delete(0, END)
    # On efface ce qui se trouve actuellement
    # dans la zone de texte.


    password_entry.insert(0)