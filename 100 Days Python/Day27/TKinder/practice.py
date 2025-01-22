from tkinter import *

window = Tk()
window.title("My first TRinder Program")
#changing size
window.minsize(width=500,height=300)
#components inside window
#label
my_label=Label(text="Enter your name", font=("Arial",24,"bold"))
my_label.pack() #to display we need pack()
#label can also update like this
my_label["text"]="HI"
my_label.config(text="Welcome To Python",font=("Arial",18,"bold"))


#working button click on terminal
def clicked_me():
    print("I Got Clicked")
#buutton
#to get rid of tkinder.Button or any other class name , we can use * to import all class from tkinder module
my_button = Button(text="Click Me",command=clicked_me)
my_button.pack()


window.mainloop() #same as while loop,mainloop() is inbuilt in tkinter module(to open window continusly)