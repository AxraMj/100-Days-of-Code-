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
windows.config(padx=100,pady=50,bg=GREEN)

#displaying image we need photoimage class for image path and canvas class for displaying
canvas= Canvas(width=200,height=224,bg=GREEN,highlightthickness=0)
photo_path=PhotoImage(file="E:/100 Days Python/100-Days-of-Code-/Day28/002 pomodoro-start/tomato.png")
canvas.create_image(100,112,image=photo_path)

#adding text in picture
canvas.create_text(100,130,text="00:00" , fill="white", font=(FONT_NAME,35,"bold"))
canvas.pack()
windows.mainloop()