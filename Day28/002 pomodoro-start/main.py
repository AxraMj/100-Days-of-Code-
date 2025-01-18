from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

windows =Tk()
windows.title("Pomodoro")
windows.minsize(width=500,height=300)

#displaying image we need photoimage class for image path and canvas class for displaying
canvas= Canvas(width=200,height=224)
image_path="E:/100 Days Python/100-Days-of-Code-/Day28/002 pomodoro-start/tomato.png"
photo_path=PhotoImage(file=image_path)
canvas.create_image(100,112,image=photo_path)
canvas.pack()
windows.mainloop()