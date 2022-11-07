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


## Game loop ##
running = True
x = 0
y = 0
ghost_x = 100
ghost_y = 100
tick = 0
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
                y -= 5
            elif event.key == pg.K_DOWN:
                y += 5
            elif event.key == pg.K_LEFT:
                x -= 5
            elif event.key == pg.K_RIGHT:
                x += 5
            elif event.key == pg.K_ESCAPE:
                running = False

    ## Move / logic ##
    ghost_x += random.randint(-5,5)
    ghost_y += random.randint(-5,5)


    ## Draw ##
    screen.fill((0,0,0)) 
    
    # Draw pacman
    r = tick%6
    screen.blit(pacman_images[r], (x,y)) 

    # Draw ghost
    r = int(tick/2)%2 # int(tick/2) for half animation speed
    screen.blit(ghost_images[r], (ghost_x, ghost_y))


    # Update window with newly drawn pixels
    pg.display.flip()  
    tick += 1

    # Limit framerate by waiting a 10-100 milliseconds
    time.sleep(0.05)