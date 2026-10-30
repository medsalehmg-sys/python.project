# project 1: Version 1:
# creation of an window :
from tkinter import *
# creation of window :
window = Tk()
# we add an title "":
window.title("XO game")
window.geometry("800x600")
window.config(background="black")
window.minsize(400,300)
window.maxsize(1200,900)
# we add an r"logo.ico":
window.iconbitmap(r"c:\Users\EL-ITKAN\Downloads\logo_xo.ico")
# creation of a frame :
frame = Frame(window,background="black")
frame.pack() # collage de la frame 
general_title=Label(frame,text=" Welcome to XO game",font=("Arial",30,"bold"),background="black",foreground="white")
general_title.pack(pady=10,padx=20)
# creation of buttons :
frame_2=Frame(window,background="purple")
frame_2.pack()
# creation of clic() function :
# creation of tour variable :
tour = "X"
combinaisons = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),   # les 3 lignes
    (0, 3, 6), (1, 4, 7), (2, 5, 8),   # # colonnes
    (0, 4, 8), (2, 4, 6)   
     ]     # # 2 diagonales
# creation of restart function :
def restart():
    global tour
    tour = "X"
    general_title.config(text=" Welcome to XO game")
    for b in casier:
        b.config(text="")

def verification_victory():
    for x, y, z in combinaisons:
        t1 = casier[x].cget("text")
        t2 = casier[y].cget("text")
        t3 = casier[z].cget("text")
        if t1 != "" and t1 == t2 == t3:
            general_title.config(text="Le joueur " + t1 + " a gagné !")
# creation of cli() function :
def clic(b):                     
    global tour                
    if b.cget("text") == "":      
        b.config(text=tour)      
        if tour == "X":           
            tour = "O"           
        else:                      
            tour = "X"      
    verification_victory()
    
    # we use the for boucle :
casier = []
for i in range(3): # here i={0,1,2}
    for j in range(3): # here j={0,1,2}
        bouton = Button(frame_2, text="", font=("Arial",35,"bold"), fg="red")
        bouton.grid(row=i, column=j)
        bouton.config(command=lambda b=bouton: clic(b))
        casier.append(bouton) 
menu_bar = Menu(window)
file_menu = Menu(menu_bar, tearoff=0,font=("Arial",15,"bold"))
file_menu.add_command(label="Restart",font=("Arial",15,"bold"),command=restart)
file_menu.add_command(label="Quit",font=("Arial",15,"bold"),command=window.quit)
menu_bar.add_cascade(label="setting", menu=file_menu,font=("Arial",25,"bold"))
window.config(menu=menu_bar)


    
            
        
        
    

    

window.mainloop()
