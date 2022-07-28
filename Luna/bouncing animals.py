WIDTH = 200
HEIGHT = 700

animal = Actor('dog')
animal.pos = (200,200)

velocityx = 2
velocityy = 2

def update():
    global velocityx, velocityy
    animal.y -= velocityy
    if animal.y <= 0 or animal.y >= HEIGHT:
        velocityy *= -1
    if animal.x <= 0 or animal.x >= WIDTH:
        velocityx *= -1
def draw ():
    screen.fill((0, 0, 0))
    animal.draw()



