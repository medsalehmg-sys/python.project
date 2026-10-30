# file Concept :
# we import os :
# algorithme : os-->(exist-->> creation of images --->> copy--->>> succesful) or\os--->>(print("failed"))
import os 
# we import copy  from m shutil :
from shutil import copy
# creation of source Variables :
source=r"logo_cadenas_noir.png"
# we used the condion if :
if os.path.exists(source):
    os.makedirs("images",exist_ok=True) # creation of file "image" if it doesn't exist : with markedirs
# creation of targret Variable 
    target=r"images/logo_cadenas_noir.png" 
# we copy the file with copy function :
    copy(source,target)
    print(" copy succesful ! ")
else:
    print("Operation failed ")
