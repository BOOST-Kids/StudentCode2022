TILE_SIZE = 64
WIDTH = TILE_SIZE * 8
HEIGHT = TILE_SIZE * 8

tiles = ['empty', 'wall', 'goal'] #List of images

maze = [
    [1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ],
    [1 ,0 ,0 ,1 ,0 ,0 ,1 ,1 ],
    [1 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ],
    [1 ,0 ,0 ,0 ,1, 0 ,1, 1 ],
    [1, 0 ,1 ,0 ,1 ,0 ,0 ,1 ],
    [1 ,0, 1, 0, 1, 0 ,0 ,1 ],
    [1, 0, 0, 2, 1, 0, 0, 1 ],
    [1, 1, 1, 1, 1, 1, 1, 1 ],
]

player = Actor("dogicon.png", anchor = (0, 0), pos=(1 * TILE_SIZE, 1 * TILE_SIZE)) #draws the player
enemy = Actor("alienicon.png", anchor = (0,0), pos=(3 * TILE_SIZE, 6 * TILE_SIZE))
enemy.yv = -1

def draw():
    screen.clear()
    for row in range (len(maze)):
        for column in range (len(maze[row])):
            x = column * TILE_SIZE
            y = row * TILE_SIZE
            tile = tiles[maze[row][column]]
            screen.blit(tile, (x,y))
    player.draw()
    enemy.draw()

def on_key_down(key):
    row = int(player.y / TILE_SIZE)
    column = int(player.x / TILE_SIZE)#gets coordinates by dividing the player size by the tile size
    if key == keys.W:
        row = row - 1
    if key == keys.S:
        row = row + 1
    if key == keys.A:
        column = column - 1
    if key == keys.D:
        column = column + 1
    tile = tiles [maze[row][column]]
    if tile == 'empty':
        x = column * TILE_SIZE
        y = row * TILE_SIZE
        animate(player, duration=0.1, pos=(x, y))
    elif tile == 'goal':
        print("Well done!!! :-D") #well done!!!
        exit()

    #enemy movement section :) :) :)
    row = int(enemy.y / TILE_SIZE)
    column = int(enemy.x / TILE_SIZE)
    row = row + enemy.yv
    tile = tiles[maze[row][column]]
    if not tile == 'wall':
        x = column * TILE_SIZE
        y = row * TILE_SIZE
        animate(enemy, duration=0.1, pos=(x,y))
    else:
        enemy.yv = enemy.yv * -1
    if enemy.colliderect(player):
        print("You died!! D-:")
        exit()