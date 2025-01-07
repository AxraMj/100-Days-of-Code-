from turtle import *

tim = Turtle()
screen = Screen()
def to_turn_left():
    tim.left(90)
def to_turn_right():
    tim.right(90)
def move_forward():
    tim.forward(100)
def move_backward():
    tim.backward(100)

screen.onkey(move_forward, "Up")  # Changed "up" to "Up"
screen.onkey(move_forward, "W")
screen.onkey(move_backward, "Down")
screen.onkey(move_backward, "Down")
screen.onkey(to_turn_left, "Left")
screen.onkey(to_turn_right, "Right")
screen.listen()
screen.exitonclick()
