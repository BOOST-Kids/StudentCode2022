WIDTH = 300
HEIGHT = 300

WIDTH = 600
HEIGHT = 500

def draw():
    screen.fill((0,0,0))

alien = Actor('alien')
alien.pos = 100,56

WIDTH = 500
HEIGHT = alien.height + 20

def draw():
    screen.clear()
    alien.draw()

alien.topright = 0,10
def update():
    alien.left += 2
    if alien.left > WIDTH:
        alien.right = 0