leftspeed = 30
rightspeed = 30

WIDTH = 1200
HEIGHT= 700

ball = Actor ('pikaboo')
ball.pos =(600,350)

right = Actor ('garry')
right.pos =(1100,200)

left = Actor ('monke')
left.pos =(100,200)

velocityx = 7
velocityy = 7
def update():
    global velocityx, velocityy

    ball.x += velocityx
    ball.y += velocityy

    global leftspeed, rightspeed


    if ball.top <= 0 or ball.bottom >= HEIGHT:
        velocityy *= -1

    if ball.left <= 0 or ball.right >= WIDTH:
        velocityx *= -1

    if ball.right >= right.left:
        if ball.top <= right.bottom and ball.bottom >= right.top:
                velocityx *= -1
        else:
            ball.pos = (700,350)
            velocityx *= -1

    if ball.left <= left.right:
        if ball.top <= left.bottom and ball.bottom >= left.top:
                velocityx *= -1
        else:
            ball.pos = (700,350)
            velocityx *= -1


def draw():
    screen.fill((184,64,72))
    ball.draw()
    left.draw()
    right.draw()
def on_key_down(key):
    global leftspeed
    global rightspeed

    if key == keys.A:
        left.y+= leftspeed
    if key == keys.Q:
        left.y-= leftspeed

    if key == keys.L:
        right.y+= rightspeed
    if key == keys.P:
        right.y-= rightspeed

def on_key_up(key):

    if key == keys.A:
        leftspeed=0
    if key == keys.Q:
        leftspeed=0

    if key == keys.L:
        rightspeed=0
    if key == keys.P:
        rightspeed=0







