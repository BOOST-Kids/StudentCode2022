leftPaddlespeed = 10
rightPaddlespeed = 10
WIDTH = 1000
HEIGHT = 500
ball = Actor('rasengan')
ball.pos = (200,200)
leftPaddle = Actor('left_paddle')
leftPaddle.pos = (50,250)

rightPaddle = Actor('right_paddle')
rightPaddle.pos = (950,250)
velocityx = 6
velocityy = 5

def update():
    global velocityx, velocityy

    ball.x += velocityx
    ball.y += velocityy
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        velocityy *= -1
    if ball.left <= 0 or ball.right >= WIDTH:
        velocityx *= -1
    if ball.right >= rightPaddle.left:
        if ball.bottom >= rightPaddle.top and ball.top <= rightPaddle.bottom:

         velocityx *= -1

    if ball.left <= leftPaddle.right:

     if ball.bottom >= leftPaddle.top and ball.top <= leftPaddle.bottom:

         velocityx *= -1
    else:
        ball.pos = (500,250)
        velocityx
def draw():
    screen.fill((255, 255, 255))
    ball.draw()
    leftPaddle.draw()
    rightPaddle.draw()
def on_key_down(key):
    global leftPaddlespeed
    global rightPaddlespeed
    if key == keys.W:
        leftPaddle.y += leftPaddlespeed
    if key == keys.S:
        leftPaddle.y += leftPaddlespeed
    if key == keys.UP:
        rightPaddle.y += rightPaddlespeed
    if key == keys.DOWN:
        rightPaddle.y += rightPaddlespeed
def on_key_up(key):
    global rightPaddlespeed
    global rightPaddlespeed

    if key == keys.W:
        leftPaddlespeed = 0
    if key == keys.S:
        leftPaddlespeed = 0
    if key == keys.W:
        rightPaddlespeed = 0
    if key == keys.S:
        rightPaddlespeed = 0
