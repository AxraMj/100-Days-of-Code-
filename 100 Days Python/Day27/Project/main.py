from tkinter import *

def mile_converter():
    miles=float(miles_entry.get())
    km=miles*1.609
    answer_label.config(text=f"{km}")

window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=350,height=200)

#entry
miles_entry = Entry(width=10)
miles_entry.grid(column=1,row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2,row=0)

is_equal_to_label=Label(text="is qual to")
is_equal_to_label.grid(column=0,row=1)

answer_label=Label(text="0")
answer_label.grid(column=1,row=1)

Km_label=Label(text="Km")
Km_label.grid(column=2,row=1)

calculate_button=Button(text="Calculate",command=mile_converter)
calculate_button.grid(column=1,row=2)

window.mainloop()