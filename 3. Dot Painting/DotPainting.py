from turtle import Turtle, Screen
from random import choice
import colorgram

timmy = Turtle()
timmy.speed(10)
screen = Screen()
screen.colormode(255)
# This module can extract a sequence of colors from a picture
colors = colorgram.extract('Dot painting\image.jpg', 30)

def random_color(colors):
    color = choice(colors)
    return color.rgb

timmy.penup()
for y in range(-5, 5):
    timmy.sety(50 * y)
    for x in range(-5, 5):
        timmy.setx(50 * x)
        timmy.dot(20, random_color(colors))
        timmy.penup()

screen.exitonclick()

