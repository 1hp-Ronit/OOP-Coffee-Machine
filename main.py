# For drawing
from turtle import Turtle, Screen

timmy = Turtle()  # Turtle class
# print(timmy)
timmy.shape("turtle")  # shape is a method of the class Turtle
timmy.color("#cdac83")  # color is a method of the class Turtle

my_screen = Screen()  # my_screen is an object of the class -> Screen
print(my_screen.canvheight)  # canvheight is an attribute of the Screen class
# Moves
timmy.forward(100)
my_screen.exitonclick()  # exitonclick is a method of class -> Screen