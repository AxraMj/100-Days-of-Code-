from turtle import Turtle, Screen

timmy=Turtle() #timmy is object #Turtle is class
print(timmy)
timmy.shape("turtle")
timmy.color("coral")
timmy.forward(100)
timmy.left(100)
timmy.forward(100)
timmy.left(100)
timmy.forward(100)

my_screen=Screen() #my_screen is object and Screen() is class
print(my_screen.canvheight) #my_screen is object and canvheight attribute
my_screen.exitonclick() #exitonclick is method
