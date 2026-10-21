# we create an dictionary :'
students={
    "paul":12,
    "camille":7
    ,"theo":17
}
for student in students.values():
    print(student)
    # we print the classerom average:
print("the Average is :",sum(students.values())/len(students))
