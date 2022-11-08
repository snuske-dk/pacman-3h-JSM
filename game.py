# Pac-Man clone made for learning/teaching git and Python

import random
import time
import pygame as pg

from pacman import PacMan
from ghost import Ghost

## Setup ##
pg.init()

screen = pg.display.set_mode((8*32,7*32))
pg.display.set_caption("Pac-Man (clone)")

font_press_enter = pg.font.Font(None, 32)

## Game loop ##
state = "LOAD"
running = True
while running:
    
    if state == "LOAD":
        pacman = PacMan(1,1)
        ghost = Ghost(3,2)
        direction = None

        # Level tiles 
        level = []
        with open("level.txt", "r") as level_file:
            for line in level_file:
                line = line.rstrip("\r\n") # Remove line endings
                row = []
                for character in line:
                    row.append(character)
                level.append(row)

        state = "READY"


    elif state == "READY":
        text = font_press_enter.render("Press [Enter] to play", True, (220,220,10))
        text_rect = text.get_rect(center=(8*32/2, 7*32/2)) 
        screen.blit(text, text_rect)

        events = pg.event.get()
        for event in events:
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    state = "PLAY"

        pg.display.flip()  
        time.sleep(0.1)
        

    elif state == "PLAY":

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

        pacman.move(level,direction)
        ghost.move(level)


        ## Draw ##
        screen.fill((0,0,0)) 

        # Draw level
        for row_idx, row in enumerate(level):
            for col_idx, tile in enumerate(row):
                if tile == "#":
                    pg.draw.rect(screen, (10,10,250), pg.Rect(col_idx*32+1, row_idx*32+1, 30, 30), 1)


        ghost.draw(screen)
        pacman.draw(screen)

        # Update window with newly drawn pixels
        pg.display.flip()  

        # Limit framerate by waiting a 10-100 milliseconds
        time.sleep(0.15)