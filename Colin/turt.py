import turtle
from itertools import cycle
from random import randint, random

randint(1, 200)
turtle.goto(1, 100)

Width: 700
Hieght: 500

turtle.bgcolor('black')
turtle.pencolor('lightyellow')
turtle.speed('fast')
turtle.pensize(5)
turtle.pendown()

def drawshape(sides, size):
    turtle.right(randint(0,360))

    for i in range(sides):
        turtle.forward(size)
        turtle.right(360/sides)

for i in range (36):
    colors=cycle(["purple","orange","blue"])

    turtle.pencolor(next(colors))

for i in range(5):
    turtle.forward(50)
    turtle.right(72)

    turtle.right(20)

    turtle.penup()
    turtle.right(10)
    turtle.goto(randint(-300, 300), randint(-300, 300))
    turtle.pendown()

    drawshape(randint(3, 8), randint(30, 50))