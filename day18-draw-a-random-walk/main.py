from turtle import Turtle, Screen
import random


colors = ["rosy brown","blue","salmon","red","thistle","green","orange red","rosy brown"]
directions = ["left","right","forward","backward"]

def turtle_move(direction):
    if direction == "left":
        my_turtle.left(90)
    elif direction == "right":
        my_turtle.right(90)
    elif direction == "backward":
        my_turtle.left(180)
    my_turtle.forward(50)

my_turtle = Turtle()
my_turtle.width(15)
my_turtle.speed(10)
my_turtle.forward(50)
for _ in range(0, 500):
    direction = random.choice(directions)
    my_turtle.color(random.choice(colors))
    turtle_move(direction)




my_screen = Screen()
my_screen.exitonclick()