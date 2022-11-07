# Pac-Man clone made for learning/teaching git and Python

import random
import time
import pygame as pg

## Setup ##
pg.init()

screen = pg.display.set_mode((300,400))
pg.display.set_caption("Pac-Man (clone)")

pacman_images = []
for i in range(6):
    img = pg.image.load(f"images/pacman_{i}.png")
    img = pg.transform.scale(img, (32,32))
    pacman_images.append(img)

ghost_images = []
for i in range(2):
    img = pg.image.load(f"images/ghost_{i}.png")
    img = pg.transform.scale(img, (32,32))
    ghost_images.append(img)

# Level tiles 
# [0,0][0,1][0,2][0,2]
# [1,0][1,1][1,2][1,2]
# [2,0][2,1][2,2][2,2] <- row
# [3,0][3,1][3,2][3,2]
#        ^ 
#      column
level = [['#', '#', '#', '#', '#'],
         ['#', ' ', ' ', ' ', '#'],
         ['#', ' ', '#', ' ', '#'],
         ['#', ' ', '#', ' ', '#'],
         ['#', ' ', '#', ' ', '#'],
         ['#', ' ', '#', ' ', '#'],
         ['#', ' ', ' ', ' ', '#'],
         ['#', '#', '#', '#', '#']]


## Game loop ##
running = True
pacman_row = 1 
pacman_col = 1 
ghost_row = 3 
ghost_col = 2 
tick = 0
direction = None
while running:
    
    ## Handle events (keypresses etc.)
    events = pg.event.get()
    for event in events:

        # Close window (e.g. pressing [x] or Ctrl+F4)
        if event.type == pg.QUIT:
            running = False
        # Keypresses
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_UP:
                direction = "up"
            elif event.key == pg.K_DOWN:
                direction = "down"
            elif event.key == pg.K_LEFT:
                direction = "left"
            elif event.key == pg.K_RIGHT:
                direction = "right"
            elif event.key == pg.K_ESCAPE:
                running = False


    ## Move / logic ##
    
    # Move pacman
    if direction == "up":
        pacman_row -= 1
    elif direction == "down":
        pacman_row += 1
    elif direction == "left":
        pacman_col -= 1 
    elif direction == "right":
        pacman_col += 1 
    
    # Move ghost 
    ghost_col += random.randint(-1,1)
    ghost_row += random.randint(-1,1)


    ## Draw ##
    screen.fill((0,0,0)) 

    # Draw level
    for row_idx, row in enumerate(level):
        for col_idx, tile in enumerate(row):
            if tile == "#":
                pg.draw.rect(screen, (10,10,250), pg.Rect(col_idx*32+1, row_idx*32+1, 30, 30), 1)
    
    # Draw pacman
    r = tick%6
    screen.blit(pacman_images[r], (pacman_col*32, pacman_row*32)) 

    # Draw ghost
    r = int(tick/2)%2 # int(tick/2) for half animation speed
    screen.blit(ghost_images[r], (ghost_col*32, ghost_row*32))


    # Update window with newly drawn pixels
    pg.display.flip()  
    tick += 1

    # Limit framerate by waiting a 10-100 milliseconds
    time.sleep(0.15)