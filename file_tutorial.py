# we import os and shutil:
import os
import shutil
# creation of variable source :

source="__pycache__/logo_cadenas_noir.png"
target="images\__pycache__/logo_cadenas_noir.png"
shutil.copy(source, target) # copy the file from source to target