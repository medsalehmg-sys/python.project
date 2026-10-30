# Decorator Concept :
# code 3:                   # version 1 :
# we import time :
import time   

# creation of an decorator :
def add_time(delay):   # delay=1 default value          # creation of decorator in decorator :
    def decorator(func):
      def wrapper():
        time.sleep(delay)
        func()  # func call 
      return wrapper   # return wrapper 
    return decorator   # return decorator 

# creation of functions :
@add_time(delay=1)   # we use the decorator add_time :
def  command():
    print("Good morning ")           # with delay=t
@add_time(delay=2)  
def other_command():
    print("How are you doing ")
@add_time(delay=3)
def another_command():
    print("Aweosome !")

command()            # functions call 
other_command()
another_command()



