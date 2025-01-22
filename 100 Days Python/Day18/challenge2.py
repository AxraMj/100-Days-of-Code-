from turtle import *

timmy_the_turtle=Turtle()


timmy_the_turtle.color("khaki4")
def triangle():
    timmy_the_turtle.right(120)
    timmy_the_turtle.forward(75)
    timmy_the_turtle.color("green")
def square():
    timmy_the_turtle.right(90)
    timmy_the_turtle.forward(75)
    timmy_the_turtle.color("blue")
def pentagon():
    timmy_the_turtle.right(72)
    timmy_the_turtle.forward(75)
    timmy_the_turtle.color("yellow")
def hexagon():
    timmy_the_turtle.right(60)
    timmy_the_turtle.forward(75)
    timmy_the_turtle.color("orange")
def heptagon():
    timmy_the_turtle.right(51)
    timmy_the_turtle.forward(75)
    timmy_the_turtle.color("black")
def octagon():
    timmy_the_turtle.right(40)
    timmy_the_turtle.forward(75)

for _ in range(3):
    triangle()
for _ in range(4):
    square()
for _ in range(5):
    pentagon()
for _ in range(6):
    hexagon()
for _ in range(7):
    heptagon()
for _ in range(9):
    octagon()

screen=Screen()
screen.exitonclick()