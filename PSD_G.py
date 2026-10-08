from tkinter import *

window = Tk()
window.title("Password Generator")
window.geometry("720x480")
window.config(background="#40565A")
window.iconbitmap(r"c:\Users\EL-ITKAN\Downloads\password_generator.ico")
logo = PhotoImage(file=r"c:\Users\EL-ITKAN\Downloads\logo_cadenas_noir.png").subsample(4)
Label(window, image=logo, background="#40565A").pack()
window.mainloop()