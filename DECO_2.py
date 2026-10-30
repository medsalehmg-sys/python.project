# decorator concept :
# Code 2:
def creation_file(rule):
    if rule=="admin":
        print("file created ")
    else :
        print("you don't have a permission") # <<<<<<---- REPETION }
# Code 2:                                                          }
def Edit_file(rule):                                                
    if rule=="admin":
        print("file Edited ")            # {SO HERE WE NEED TO USE DECORATOR 
    else :                                   ##################                  
        print("you don't have a permission")# <<<<<<---- REPETION

def Del_file(rule):
    if rule=="admin":                       ###########################
        print("file Delited ")
    else :                                    ##############################
        print("you don't have a permission")  # <<<<<<---- REPETION }
creation_file("user")
Edit_file("user")
Del_file("admin")
    



    