#we import tkinter :
from tkinter import*
# we import webbrowser:
import webbrowser
# creation of function yt_button():
def yt_button():
    webbrowser.open(r"http://www.youtube.com/@eng-Medsaleh")
# creation of window :
window=Tk()
window.title("My Application")
window.config(background="black")
window.geometry("1080x720")
window.minsize(720,480)
window.iconbitmap(r"c:\Users\HP\Downloads\engineering_app_logo.ico")
window.maxsize(1080,720)
frame=Frame(window,background="black")
button_yt=Button(frame,background="black",font=("latex",25),command=yt_button,fg="white")
button_yt.pack(pady=25,fill=X)
label_tittle=Label(frame,text="welcome to my we site ",font=("latex",40),fg="white")
label_tittle.pack()
label_subtittle=Label(frame,text="Hello every one it's Mohamed saleh  ",font=("latex",20),fg="white"
)
label_subtittle.pack()
frame.pack(expand=YES)
window.mainloop()