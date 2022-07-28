import turtle
from itertools import cycle
from random import randint, random

#Width: 700
#Height: 500

turtle.pensize(4)

colors = cycle(["red", "orange", "yellow", "green", "blue", "purple"])

def drawshape(sides, size):
    turtle.right(randint(0, 360))

    for i in range(sides):
        turtle.forward(size)
        turtle.right(360/sides)

for i in range(36):
    turtle.pencolor(next(colors))

    turtle.penup()
    turtle.goto(randit(-350, 300), randint(-250, 250))
    turtle.pendown()

    drawshape(randint(3, 8), randint