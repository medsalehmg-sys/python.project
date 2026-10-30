# decorator concept :
# Code 2:   
# Creation of an decorator is_admin :

def is_admin(func):
    def wrapper(rule): # rule  is an Variable in def wrapper() so you should to define it in def wrapper(rule)
        if rule=="admin":
            func()     # Here we use use the Condition if\else :
        else:
            print("you don't Have a permission ! ")
    return wrapper # return Wrapper verry importante step
    
        
@is_admin  # we use the decorator :
def creation_file():
    print("file created ")
# Code 2:
@is_admin     # Here we don't need to use the condition if \else :
def Edit_file():                                                
    print("file Edited ")            # SO HERE WE NEED TO USE DECORATOR #
@is_admin                                                               
def Del_file():
    print("file Delited ")                   
creation_file("user") # <<<<< the firts is an "User"
Edit_file("user") ####<<<<< the second is an "user"
Del_file("admin") #####<<<<<< the third is an "admin" ??? Have a permission >> YES
    



    