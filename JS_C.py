# we import Json :'
# is an subject used to convert a dictionary to json format and save a Data :
import json
 # creation of an big dictionary formed by dictionary "
students={
    "paul":{
        "rate":12,
        "appreciation":"good"
    },
    "camille":{
        "rate":17
        ,"appreciation":"excellent"
    },
    "theo":{
        "rate":8
        ,"appreciation":"Bad"
    }
}
# we print student appreciation :
print(students["camille"]["appreciation"])
# we add an element :
students={"Romaissa":{
    "rate":18
    ,"appreciation":
    "Excelent"
}
}
# we edited an Element :
students["paul"]["rate"]=10
students["paul"]["appreciation"]=" Acceptable"
# .items give key+element :
 #info = his samallest dictionary {"rate": ..., "appreciation": ...}
for name,info in students.items:
    print(info["rate"],info["appreciation"])
    # ÉTAPE 7 : sauvegarder dans un fichier
# open("classe.json", "w") : open the file in reading mode
#   (it's create if it's doesn't exist , écrasé s'il existe).
# with ... as file :    close the file automatically
#  json.dump(...) :  write the file in json file 
# indent=4 : rend le fichier lisible (retours à la ligne + espaces)
with open("class.json","w") as file :
    json.dump(students,file,indent=4)


