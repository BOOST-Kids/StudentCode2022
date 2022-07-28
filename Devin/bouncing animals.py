WIDTH = 700
HEIGHT = 700

bob = Actor('walrus')
bob.pos = (98, 168)

velocityx = 0
velocityy = 100

def update():
    global velocityx, velocityy

    bob.x += velocityx
    bob.y -= velocityy

    if bob.y <= 0 or bob.y >= HEIGHT:
        velocityy *=-1

    if bob.y <= 0 or bob.y >= WIDTH:
        velocityx *=-1
def draw():
    screen.fill((234, 67, 138))
    bob.draw()