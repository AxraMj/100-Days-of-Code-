from turtle import Turtle
ALIGNMENT="center"
FONT=("Arial",24,"normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.write(f"score:{self.score}",align=ALIGNMENT,font=FONT)
        self.hideturtle()
        self.updatescoreboard()
    
    def updatescoreboard(self):
        self.write(f"score:{self.score}",align=ALIGNMENT,font=FONT)

    def gameover(self):
        self.goto(0,0)
        self.write("Game over!!",align=ALIGNMENT,font=FONT)


    def increasescore(self):
        self.score+=1
        self.clear()
        self.updatescoreboard()        