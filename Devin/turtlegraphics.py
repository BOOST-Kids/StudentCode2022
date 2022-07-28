import turtle
from itertools import cycle
from random import randint, random

randint(1, 100)
turtle.goto(randint(1, 100), randint(1, 100))

turtle.bgcolor("black")
turtle.pencolor("red")
turtle.speed("fast")
turtle.pensize(4)
colors = cycle(["red", "orange", "yellow", "green", "blue", "purple"])

turtle.pendown()
def drawshape(sides, size):
    turtle.right(randint(0, 360))

    for i in range(sides):
        turtle.forward(size)
        turtle.right(360/sides)

for i in range(36):
    turtle.pencolor(next(colors))

    turtle.penup()
    turtle.goto(randint(-350, 300), randint(-250,250))
    turtle.pendown()

    drawshape(randint(3,10), randint(30, 50))