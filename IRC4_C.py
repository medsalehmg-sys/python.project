
# Code :
from random import randint,choice
from tkinter import*
import string
def generate_password():
    password_min=6
    password_max=12
    all_chrcs=string.ascii_letters+string.punctuation+string.digits
    password= "".join(choice(all_chrcs) for x in range(randint(password_min,password_max)))
    password_entry.delete(0,END)
    password_entry.insert(0,password)
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
canvas.grid(row=0,column=0,sticky=W) # sticky -----> picture position {}
# creation of sub_bottle :
right_frame=Frame(frame,bg="gray") # creation of Right_frame in frame 

# creation of tittle + add text : in right_frame :
label_title=Label(right_frame,text="password",background="black",fg="white",font=("Latex",30))
label_title.pack()
# creation a Field\ Enter | input the pasword or  text:
password_entry=Entry(right_frame,background="black",fg="white",font=("Latex",30))
password_entry.pack()
#creation of generate_password_button :
generate_password_button=Button(right_frame,text="Generate",background="black",fg="white",font=("Latex",30),command=generate_password)
generate_password_button.pack(fill=X)
# gris : on right_frame \ on place la sous boite{sub_bottle} right the principal frame 
right_frame.grid(row=0,column=1,sticky=W)

frame.pack(expand=YES) # center the frame 
# creation of menu_bar:
# we o\pen the window :
menu_bar=Menu(window)
file_menu=Menu(menu_bar,tearoff=0)
file_menu.add_command(label="new",command=generate_password)
file_menu.add_command(label="exit",command=window.quit)
menu_bar.add_cascade(label="File",menu=file_menu)
window.config(menu=menu_bar)
window.mainloop()