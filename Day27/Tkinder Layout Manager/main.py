#Tkinder layout managers
#pack-The pack() method is much simpler to use for organizing widgets, especially if you simply want Tkinter to figure out exactly where the widget in your GUI should be.
#place-place, allows you to organize widgets by specifying both the position and size of each widget relative to other widgets. 
#grid-The grid method organizes widgets in a 2-dimensional table-like structure (think of an Excel spreadsheet), where each cell can hold a widget.

from tkinter import *

window = Tk()
window.title("My first TRinder Program")
window.minsize(width=500,height=300)

my_label=Label(text="Enter your name")
# my_label.pack(side="left") #only on particular side we can palce text
# my_label.place(x=100,y=200) #on any x,y axis we can place text
my_label.grid(column=0,row=0)
window.mainloop()