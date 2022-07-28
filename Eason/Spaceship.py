HEIGHT = 800
WIDTH = 1200
lasers = []
laserstwo = []
lefthealth = 5
righthealth = 5
cooldown=1
othercooldown=1
running=True

ship2 = Actor("playership2_blue.png")
ship2.center = (1000, 500)
spaceship = Actor("playership2_red.png")
spaceship.center = (50, 500)
ship2.angle = 90
spaceship.angle = -90


def draw():
    screen.clear()
    screen.blit("cover1.jpg",(0,0))
    spaceship.draw()
    ship2.draw()
    for items in lasers:
        items.draw()
    for items in laserstwo:
        items.draw()
    screen.draw.text("health",(50,50))
    screen.draw.text("health: "+str(lefthealth),(50,50))
    screen.draw.text("health: "+str(righthealth),(1050,50))
    if lefthealth==0:
        screen.draw.text("Gameover",(500,500))
    if righthealth==0:
        screen.draw.text("Gameover",(500,500))
def update(dt):
    global cooldown
    global othercooldown
    global lefthealth
    global righthealth
    global running
    if lefthealth==0 or righthealth==0:
        running=False
    if running:

        if keyboard.up and ship2.y>=0:
            ship2.y -= 10
        if keyboard.down and ship2.y<=800:
            ship2.y += 10
        if keyboard.left and ship2.x>=0:
            ship2.x -= 10
        if keyboard.right and ship2.x<=1200:
            ship2.x += 10
        if keyboard.W and spaceship.y>=0:
            spaceship.y -= 10
        if keyboard.S and spaceship.y<=800:
            spaceship.y += 10
        if keyboard.A and spaceship.x>=0:
            spaceship.x -= 10
        if keyboard.D and spaceship.x<=1200:
            spaceship.x += 10
        if keyboard.space:
            if cooldown>0.5:
                cooldown=0
                laser = Actor("laserblue04.png")
                laser.x = ship2.x
                laser.y = ship2.y
                laser.angle = 90
                lasers.append(laser)
        for items in lasers:
            items.x -= 5
            if items.x<0:
                lasers.remove(items)
            if items.colliderect(spaceship):
                lefthealth-=1
                lasers.remove(items)
        cooldown+=dt
        othercooldown+=dt
        for items in laserstwo:
            items.x += 5
            if items.x>1200:
                laserstwo.remove(items)
            if items.colliderect(ship2):
                righthealth-=1
                laserstwo.remove(items)
        if keyboard.p:
            if othercooldown>0.5:
                othercooldown=0
                lasertwo = Actor("laserred04.png")
                lasertwo.x = spaceship.x
                lasertwo.y = spaceship.y
                lasertwo.angle = 90
                laserstwo.append(lasertwo)

