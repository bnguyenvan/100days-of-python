from turtle import Turtle, Screen
import random
my_turtle = Turtle()
my_turtle.color("red")
# for _ in range(10):
#     my_turtle.forward(10)
#     my_turtle.penup()
#     my_turtle.forward(10)
#     my_turtle.pendown()
color = ["rosy brown","blue","salmon","red","thistle","green","orange red","rosy brown"]

def draw_shape(num_sides):
    angle = 360 / num_sides
    for j in range(num_sides):
        my_turtle.forward(50)
        my_turtle.right(angle)
for i in range(3, 11):
    my_turtle.color(random.choice(color))
    draw_shape(i)

my_screen = Screen()
my_screen.exitonclick()