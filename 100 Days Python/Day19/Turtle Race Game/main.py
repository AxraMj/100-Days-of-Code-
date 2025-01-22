from turtle import *
import random
screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Lets Bet",prompt="Who will win the Race?Guess Color")
is_game_on=False
color = ["red","green","blue","yellow","orange","purple"]
y_position = [-70,-40,-10,20,50,80]
all_turtles=[]

for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230,y=y_position[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_game_on=True

while is_game_on:
    for turtle in all_turtles:
        if turtle.xcor()>230:
            is_game_on=False
            Warning_color= turtle.pencolor()
            if Warning_color==user_bet:
                print(f"You won!! The {Warning_color} turtle is the Winner!!!")
            else:
                print(f"ohh You lost!! The {Warning_color} turtle is the Winner!!!")
        random_dis=random.randint(0,10)
        turtle.forward(random_dis)

screen.exitonclick()