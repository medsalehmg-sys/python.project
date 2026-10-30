
# we create an menu :
class Menu():
 menu_bar=Menu(window)
 file_menu=Menu(menu_bar,tearoff=0)
 file_menu.add_command(label="new",command=window.restart)
 file_menu.add_command(label="exit",command=window.quit)
 menu_bar.add_cascade(label="file",menu=file_menu)