WIDTH = 1000
HEIGHT = 500
leftspeed=7
rightspeed=7

def on_key_down(key):
    global leftspeed
    global rightspeed
    if key==keys.UP:
        sudowoodo.y -= rightspeed
    if key==keys.DOWN:
        sudowoodo.y += leftspeed
    if key==keys.W:
        sudowoodi.y -= rightspeed
    if key==keys.S:
        sudowoodi.y += leftspeed

def on_key_up(key):
    if key==keys.UP:
        rightspeed=0
    if key==keys.DOWN:
        sudowoodo.y += leftspeed
    if key==keys.W:
        rightspeed=0
    if key==keys.S:
        sudowoodi.y += leftspeed

sudowoodo = Actor('sudowoodo')
sudowoodo.pos = (950, 250)

sudowoodi = Actor('sudowoodi')
sudowoodi.pos = (50, 250)

ball = Actor('ball')
ball.pos = (500, 250)

velocityx = 5
velocityy = 0

def update():
    global velocityx, velocityy, leftspeed, rightspeed

    ball.x += velocityx
    ball.y += velocityy

    if ball.top <= 0 or ball.bottom >= HEIGHT:
        velocityy *= -1

    if ball.left <= 0 or ball.right >= WIDTH:
        velocityx *= -1

    if ball.right <= 0 or ball.left >= WIDTH:
        velocityx *= -1

    if ball.right >= sudowoodo.left:
        if ball.bottom >= sudowoodo.top and ball.top <= sudowoodo.bottom:
            velocityx *= -1
        else:
            ball.pos = (500, 250)
            velocityx *= -1

    if ball.left <= sudowoodi.right:
        if ball.bottom >= sudowoodo.top and ball.top <= sudowoodo.bottom:
            velocityx *= -1
        else:
            ball.pos = (500, 250)
            velocityx *= -1


def draw():
    screen.fill((234, 67, 138))
    ball.draw()

    sudowoodo.draw()

    sudowoodi.draw()