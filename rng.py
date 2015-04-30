#simple GUI

from Tkinter import *


def hello():
	print "Hello World!"


##Create the window and drop down menu
root = Tk()
menubar = Menu(root)

##List drop down menus to create cascade menus
file_menu = Menu(menubar)
edit_menu = Menu(menubar)
##Add the cascades to the menubar
menubar.add_cascade(label="File", menu = file_menu)
menubar.add_cascade(label="Edit", menu = edit_menu)

##Add commands to each cascade
#file_menu
file_menu.add_command(label="Hello", command=hello)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)


##Modify root window
root.title("Roguelike 'Next-Level' Generator")
root.geometry("640x480")


## Display menubar and Start event loop
root.config(menu=menubar)
root.mainloop()