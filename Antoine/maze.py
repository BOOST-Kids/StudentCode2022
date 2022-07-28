TILE_SIZE = 32
WIDTH = TILE_SIZE  *20
HEIGHT = TILE_SIZE  *20

tiles = ['miniempty','miniwall','minigoal', 'minidoor', 'minikey']

maze = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,3,0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,1],
    [1,1,0,1,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1],
    [1,1,0,1,1,0,0,0,0,0,0,1,1,1,0,0,0,0,0,1],
    [1,0,0,0,4,1,1,1,0,0,1,1,1,0,0,0,0,0,0,1],
    [1,0,1,0,1,4,1,0,0,1,1,4,1,1,1,1,1,0,0,1],
    [1,1,1,0,1,3,1,0,0,1,0,4,1,0,0,0,0,0,0,1],
    [1,4,0,1,1,0,0,0,0,1,0,1,1,0,0,0,0,1,1,1],
    [1,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,1,4,1],
    [1,1,1,1,1,1,1,1,3,1,0,1,0,0,0,0,0,1,0,1],
    [1,4,0,0,0,0,0,0,3,1,3,1,1,0,1,0,0,1,0,1],
    [1,0,0,0,0,0,0,0,0,1,0,0,1,0,1,0,0,1,0,1],
    [1,0,0,0,0,0,0,1,1,1,3,1,1,1,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,1,4,1,0,0,1,1,0,0,0,1,3,1],
    [1,0,0,0,0,0,0,1,4,1,3,0,1,0,0,0,1,4,4,1],
    [1,0,0,0,0,1,1,1,3,1,0,1,1,1,0,1,1,1,1,1],
    [1,0,0,0,0,1,4,0,0,1,0,0,0,0,0,1,0,0,0,1],
    [1,0,0,0,0,1,1,0,0,1,1,0,0,0,0,1,1,0,0,1],
    [2,3,0,0,0,0,0,0,0,1,4,0,0,0,1,1,0,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
unlock = 0
player = Actor("minialienicon.png", anchor = (0,0), pos = (1 * TILE_SIZE, 1 * TILE_SIZE))
enemy = Actor ("miniwalrusicon", anchor=(0,0), pos= (3 * TILE_SIZE, 6 * TILE_SIZE))
enemy2 = Actor ("minidogicon", anchor=(0,0), pos= (4 * TILE_SIZE, 8 * TILE_SIZE))
enemy.yv = -1
enemy2.yv = -1
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
        enemy2.draw()
def on_key_down(key):
    global unlock
    row = int(player.y / TILE_SIZE)
    column = int(player.x / TILE_SIZE)
    if key == keys.UP:
        row = row - 1
    if key == keys.DOWN:
        row = row +1
    if key ==keys.LEFT:
        column = column - 1
    if key == keys.RIGHT:
        column = column + 1
    tile = tiles[maze[row][column]]
    if tile == 'miniempty':
        x = column * TILE_SIZE
        y = row * TILE_SIZE
        animate(player, duration = 0.1,pos=(x,y))
    elif tile == 'minigoal':
        print ("well done")
        exit()
    elif tile == 'minikey':
        unlock = unlock + 1
        maze [row][column] = 0
    elif tile == 'minidoor' and unlock > 0:
        unlock = unlock - 1
        maze[row][column] = 0
        x = column * TILE_SIZE
        y = row * TILE_SIZE
        animate(player, duration = 0.1,pos=(x,y))
    if tile == 'minikey':
        x = column * TILE_SIZE
        y = row * TILE_SIZE
        animate(player, duration = 0.1,pos=(x,y))

    row = int(enemy.y / TILE_SIZE)
    column = int(enemy.x / TILE_SIZE)
    row = row + enemy.yv
    tile = tiles[maze[row][column]]

    if not tile == 'miniwall':
        x = column * TILE_SIZE
        y = row * TILE_SIZE
        animate(enemy, duration = 0.1, pos=(x,y))
    else:
        enemy.yv = enemy.yv * -1
    if enemy.colliderect(player):
        print ("how did you die to an npc lol")
        exit()
    row = int(enemy2.y / TILE_SIZE)
    column = int(enemy2.x / TILE_SIZE)
    column = column + enemy2.yv
    tile = tiles[maze[row][column]]
    if not tile == 'miniwall':
        x = column * TILE_SIZE
        y = row * TILE_SIZE
        animate(enemy2, duration = 0.1, pos=(x,y))
    else:
        enemy2.yv = enemy2.yv * -1
    if enemy2.colliderect(player):
        print ("you suck")
        exit()