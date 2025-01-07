from turtle import *
screen=Screen()
screen.setup(width=500,height=400)
screen.textinput(title="Lets Bet",prompt="Who will win the Race?Guess Color")

color=["red","green","blue","yellow","orange","purple"]
y_position=[-70,-40,-10,20,50,80]

for turtle_index in range(0,6):
    tim=Turtle(shape="turtle")
    tim.color(color[turtle_index])
    tim.penup()
    tim.goto(x=-230,y=y_position[turtle_index])

screen.exitonclick()