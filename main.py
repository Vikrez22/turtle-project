from turtle import Turtle, Screen
import random

tim = Turtle()

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]


# turtle shapes
def draw_shape(num_sides):
    angle = 360 / num_sides
    for i in range(num_sides):
        angle = 360 / num_sides
        tim.forward(100)
        tim.right(angle)

for shape_side_n in range(3, 10):
    tim.color(random.choice(colours))
    draw_shape(shape_side_n)







screen = Screen()
screen.exitonclick()