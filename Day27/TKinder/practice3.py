from tkinter import *

window = Tk()
window.title("Practice program")
window.minsize(width=500,height=300)

my_label=Label(text="Click me")
my_label.pack()

#Entry (to input something)
input_text= Entry()
input_text.pack()


def click_me():
    my_label["text"]=input_text.get()
    

my_button=Button(text="Click me", command=click_me)
my_button.pack()



window.mainloop()