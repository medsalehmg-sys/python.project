
from random import randint,choice
from tkinter import*
import string
def generate_password():
    password_min = 6
    password_max = 12
    all_chrcs = string.ascii_letters + string.punctuation + string.digits
    
    password = "".join(
            choice(all_chrcs)
            for x in range(randint(password_min, password_max))
        )                                  
    password_entry.delete(0, END)       
    password_entry.insert(0, password)
window =Tk()
window.title("Password Generator")
window.geometry("720x480")
window.config(background="gray")
frame = Frame(window, background="gray")
width = 300
height = 300
image = PhotoImage(
    file=r"c:\Users\EL-ITKAN\Downloads\logo_cadenas_noir.png"
).subsample(3)
canvas = Canvas(
    frame,
    width=width,
    height=height,
    background="gray",
    bd=0,
    highlightthickness=0
)
canvas.create_image(
    width / 2,
    height / 2,
    image=image
)
canvas.grid(row=0, column=0, sticky=W)

right_frame = Frame(frame, bg="gray")
label_title = Label(
    right_frame,
    text="Password",
    background="black",
    fg="white",
    font=("Latex", 30)
)
label_title.pack()
password_entry = Entry(
    right_frame,
    background="black",
    fg="white",
    font=("Latex", 30)
)
password_entry.pack()
generate_password_button = Button(
    right_frame,
    text="Generate",
    background="black",
    fg="white",
    font=("Latex", 30),
    command=generate_password
)
generate_password_button.pack(fill=X)
right_frame.grid(row=0, column=1, sticky=W)
frame.pack(expand=YES)

menu_bar = Menu(window)          # 1. La barre en haut (vide)
file_menu = Menu(menu_bar, tearoff=0)   # 2. Une liste "File" (vide)

file_menu.add_command(label="New", command=generate_password)   # 3. Une ligne "New"
file_menu.add_command(label="Exit", command=window.quit)       # 3. Une ligne "Exit"

menu_bar.add_cascade(label="File", menu=file_menu)   # 4. On met la liste dans la barre
window.config(menu=menu_bar)                         # 5. On met la barre sur la fenêtre

