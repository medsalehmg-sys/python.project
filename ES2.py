# We import os \ copy function from shutil:
import os 
from shutil import copy
# we create source Variable :
source=r"logo_cadenas_noir.png"
# we used the condition if\else :
if os.path.exists(source):
    os.makedirs("images",exist_ok=True)
    # creation of images file 
    # we create target variable:
    target=r"images\logo_cadenas_noir.png"
    copy(source,target)
    # we copy source\target 
    print(" copy successful")
else:
    print(" the source  file doesn't exist")
