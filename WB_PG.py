# interface concept
#programme number 1 a simple web site :
from tkinter import * #  the first step to create a window we import from tkinter 
import webbrowser # we import webbrowser
def open_web_channel():
    webbrowser.open_new("http://www.youtube.com/@eng-Medsaleh") # we create open_web_channel() function
# we create a window :
window=Tk()
# we give a tittle for the window
window.title("My Application ")
#we create an icon for window : use iconbitmap(r"files.ico")
window.iconbitmap(r"c:\Users\HP\Downloads\engineering_app_logo.ico")
# configuration : | color :
window.config(background="#0B1F3A")
# we give a charcteristcs for this window
# dimension for the window
window.geometry("720x480")
# mini-size:
window.minsize(420,360)
# we create a frame
frame=Frame(window,background="#0B1F3A")
# we add a first text :
label_tittle=Label(frame,text="Welcome to my web ",font=("latex",40),fg="white",bg="#0B1F3A")
label_tittle.pack()
# we add a second text :
label_subtittle=Label(frame,text="Hello every one it's Mohamed saleh  ",font=("latex",25),fg="white",bg="#0B1F3A")
label_subtittle.pack()
# we add a button :
yt_boutton=Button(frame,text="Open Youtube ",font=("latex",25),bg="white",fg="#0B1F3A",command=open_web_channel)
yt_boutton.pack(pady=25,fill=X)
frame.pack(expand=YES)
# we print this window :
window.mainloop()