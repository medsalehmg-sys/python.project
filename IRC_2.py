# Code :
from tkinter import*
# creation of the window
window=Tk()
# we add a tittle for the window :
window.title("password Generator ")
# we add a Dimension for the Window :
window.geometry("720x480")
window.iconbitmap(r"c:\Users\EL-ITKAN\Downloads\password_generator.ico")
# We add an configuration for the window :
window.config(background="gray")
# creation of picture\image :
# Largeur :
width=300
height=300
image = PhotoImage(file=r"c:\Users\EL-ITKAN\Downloads\logo_cadenas_noir.png").subsample(3) 
# we create new Variable canvas :J
canvas=Canvas(window,width=width,height=height,background="gray",bd=0,highlightthickness=0)
canvas.create_image(width/2,height/2,image=image)
canvas.pack(expand=YES)
# we o\pen the window :
window.mainloop()