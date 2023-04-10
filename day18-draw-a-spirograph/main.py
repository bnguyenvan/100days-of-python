import turtle as t
from turtle import Screen
import random

timy = t.Turtle()
timy.speed("fastest")
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

# def draw_circle(number_slides):
#     angle = 360 / number_slides
#     len = (2 * 3.14 * 100) / number_slides
#     for _ in range(number_slides):
#         timy.forward(len)
#         timy.right(angle)

#angle_total = 360/100

def draw_spirograph(size_of_graph):
    for _ in range(int(360 / size_of_graph)):
        timy.color(random_color())
        timy.circle(100)
        timy.setheading(timy.heading() + size_of_graph)

draw_spirograph(5)

my_screen = t.Screen()
my_screen.exitonclick()
