from turtle import *
import random
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
def random_direction(): 
    random_angle = random.choice([0, 10, 180, 270])
    tim.setheading(random_angle)

screen.onkey(move_forward, "Up")  # Changed "up" to "Up"
screen.onkey(move_backward, "Down")
screen.onkey(move_backward, "Down")
screen.onkey(to_turn_left, "Left")
screen.onkey(to_turn_right, "Right")
screen.onkey(random_direction, "r")
screen.listen()
screen.exitonclick()
