WIDTH = 1000
HEIGHT = 500

leftPaddle = Actor('left_paddle')
leftPaddle.pos = (20, 250)

rightPaddle = Actor('right_paddle')
rightPaddle.pos = (980, 250)

ball = Actor('ball')
ball.pos = (200, 200)

velocityx = 6
velocityy = 5

leftPaddleVelocity = 0
rightPaddleVelocity = 0



def update():
    global velocityx, velocityy, leftPaddleVelocity, rightPaddleVelocity

    ball.x += velocityx
    ball.y += velocityy

    leftPaddle.y += leftPaddleVelocity
    rightPaddle.y += rightPaddleVelocity




    if ball.top <= 0 or ball.bottom >= HEIGHT:
        velocityy *= -1

    if ball.left <= 0 or ball.right >= WIDTH:
        velocityx *= -1

    if ball.right >= rightPaddle.left:
        if ball.top <= rightPaddle.bottom and ball.bottom >= rightPaddle.top:
            velocityx *= -1
        else:
            ball.pos =(500, 250)
            velocityx*= -1


    if ball.left <= leftPaddle.right:
        if ball.top <= leftPaddle.bottom and ball.bottom >= leftPaddle.top:
            velocityx *= -1
        else:
            ball.pos =(500, 250)
            velocityx*= -1


def draw():
    screen.fill((255, 255, 255))
    ball.draw()
    leftPaddle.draw()
    rightPaddle.draw()

def on_key_down(key):

    global leftPaddleVelocity, rightPaddleVelocity

    if key == key.W:
        leftPaddleVelocity = -5
    if key == key.S:
        leftPaddleVelocity = 5
    if key == key.UP:
        rightPaddleVelocity = -5
    if key == key.DOWN:
        rightPaddleVelocity = 5


def on_key_up(key):
    global leftPaddleVelocity, rightPaddleVelocity

    if key == key.W:
        leftPaddleVelocity = 0
    if key == key.S:
        leftPaddleVelocity = 0
    if key == key.UP:
        rightPaddleVelocity = 0
    if key == key.DOWN:
        rightPaddleVelocity = 0


