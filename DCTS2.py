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
print(students["paul"]["appreciation"])
    #add student :
students["leo"]={
    "rate":11,
    "appreciation":"acceptable"
}
for student in students:
 print(students[student]["rate"],students[student]["appreciation"])
