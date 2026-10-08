
# interface concept
from tkinter import * #  the first step to create a window
# we create a window :
window=Tk()
# we give a tittle for the window
window.title("My Application ")
#we create an icon for window : use iconbitmap(r"files.ico")
window.iconbitmap(r"c:\Users\HP\Downloads\engineering_app_logo.ico")
# configuration :
window.config(background="#0B1F3A")
# we give a charcteristcs for this window
# dimension for the window
window.geometry("720x480")
# mini-size:
window.minsize(420,360)
# we print this window :
window.mainloop()