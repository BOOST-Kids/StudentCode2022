WIDTH= 1500
HEIGHT=750


lefthealth = 30
righthealth = 10000
lasers = []
laserstwo = []
othercooldown=1
cooldown = 1
running= True

playership2 = Actor ("enemyblue3.png")
playership2.center = (50,400)
playership2.angle = 450


playership = Actor ("playership3_blue.png")
playership.center = (1450,400)
playership.angle = 90
def draw():
    screen.clear()
    screen.blit ("space-background-with-abstract-shape-stars_189033-30.webp", (0,0))
    playership.draw()
    playership2.draw()
    for items in lasers:
        items.draw()
    for items in laserstwo:
        items.draw()
    screen.draw.text("health",(50,50))
    screen.draw.text ("health:"+str(lefthealth), (50,50) )
    screen.draw.text("health",(50,50))
    screen.draw.text ("health:"+str(righthealth), (1400,50) )
    if lefthealth == 0:
        screen.draw.text ("game over player right wins", (750, 550))
    if righthealth == 0:
        screen.draw. text ("game over player left wins", (750, 550))
def update(dt):
    global cooldown
    global othercooldown
    global lefthealth
    global righthealth
    global running
    if lefthealth == 0 or righthealth == 0:
        running = False
    if running:
        cooldown+= dt
        othercooldown+= dt
        if keyboard.up and playership.y > 0:
            playership.y-=10
        if keyboard.down and playership.y < 750:
            playership.y+=10
        if keyboard.right and playership.x < 1500:
            playership.x+=10
        if keyboard.left and playership.x > 0:
            playership.x-=10

        if keyboard.w and playership2.y > 0:
            playership2.y-=10
        if keyboard.s and playership2.y < 750:
            playership2.y+=10
        if keyboard.d and playership2.x < 1500:
            playership2.x+=10
        if keyboard.a and playership2.x > 0:
            playership2.x-=10

        if keyboard.space:
            if cooldown > 0.5:
                cooldown = 0
                laser = Actor ("lasergreen06.png")
                laser.x = playership.x
                laser.y = playership.y
                laser.angle = 90
                lasers.append (laser)
        for items in lasers:
                items.x-= 5
                if items.x < 0:
                    lasers.remove (items)
                if items.colliderect(playership2):
                    lefthealth-= 10
                    lasers.remove(items)
        for items in laserstwo:
                items.x+= 5
                if items.x > 1500 :
                    laserstwo.remove (items)
                if items.colliderect(playership):
                    righthealth-= 10
                    laserstwo.remove(items)
        if keyboard.e:
            if othercooldown > 0:
                othercooldown = 0
                lasertwo = Actor ("laserblue06.png")
                lasertwo.x = playership2.x
                lasertwo.y = playership2.y
                lasertwo.angle=90
                laserstwo.append (lasertwo)
