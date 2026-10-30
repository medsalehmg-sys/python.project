# Decorator Concept :
# code 3:                   # version 1 :
# we import time :
import time   

# creation of an decorator :
def decorator(func):
    def wrapper():
        time.sleep(1)
        func()
    return wrapper

# creation of functions :
@decorator
def  command():
    print("Good morning ")
@decorator   
def other_command():
    print("How are you doing ")
@decorator
def another_command():
    print("Aweosome !")

command()            # functions call 
other_command()
another_command()



