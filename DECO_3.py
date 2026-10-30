# Decorator Concept :
# code 3:
# we import time :
import time
# creation of functions :
def  command():
    time.sleep(4) #####<<<<<< 1s \REPETION
    print("Good morning ")
def other_command():
    time.sleep(1) ##### REPETION
    print("How are you doing ")
def another_command():
    time.sleep(1)  ##### REPETION 
    print("Aweosome !")

command()            # functions call 
other_command()
another_command()



