from turtle import *
import time
screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black") 
screen.title("My Snake Game")
screen.tracer(0)

starting_posttion=[(0,0), (-20,0),(-40,0)]
segment=[]

for posstion in starting_posttion:
    new_segment=Turtle(shape="square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(posstion)
    segment.append(new_segment)

game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    for seg_num in range(len(segment)-1,0,-1):
        new_x=segment[seg_num-1].xcor()
        new_y=segment[seg_num-1].ycor()
        segment[seg_num].goto(new_x,new_y)
    
    segment[0].forward(20)
    segment[0].left(90)
    

        

screen.exitonclick()



# def snake_forward_move():
#     snake.forward(50)
# def snake_backward_move():
#     snake.backward(50)
# def snake_left_move():
#     snake.left(90)
# def snake_Right_move():
#     snake.right(90)

# screen.onkey(snake_forward_move, "Up") 
# screen.onkey(snake_backward_move, "Down") 
# screen.onkey(snake_left_move, "Left")
# screen.onkey(snake_Right_move, "Right") 