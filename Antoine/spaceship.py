HEIGHT = 500
WIDTH = 1200
lasers = []
cooldown = 0.375
lasers2 = []
running = True
othercooldown = 0.375
ship = Actor ("playership2_blue")
ship.center =(100,250)
ship.angle = 270
righthealth = 100
lefthealth = 100
redship = Actor ("playership1_red")
redship.center =(1100,250)
redship.angle = 90
def draw():
    screen.clear()
    screen.blit("83675_1648779636_a90c11721f772d74f8ab02c00d599f78.webp",(0,0))
    redship.draw()
    ship.draw()
    for items in lasers:
        items.draw()
    for items in lasers2:
        items.draw()
    screen.draw.text("Health:"+str(righthealth),(50,50))
    screen.draw.text("Health:"+str(lefthealth),(1100,50))
    if (righthealth) == 0:
        screen.draw.text(("GAME OVER: REDSHIP WINS"),(700,400))
    if (lefthealth) == 0:
        screen.draw.text(("GAME OVER: BLUESHIP WINS"),(700,400))
def update(dt):
    global cooldown
    global othercooldown
    global lefthealth
    global righthealth
    global running
    if righthealth == 0 or lefthealth ==0:
        running = False
    if running:
        if keyboard.W and ship.y >=0:
            ship.y-=10
        if keyboard.S and ship.y <=800:
            ship.y+=10
        if keyboard.D and ship.x <=1400:
            ship.x+=15
        if keyboard.A and ship.x >=0:
            ship.x-=10
        if keyboard.up and redship.y >=0:
            redship.y-=10
        if keyboard.down and redship.y <=800:
            redship.y+=10
        if keyboard.right and redship.x <=1400:
            redship.x+=10
        if keyboard.left and redship.x >=0:
            redship.x-=15
        if keyboard.space:
            if cooldown>0.375:
                cooldown=0
                laser = Actor ("laserred03.png")
                laser.x=redship.x
                laser.y=redship.y
                laser.angle = 90
                lasers.append(laser)
        for items in lasers:
            items.x-=10
            if items.x<=0:
                lasers.remove(items)
            if items.colliderect(ship):
                righthealth-=20
                lasers.remove(items)
        cooldown+=dt
        if keyboard.z:
            if othercooldown>0.375:
                othercooldown=0
                laser2 = Actor ("laserblue03.png")
                laser2.x= ship.x
                laser2.y=ship.y
                laser2.angle = 90
                lasers2.append(laser2)
        for items in lasers2:
            items.x+=10
            if items.x<=0:
                lasers2.remove(items)
            if items.colliderect(redship):
                lefthealth-=20
                lasers2.remove(items)
        othercooldown+=dt
