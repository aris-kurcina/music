from tkinter import filedialog
from tkinter import *

root = Tk()
root.withdraw()
folder_selected = filedialog.askdirectory()

print ("FOLDER is " + folder_selected)