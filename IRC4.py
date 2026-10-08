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
# we create a frame :
frame=Frame(window,background="gray") 
# creation of picture\image :
# Largeur :
width=300  
height=300 
image = PhotoImage(file=r"c:\Users\EL-ITKAN\Downloads\logo_cadenas_noir.png").subsample(3) 
# we create new Variable canvas :J
canvas=Canvas(frame,width=width,height=height,background="gray",bd=0,highlightthickness=0)
canvas.create_image(width/2,height/2,image=image)
canvas.grid(row=0,column=0,sticky=W)
# creation of tittle + add text :
label_title=Label(frame,text="password",background="black",fg="white",font=("Latex",30))
label_title.grid(row=0,column=1,sticky=W)
frame.pack(expand=YES)
# we o\pen the window :
window.mainloop()