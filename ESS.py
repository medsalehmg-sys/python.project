# dictionary concept :
# we import json
import json
# we create students dictionary:

students={
    "paul":{"rate":12,"appreciation":"good Work "},
    "camille":{
        "rate":7
        ,"appreciation":"bad Work"
    },
    "theo":{
       "rate": 17,
       "appreciation":"Excellent work"
           }
}
# we print the appreciation of paul :
print(students["paul"]["appreciation"])
    #add student :
students["leo"]={
    "rate":11,
    "appreciation":"acceptable"
}
# modification of an element :
students["camille"]["rate"]=10
students["camille"]["appreciation"]="acceptable"
# we print the appreciation of camille :
print(students["camille"]["appreciation"])
# we print the rate and appreciation of all students :
for student in students:
 print(students[student]["rate"],students[student]["appreciation"])
 # we save the students dictionary in a json file :
 with open("classe.json","w+") as file:
  json.dump(students,file)
  #.dump() function is used to write the data to the file in JSON format.


