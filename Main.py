from tkinter import *
from tkinter import ttk

from Graphics import GraphicsConstructor

class AppConstructor(GraphicsConstructor):
    def __init__(self, window = 'window'):
        GraphicsConstructor.__init__(self, window)

window= Tk()
window.title('Welcome to the EDA GUI app!')
start= AppConstructor (window)
menubar = Menu(window)
filemenu = Menu(menubar, tearoff = 0)
filemenu.add_command(label="Load File", command = start._load_file_action)
filemenu.add_command(label = "Save File", command = start._save_file_action)
filemenu.add_command(label = "Save File as...", command = start._save_file_as_action)

columnmenu = Menu(menubar, tearoff = 0)
columnmenu.add_command(label="Save Column", command = start._save_column_action)
columnmenu.add_command(label="Save Column as...", command = start._save_column_as_action)


menubar.add_cascade(label = "File", menu = filemenu)
menubar.add_cascade(label = "Column Options", menu = columnmenu)
window.config(menu = menubar)
window.mainloop()
