from tkinter import *

windows = Tk()
windows.title("Registration form")
windows.minsize(width=500,height=300)

#label
my_label=Label(text="Registration Form")
my_label.pack()

#Entry
my_entry = Entry()
my_entry.insert(END,string="Enter your name")
my_entry.pack()

#Text
my_text=Text(width=20,height=5)
my_text.pack()

#spinBox
my_spinbox= Spinbox(from_=1, to=10)
my_spinbox.pack()

#scale
my_scale=Scale()
my_scale.pack()

#checkbox
my_checkbox=Checkbutton(text="male")
my_checkbox.pack()

#radiobutton
checked_state=IntVar()
my_radiobutton1 = Radiobutton(text="true",value=1,variable=checked_state,command=checked_state)
my_radiobutton2 = Radiobutton(text="false",value=2,variable=checked_state,command=checked_state)
my_radiobutton1.pack()
my_radiobutton2.pack()

#listbox
my_listbox=Listbox()
fruits=["apple","orange","graps"]
for item in fruits:
    my_listbox.insert(fruits.index(item),item)
my_listbox.pack()

#button
my_button =Button(text="Submit")
my_button.pack()
windows.mainloop()