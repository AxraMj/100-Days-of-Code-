from turtle import *

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(100)

screen.onkey(move_forward, "Up")  # Changed "up" to "Up"
screen.listen()
screen.exitonclick()
