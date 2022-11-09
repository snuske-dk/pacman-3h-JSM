import pygame as pg
import random

class Ghost:

    def __init__(self, row, col):

        self.col = col
        self.row = row

        self.images = []
        for i in range(2):
            img = pg.image.load(f"images/ghost_{i}.png")
            img = pg.transform.scale(img, (32,32))
            self.images.append(img)

        self.tick = 0


    def move(self, level):
        self.col += random.randint(-1,1)
        self.row += random.randint(-1,1)

        self.tick += 1 
    
    def draw(self,screen):
        r = self.tick%2
        screen.blit(self.images[r], (self.col*32, self.row*32)) 