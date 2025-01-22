from tkinter import *

window = Tk()
window.title("My first TRinder Program")
window.minsize(width=500,height=300)
window.config(padx=20,pady=20)

my_label=Label(text="Label")
my_label.grid(column=0,row=0)

my_button= Button(text="Button")
my_button.grid(column=2,row=0)

my_button2= Button(text="Button2")
my_button2.grid(column=1,row=1)

my_entry=Entry()
my_entry.grid(column=3,row=2)

window.mainloop()