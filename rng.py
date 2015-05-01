#simple GUI

from Tkinter import *


##Functions on calling actions from the menu
#file_menu
def file_hello():
	print "Hello World!"
	
def file_new():
	print "New Map"
	
def file_open():
	print "Open Map"
	
def file_save():
	print "Save"
	
def file_save_as():
	print "Save As"
	
#edit_menu
def edit_undo():
	print "Undo"
	
def edit_redo():
	print "Redo"


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
file_menu.add_command(label="Hello", command=file_hello)
file_menu.add_command(label="New...", command=file_new)
file_menu.add_separator()
file_menu.add_command(label="Open", command=file_open)
file_menu.add_separator()
file_menu.add_command(label="Save", command=file_save)
file_menu.add_command(label="Save as...", command=file_save_as)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
#edit_menu
edit_menu.add_command(label="Undo", command=edit_undo)
edit_menu.add_command(label="Redo", command=edit_redo)
edit_menu.add_separator()
##End of commands



##Modify root window
root.title("Roguelike 'Next-Level' Generator")
root.geometry("640x480")


## Display menubar and Start event loop
root.config(menu=menubar)
root.mainloop()