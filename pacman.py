import pygame as pg

class PacMan:

    def __init__(self, row, col):

        # https://sfxr.me/#34T6PktF8TcRjBGBCtaWAp8xrJeEmwSfouC2KVwAWC42iM2UWcDqruxhd8Xq4MFBc7kMaDGuyeyqde9ddiWDHprGh2dvs6Ery9NZQmbQM9gyXmSZzdhxPnMnw
        # https://sfxr.me/#34T6PkpqAUU8XZ3ze41FCou6ZCuAPdnvQEjkm2P1TPRMxjSRZdiQm9e5DJF1dPTvN8C3gPXJ7DuFniwZVHsmDC5qDkCUYDnkkgQAsqe9MaC2pHxKexVqdd5Jw
        self.sound_move0 = pg.mixer.Sound("sounds/pacman_move_0.wav")
        self.sound_move1 = pg.mixer.Sound("sounds/pacman_move_1.wav")
        self.sound_move0.set_volume(0.5)
        self.sound_move1.set_volume(0.5)

        self.col = col
        self.row = row
        self.direction = "left"

        self.images = []
        for i in range(6):
            img = pg.image.load(f"images/pacman_{i}.png")
            img = pg.transform.scale(img, (32,32))
            self.images.append(img)

        self.tick = 0


    def move(self, level, direction):
        # Move pacman
        self_direction = None
        tick = 0
        moving = False
        if direction == "up":
            if level.tiles[self.row-1][self.col] != "#":
                self_direction = "up"
                self.row -= 1
                moving = True
        elif direction == "down":
            if level.tiles[self.row+1][self.col] != "#":
                self_direction = "down"
                self.row += 1
                moving = True
        elif direction == "left":
            if level.tiles[self.row][self.col-1] != "#":
                self_direction = "left"
                self.col -= 1
                moving = True
        elif direction == "right":
            if level.tiles[self.row][self.col+1] != "#":
                self_direction = "right"
                self.col += 1
                moving = True
        
    def draw(self,screen,direction):
        r = int((self.tick/2)%6)
        if direction == "left":
            screen.blit(self.images[r], (self.col, self.row))
        elif direction == "right":
            screen.blit(pg.transform.rotate(self.images[r],180), (self.col, self.row))
        elif direction == "up":
            screen.blit(pg.transform.rotate(self.images[r],-90), (self.col, self.row))
        elif direction == "down":
            screen.blit(pg.transform.rotate(self.images[r],90), (self.col, self.row))
        else:
            screen.blit(self.images[0], (self.col, self.row))
        
        moving = True
        if moving:
            if self.tick%2 == 0:
                self.sound_move0.play()
            else:
                self.sound_move1.play()

        self.tick += 1 
    
    




