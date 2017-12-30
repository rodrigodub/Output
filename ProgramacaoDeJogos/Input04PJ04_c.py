#################################################
#                   INPUT
# Programação de Jogos 4
# Campo Minado / Movimento
#
# Usage:
# > python3 Input04PJ04_c.py
#
# v2.084
# 20171230
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
        # the displacement vector between each frame
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
        # number of frames between initial and final paratrooper position
        self.duration = 200
        # the more time passes (i.e. frames) the closest to final destination
        self.proximity = 0
        # step sizes
        self.deltax = (self.final[0] - self.initial[0]) / self.duration
        self.deltay = (self.final[1] - self.initial[1]) / self.duration
        # list with all trajectory intermediate positions
        self.trajectory = self.calculatetrajectory()

    def move(self):
        # move closer to the final destination
        if self.proximity < self.duration:
            self.pos = self.image.get_rect().move(self.trajectory[self.proximity])
            self.proximity += 1
        # move to final destination
        else:
            self.state = 1
            self.pos = self.image.get_rect().move(self.final[0], self.final[1])

    def calculatetrajectory(self):
        trajectoryfloat = []
        # first position is the initial position
        previouspos = self.initial
        trajectoryfloat.append(previouspos)
        # append a tuple (float x, float y) for each frame with the delta steps
        for i in range(0, self.duration):
            newpos = (previouspos[0] + self.deltax, previouspos[1] + self.deltay)
            trajectoryfloat.append(newpos)
            previouspos = newpos
        # calculate a new trajectory list with tuples (int x, int y), and return it
        trajectoryint = [(int(i[0]), int(i[1])) for i in trajectoryfloat]
        return trajectoryint


# paratrooperlist
class Paratrooperlist(object):
    def __init__(self):
        self.platoon = []

    def release(self):
        # release a new paratrooper if platoon is empty or if last paratrooper has landed
        if len(self.platoon) == 0 or (len(self.platoon) < 10 and self.platoon[-1].state == 1):
            self.platoon.append(Paratrooper())


# event loop
def eventloop(scr, tnk, prt):
    # arguments: scr=screen, tnk=tank, prt=paratrooper list
    while True:
        # quit gracefully
        for event in pygame.event.get():
            if event.type == pygame.QUIT or pygame.key.get_pressed()[K_q]:
                sys.exit()
        # check tank controls
        tnk.control()
        # release a paratrooper
        prt.release()
        # blit the background to erase the last paratrooper position
        scr.area.blit(scr.image, prt.platoon[-1].pos, prt.platoon[-1].pos)
        # blit the background to erase the last tank position
        scr.area.blit(scr.image, tnk.pos, tnk.pos)
        # move tank
        tnk.move()
        # move paratrooper
        prt.platoon[-1].move()
        # blit paratrooper in new position
        scr.area.blit(prt.platoon[-1].image, prt.platoon[-1].pos)
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
    # creates a paratrooper list
    parat1 = Paratrooperlist()
    # start the event loop with tank moving right
    eventloop(screen, thetank, parat1)


# execute main
if __name__ == '__main__': 
    main()


