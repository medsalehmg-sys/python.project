# ============================================================
# ÉTAPE 1 : importer le module json
# json est un module intégré à Python : il permet de convertir
# un dictionnaire en texte JSON (et inversement) pour le
# sauvegarder dans un fichier.
# ============================================================
import json

# ============================================================
# ÉTAPE 2 : créer le dictionnaire students
# C'est un dictionnaire de dictionnaires :
#   - clé extérieure  = le nom de l'étudiant ("paul", ...)
#   - valeur          = un petit dictionnaire avec 2 clés :
#                       "rate" (la note) et "appreciation" (le commentaire)
# ============================================================
students = {
    "paul": {"rate": 12, "appreciation": "good Work"},
    "camille": {"rate": 7, "appreciation": "bad Work"},
    "theo": {"rate": 17, "appreciation": "Excellent work"},
}

# ============================================================
# ÉTAPE 3 : lire une valeur
# On accède en deux temps :
#   students["paul"]                   -> {"rate": 12, "appreciation": "good Work"}
#   students["paul"]["appreciation"]   -> "good Work"
# Affiche : good Work
# ============================================================
print(students["paul"]["appreciation"])

# ============================================================
# ÉTAPE 4 : ajouter un nouvel étudiant
# La clé "leo" n'existe pas encore, donc Python la crée.
# Le dictionnaire contient maintenant 4 étudiants.
# ============================================================
students["leo"] = {"rate": 11, "appreciation": "acceptable"}

# ============================================================
# ÉTAPE 5 : modifier des éléments existants
# La clé "camille" existe déjà : Python remplace l'ancienne valeur.
# (même syntaxe que pour ajouter : dictionnaire[clé] = valeur)
# ============================================================
students["camille"]["rate"] = 10                    # 7 devient 10
students["camille"]["appreciation"] = "acceptable"  # "bad Work" devient "acceptable"

# ============================================================
# ÉTAPE 6 : parcourir le dictionnaire et afficher
# .items() donne des paires (clé, valeur) :
#   name = le nom de l'étudiant ("paul", "camille", ...)
#   info = son petit dictionnaire {"rate": ..., "appreciation": ...}
# La boucle s'exécute une fois par étudiant (4 fois ici).
# ============================================================
for name, info in students.items():
    print(info["rate"], info["appreciation"])

# ============================================================
# ÉTAPE 7 : sauvegarder dans un fichier
# open("classe.json", "w") : ouvre le fichier en écriture
#   (il est créé s'il n'existe pas, écrasé s'il existe).
# with ... as file : ferme automatiquement le fichier à la fin.
# json.dump(...) : écrit le dictionnaire dans le fichier en JSON.
# indent=4 : rend le fichier lisible (retours à la ligne + espaces).
# Cette étape est HORS de la boucle : le fichier est écrit une seule fois.
# ============================================================
with open("classe.json", "w") as file:
    json.dump(students, file, indent=4)

# ============================================================
# BONUS : relire le fichier plus tard
# json.load fait l'inverse de json.dump : il lit le fichier
# et reconstruit le dictionnaire Python.
# ============================================================
# with open("classe.json", "r") as file:
#     students = json.load(file)