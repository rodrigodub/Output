#################################################
#                   INPUT
# Programação de Jogos 4
# Campo Minado / Movimento
#
# Usage:
# > python3 Input04PJ04_c.py
#
# v2.078
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
        self.vector = (2, 0)

    def move(self):
        # movement rules
        self.pos.left += self.vector[0]
        self.pos.top += self.vector[1]
        if self.pos.left > 640:
            self.pos.left = 0
        if self.pos.left < 0:
            self.pos.left = 640
        if self.pos.top > 480:
            self.pos.top = 230
        if self.pos.top < 230:
            self.pos.top = 480

    def control(self):
        keys = pygame.key.get_pressed()
        if keys[K_SPACE]:
            self.vector = (0, 0)
        if keys[K_RIGHT]:
            self.vector = (2, 0)
        if keys[K_LEFT]:
            self.vector = (-2, 0)
        if keys[K_UP]:
            self.vector = (0, -2)
        if keys[K_DOWN]:
            self.vector = (0, 2)
        if keys[K_RIGHT] and keys[K_UP]:
            self.vector = (2, -2)
        if keys[K_LEFT] and keys[K_UP]:
            self.vector = (-2, -2)
        if keys[K_RIGHT] and keys[K_DOWN]:
            self.vector = (2, 2)
        if keys[K_LEFT] and keys[K_DOWN]:
            self.vector = (-2, 2)


# paratrooper
class Paratrooper(object):
    """Define a paratrooper, its initial and final position, and state (0: on air, 1: on ground, 2:rescued)"""
    def __init__(self):
        self.image = load_image('skydiver.png')
        self.initial = (random.randint(0, 640), -20)
        self.final = (random.randint(10, 630), random.randint(230, 470))
        self.pos = self.image.get_rect().move(self.initial[0], self.initial[1])
        self.state = 0
        self.duration = 200
        self.proximity = self.duration

    def move(self):
        if self.proximity > 0:
            self.pos.left += (self.final[0] - self.initial[0]) / self.duration
            self.pos.top += (self.final[1] - self.initial[1]) / self.duration
            self.proximity -= 1
        else:
            self.state = 1
            self.pos = self.image.get_rect().move(self.final[0], self.final[1])


# paratrooperlist

# skydmovement


# event loop
def eventloop(scr, tnk, prt):
    # arguments: scr=screen, tnk=tank, prt=paratrooper
    while True:
        # quit gracefully
        for event in pygame.event.get():
            if event.type == pygame.QUIT or pygame.key.get_pressed()[K_q]:
                sys.exit()
        # check tank controls
        tnk.control()
        # blit the background to erase the last tank position
        scr.area.blit(scr.image, tnk.pos, tnk.pos)
        # blit the background to erase the last paratrooper position
        scr.area.blit(scr.image, prt.pos, prt.pos)
        # move tank
        tnk.move()
        # move paratrooper
        prt.move()
        # blit tank in new position
        scr.area.blit(tnk.image, tnk.pos)
        # blit paratrooper in new position
        scr.area.blit(prt.image, prt.pos)
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
    # creates a paratrooper
    parat1 = Paratrooper()
    # start the event loop with tank moving right
    eventloop(screen, thetank, parat1)


# execute main
if __name__ == '__main__': 
    main()


