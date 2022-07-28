TILE_SIZE = 32
WIDTH = TILE_SIZE *20
HEIGHT = TILE_SIZE *20

tiles = ["miniempty","miniwall","minigoal","minidoor","minikey"]
unlock = 0
maze = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,1,0,0,3,0,0,0,0,1,1,1,1,0,1,0,0,1,1],
    [1,0,0,0,1,1,3,1,0,4,0,1,1,1,0,4,0,0,0,1],
    [1,0,1,0,1,0,0,1,4,0,0,1,1,1,0,0,4,3,0,1],
    [1,0,1,0,1,0,1,1,0,1,0,1,0,3,0,1,3,0,0,1],
    [1,0,1,0,1,0,0,4,3,0,0,1,1,1,0,1,0,1,0,1],
    [1,0,1,0,1,0,1,1,0,1,1,1,0,0,0,1,0,0,0,1],
    [1,0,4,0,0,0,1,1,1,0,4,1,3,1,0,4,3,1,3,1],
    [1,0,1,0,0,0,1,1,1,1,1,1,1,3,1,1,4,1,1,1],
    [1,0,3,0,3,0,0,0,4,3,3,1,1,1,3,3,1,0,0,1],
    [1,4,3,1,0,1,3,0,3,0,0,1,4,1,4,1,3,0,1,1],
    [1,3,1,1,1,1,3,0,1,3,3,0,1,1,0,1,1,4,1,1],
    [1,4,0,1,3,4,0,0,0,0,3,1,1,1,0,0,0,1,1,1],
    [1,0,1,3,1,1,1,4,0,3,1,0,0,1,1,0,0,0,4,1],
    [1,3,1,1,1,1,1,0,0,1,3,1,3,1,1,0,0,1,3,1],
    [1,0,1,1,1,0,1,4,3,1,0,1,0,0,1,0,1,1,4,1],
    [1,0,1,1,1,0,4,3,1,1,1,0,1,0,4,3,3,1,1,1],
    [1,0,1,1,1,0,3,0,1,0,3,0,1,0,0,3,0,0,1,1],
    [1,3,0,4,0,3,4,0,4,3,0,4,3,0,3,0,0,4,2,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
]

player = Actor("minialienicon.png", anchor=(0,0), pos=(1 * TILE_SIZE, 1 * TILE_SIZE))
enemy = Actor("minidogicon.png", anchor=(0,0), pos=(3* TILE_SIZE, 6 * TILE_SIZE))

enemy.yv= -1
def draw():
    screen.clear()
    for row in range(len(maze)):
        for column in range(len(maze[row])):
            x = column * TILE_SIZE
            y = row * TILE_SIZE
            tile = tiles[maze[row][column]]
            screen.blit(tile, (x,y))
        player.draw()
        enemy.draw()


def on_key_down(key):
    global unlock
    global keycounter
    row = int(player.y / TILE_SIZE)
    column = int(player.x / TILE_SIZE)
    if key == keys.UP:
        row = row - 1
    if key == keys.DOWN:
        row = row + 1
    if key == keys.LEFT:
        column = column - 1
    if key == keys.RIGHT:
        column = column + 1
    tile = tiles[maze[row][column]]
    if tile == "miniempty":
        x = column * TILE_SIZE
        y = row * TILE_SIZE
        animate(player, duration=0.1, pos=(x,y))
    elif tile == "minigoal":
        print("Well done")
        exit()
    elif tile == "minikey":
        x = column * TILE_SIZE
        y = row * TILE_SIZE
        animate(player, duration=0.1, pos=(x,y))
        unlock = unlock + 1
        maze[row][column] = 0 # 0 is "empty" tile
    elif tile == "minidoor" and unlock > 0:
        x = column * TILE_SIZE
        y = row * TILE_SIZE
        animate(player, duration=0.1, pos=(x,y))
        unlock = unlock - 1
        maze[row][column] = 0 # 0 is "empty" tile

    row = int(enemy.y / TILE_SIZE)
    column = int(enemy.x / TILE_SIZE)
    row = row + enemy.yv
    tile = tiles[maze[row][column]]
    if not tile == "miniwall":
        x = column * TILE_SIZE
        y = row * TILE_SIZE
        animate(enemy, duration=0.1, pos=(x,y))
    else:
        enemy.yv = enemy.yv * -1
    if enemy.colliderect(player):
        print("You Died")
        exit()
