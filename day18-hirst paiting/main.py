# import colorgram
# # Extract 6 colors from an image.
# colors = colorgram.extract('image.jpg', 100)
# colors_extract = []
# for i in colors:
#     red = i.rgb.r
#     blue = i.rgb.b
#     green = i.rgb.g
#     color = (red, blue, green)
#     colors_extract.append(color)
# print(colors_extract)
# print(len(colors_extract))
import turtle
import turtle as t
import random
my_turtle = t.Turtle()
color_list = [(212, 97, 154), (239, 243, 246), (52, 132, 108), (178, 33, 78), (198, 34, 143), (123, 97, 80), (235, 244, 240), (116, 171, 155), (124, 158, 175), (228, 129, 197), (194, 105, 85), (54, 20, 38), (12, 65, 51), (189, 142, 123), (54, 115, 120), (41, 126, 169), (167, 31, 21), (225, 78, 94), (4, 28, 30), (39, 34, 32), (243, 159, 163), (81, 168, 148), (164, 22, 27), (239, 167, 163), (104, 159, 123), (164, 193, 209), (21, 93, 81), (29, 81, 85), (162, 212, 206), (53, 81, 62), (183, 206, 190), (85, 35, 74)]
t.colormode(255)
my_turtle.speed("fastest")
my_turtle.penup()
my_turtle.hideturtle()

def draw_a_line(number_of_point):
    for i in range(number_of_point):
        my_turtle.dot(20, random.choice(color_list))
        if i < (number_of_point - 1):
            my_turtle.forward(70)
for i in range(10):
    my_turtle.setposition(-350, i * 70 - 350)
    draw_a_line(10)
my_screen = t.Screen()
my_screen.screensize(700, 700)
my_screen.exitonclick()