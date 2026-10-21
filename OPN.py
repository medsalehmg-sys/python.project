# charger les donnes depuis le fichier :\load data from the file 
# we import json:

import json

# we use the function open() to open the file in read mode :
with open("classe.json","r") as file:
    students=json.load(file) # .load() function is used to load the data from the file and convert it into a Python dictionary.
    print(students)
    