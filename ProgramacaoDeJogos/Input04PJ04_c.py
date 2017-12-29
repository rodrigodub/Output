#################################################
#                   INPUT
# Programação de Jogos 4
# Campo Minado / Movimento
#
# Usage:
# > python3 Input04PJ04_c.py
#
# v2.076
# 20171229
#################################################
__author__ = 'Rodrigo Nobrega'


# import
import os, sys, pygame
from pygame.locals import *
import random


# load image function
def load_image(file):
    path = os.path.join('images', file)
    return pygame.image.load(path).convert_alpha()


# screen
class Setupscreen(object):
    """Starts a screen and displays background"""
    def __init__(self, image_file):
        # physical parameters
        self.size = (640, 480)
        self.bgcolour = [90, 230, 90]
        # the canvas
        self.area = pygame.display.set_mode(self.size)
        # background image and its enclosing rectangle
        self.image = load_image(image_file)
        self.rect = self.image.get_rect()
        # show image
        self.show()

    def show(self):
        # fill screen with solid colour
        self.area.fill(self.bgcolour)
        # blit the image
        self.area.blit(self.image, (0, 0))


# tank
class Tank(object):
    """Creates the player's tank and controls how it moves"""
    def __init__(self, x, y):
        self.image = load_image('tank4.png')
        self.pos = self.image.get_rect().move(x, y)

    def move(self, vector):
        # movement rules
        self.pos.left += vector[0]
        self.pos.top += vector[1]
        if self.pos.left > 640:
            self.pos.left = 0
        if self.pos.left < 0:
            self.pos.left = 640
        if self.pos.top > 480:
            self.pos.top = 230
        if self.pos.top < 230:
            self.pos.top = 480
        

# tankmovement

# paratrooper

# skydmovement


# event loop
def eventloop(scr, tnk, vec):
    # arguments: scr=screen, tnk=tank, vec=tank vector
    vector = vec
    while True:
        # quit gracefully
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()
            # tank movement
            keys = pygame.key.get_pressed()
            if keys[K_SPACE]:
                vector = (0, 0)
            if keys[K_RIGHT]:
                vector = (2, 0)
            if keys[K_LEFT]:
                vector = (-2, 0)
            if keys[K_UP]:
                vector = (0, -2)
            if keys[K_DOWN]:
                vector = (0, 2)
            if keys[K_RIGHT] and keys[K_UP]:
                vector = (2, -2)
            if keys[K_LEFT] and keys[K_UP]:
                vector = (-2, -2)
            if keys[K_RIGHT] and keys[K_DOWN]:
                vector = (2, 2)
            if keys[K_LEFT] and keys[K_DOWN]:
                vector = (-2, 2)
        # blit the background to erase the last tank position
        scr.area.blit(scr.image, tnk.pos, tnk.pos)
        # move tank
        tnk.move(vector)
        # blit tank in new position
        scr.area.blit(tnk.image, tnk.pos)
        # refresh display
        pygame.display.flip()


# main routine
def main():
    print('\n ::: Input 04 - Campo Minado :::\n')
    # start Pygame
    pygame.init()
    # start the display
    screen = Setupscreen('desert640.png')
    # creates tank at initial position
    thetank = Tank(50, 300)
    # start the event loop with tank moving right
    eventloop(screen, thetank, (2, 0))


# execute main
if __name__ == '__main__': 
    main()


