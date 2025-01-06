import turtle as t
import random
tim=t.Turtle()
directions=[0,90,180,270]
tim.pensize(15)
tim.speed("fastest")
colours=["green","yellow","beige","bisque4","BlueViolet","burlywood4","coral2","cornsilk","crymson","DarkGoldenrod2","DarkOliveGreen4","DeepPink4","firebrick1","gray10"]
for _ in range(200):
    tim.color(random.choice(colours))
    tim.forward(30)
    tim.setheading(random.choice(directions))
