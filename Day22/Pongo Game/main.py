from turtle import *

screen=Screen()
screen.bgcolor("black")

divider = Turtle()
divider.speed(0)  # Fast drawing
divider.hideturtle()
divider.pensize(2)  # Thickness of the border lines
divider.pencolor("white")  # Line color

divider.penup()
divider.goto(0, screen.window_height() // 2)  # Start at the top middle
divider.pendown()
divider.setheading(270)  # Point downwards
divider.forward(screen.window_height())  # Draw downward

screen.exitonclick()