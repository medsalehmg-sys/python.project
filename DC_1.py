# Decorator concept :
# Code1:
# creation of decorateur :
def decorateur(func): # a decorateur is defined by function in function \
    def wrapper():  # creation wrapperr function in decorator 
        print("Before")
        func()  # function call
        print("After")
    return wrapper # return wrapper same level with def 
# How to use the decorator : @decorateur  
@decorateur
def say_hello():
    print("Hello Every one ! ")
# function call :
say_hello()
    
