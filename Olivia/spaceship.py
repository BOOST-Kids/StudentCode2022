# Write your code here >:]
HEIGHT=800
WIDTH= 800

laser1 = []
cooldown = 0.5 #makes lasers wait
laser2 = []
othercooldown = 0.5

shipRed=Actor("playership1_red")
shipRed.center = 750,400
shipRed.angle = 90

shipBlue=Actor("playership1_blue")
shipBlue.center = 50, 400
shipBlue.angle = 270

RedHealth=20
BlueHealth=20

running = True #checks if its running

def draw():
    screen.clear() #clears screen for other stuff
    screen.blit ("background.jpg", (0,0)) #spaace!!!
    shipBlue.draw()
    shipRed.draw()
    for items in laser1:
        items.draw() #draws lasers in the list above
    for items in laser2:
        items.draw() #draws lasers in the list
    screen.draw.text ("Health: " +str(BlueHealth), (30,30))
    screen.draw.text ("Health: " +str(RedHealth), (700,30))
    if BlueHealth == 0:
        screen.draw.text ("The Red Ship has Won!", (335,400)) #game over gg
    if RedHealth == 0:
        screen.draw.text ("The Blue Ship has Won!", (330,400)) #game over!
def update(dt):
    global BlueHealth
    global RedHealth
    global cooldown
    global othercooldown
    global running

    if RedHealth == 0 or BlueHealth == 0:
        running = False #stops the game
    if running:
        if keyboard.u and shipRed.y >= 0: #bumps the top
            shipRed.y -= 8
        if keyboard.j and shipRed.y <= 800: #bumps bottom of screen
            shipRed.y += 8
        if keyboard.h and shipRed.x >=0: #bumps left side of screen
            shipRed.x -= 8
        if keyboard.k and shipRed.x <= 800: #bumps right side of screen
            shipRed.x += 8 #makes red ship move

        if keyboard.w and shipBlue.y >= 0: #bumps top of screen
            shipBlue.y -= 10
        if keyboard.s and shipBlue.y <= 800: #bumps bottom of screen
            shipBlue.y += 10
        if keyboard.a and shipBlue.x >= 0: #bumps left side of screen
            shipBlue.x -= 10
        if keyboard.d and shipBlue.x <=800: #bumps right side of screen
            shipBlue.x += 10 #makes blue ship move
        if keyboard.y:
            if cooldown > 0.5:
                cooldown = 0
                laserRed = Actor("laserred04")
                laserRed.x = shipRed.x
                laserRed.y = shipRed.y
                laserRed.angle = 90
                laser1.append(laserRed) #adds to a list
        for items in laser1:
            if items.colliderect(shipBlue):
                BlueHealth -= 1
                laser1.remove (items) #collide, removes health
            items.x -= 7
            if items.x < 0 :
                laser1.remove (items)
        cooldown += dt
        if keyboard.e:
            if othercooldown > 0.5:
                othercooldown = 0
                laserBlue = Actor("laserblue04")
                laserBlue.x = shipBlue.x
                laserBlue.y = shipBlue.y
                laserBlue.angle = 90
                laser2.append(laserBlue) #adds to a list
        for items in laser2:
            if items.colliderect(shipRed):
                RedHealth -= 1
                laser2.remove (items) #collide, removes health
            items.x += 7
            if items.x > WIDTH:
                laser2.remove (items)
        othercooldown += dt