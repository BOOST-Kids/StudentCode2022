WIDTH = 700
HEIGHT= 800

Donke = Actor ('alien')
Donke.pos =(200,200)

velocityx = 100
velocityy = 200
def update():
    global velocityx, velocityy

    Donke.x += velocityx
    Donke.y += velocityy

    if Donke.y <= 0 or Donke.y >= HEIGHT:
        velocityy *= -1

    if Donke.x <= 0 or Donke.x >= HEIGHT:
        velocityx *= -1
def draw():
    screen.fill((20,70,6))
    Donke.draw()