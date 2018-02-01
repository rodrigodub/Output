#################################################
#                   INPUT 6
# Programacao de Jogos 5
# Deadly Enemies and Aliens
#
# Usage:
# > python3 Input06PJ05.py
#
# v2.120
# 20180201
#################################################
__author__ = 'Rodrigo Nobrega'


# import
import os, sys, pygame
from pygame.locals import *
import random
import math
# import time


# load image function
def load_image(file):
    path = os.path.join('images/aliens', file)
    return pygame.image.load(path).convert_alpha()


# write text
def writetext(font, text, colour):
    # colour: tuple (r, g, b)
    a = font.render(text, 0, colour)
    return a


# tests if inside the space station shield perimeter
# radius = 32 (station) + 8 (shield) + 32 (alien ship)
# space station centre = (320, 240)
def testinside(x, y, radius):
    if radius > math.sqrt(pow((x - 320), 2) + pow((y - 240), 2)):
        return True
    else:
        return False


# screen
class Setupscreen(object):
    """Starts a screen and displays background"""
    def __init__(self, image_file=None):
        # physical parameters
        self.size = (640, 480)
        self.bgcolour = [230, 230, 230]
        # the canvas
        self.area = pygame.display.set_mode(self.size)
        self.title = pygame.display.set_caption('Deadly Enemies and Aliens')
        # background image and its enclosing rectangle
        if image_file:
            self.image = load_image(image_file)
            self.rect = self.image.get_rect()
        else:
            self.image = ''
            self.rect = Rect(0, 0, 0, 0)
        # show image
        self.show()

    def show(self):
        # fill screen with solid colour
        self.area.fill(self.bgcolour)
        # blit background image
        if self.image != '':
            self.area.blit(self.image, (0, 0))


# Space station
class Spacestation(object):
    """"Everything related to the Space Station"""
    def __init__(self):
        self.image = load_image('spacestation_64.png')
        self.pos = self.image.get_rect()
        self.pos.center = (320, 240)
        self.fuel = 100
        # shield images
        self.shield1 = load_image('shield_1b.png')
        self.shield2 = load_image('shield_2b.png')
        self.shield3 = load_image('shield_3b.png')
        self.shield4 = load_image('shield_4b.png')
        # shield positions
        self.shield1pos = self.shield1.get_rect()
        self.shield2pos = self.shield2.get_rect()
        self.shield3pos = self.shield3.get_rect()
        self.shield4pos = self.shield4.get_rect()
        # center them on space station
        self.shield1pos.bottomright = (320, 240)
        self.shield2pos.bottomleft = (320, 240)
        self.shield3pos.topleft = (320, 240)
        self.shield4pos.topright = (320, 240)

    def defend(self, scr):
        # params: scr=screen
        if self.fuel > 0:
            keys = pygame.key.get_pressed()
            if keys[K_1]:
                scr.area.blit(self.shield1, self.shield1pos)
                self.fuel -= 0.1
            else:
                scr.area.blit(scr.image, self.shield1pos, self.shield1pos)
                scr.area.blit(self.image, self.pos)
            if keys[K_2]:
                scr.area.blit(self.shield2, self.shield2pos)
                self.fuel -= 0.1
            else:
                scr.area.blit(scr.image, self.shield2pos, self.shield2pos)
                scr.area.blit(self.image, self.pos)
            if keys[K_3]:
                scr.area.blit(self.shield3, self.shield3pos)
                self.fuel -= 0.1
            else:
                scr.area.blit(scr.image, self.shield3pos, self.shield3pos)
                scr.area.blit(self.image, self.pos)
            if keys[K_4]:
                scr.area.blit(self.shield4, self.shield4pos)
                self.fuel -= 0.1
            else:
                scr.area.blit(scr.image, self.shield4pos, self.shield4pos)
                scr.area.blit(self.image, self.pos)
        else:
            scr.area.blit(scr.image, (280, 200, 80, 80), (280, 200, 80, 80))
            scr.area.blit(self.image, self.pos)

    def burn(self, scr):
        # params: scr=screen
        scr.area.blit(scr.image, (60, 15, 100, 10), (60, 15, 100, 10))
        scr.area.fill((200, 200, 200), (60, 15, self.fuel, 10))


# Alien ship
class Alien(object):
    """Class to deal with the alien ship"""
    def __init__(self):
        # alien ship image and position
        self.image = load_image('alienship_64.png')
        self.pos = self.image.get_rect()
        self.pos.center = (random.randint(0, 640), random.randint(0, 480))
        #self.posprev = self.pos
        self.posprev = self.image.get_rect()
        self.posprev.center = self.pos.center
        # vector defines the amount of movement in each axis
        self.vector = [0, 0]
        # blast has the same movement components as the ship
        self.blastimage = load_image('blast.png')
        self.blastpos = self.blastimage.get_rect()
        self.blastposprev = self.blastpos
        self.blastvector = [0, 0]
        # if firestate is 0, it can fire. If it's 1, it is firing
        self.firestate = 0
        # this is the shield that needs to be used
        self.defenseshield = 0

    def move(self, scr):
        # clears the previous position
        scr.area.blit(scr.image, self.posprev, self.posprev)
        # changes direction occasionally, modifying vector
        if random.randint(1, 20) == 1:
            self.vector[0] = random.randint(1, 3) * 5 - 10
            self.vector[1] = random.randint(1, 3) * 5 - 10
        # new position = old position + vector
        self.pos.center = (self.pos.centerx + self.vector[0], self.pos.centery + self.vector[1])
        # if ship is crossing borders, appears on the other side
        if self.pos.centerx < 0:
            self.pos.centerx += 640
        elif self.pos.centerx > 640:
            self.pos.centerx -= 640
        elif self.pos.centery < 42:
            self.pos.centery = 480 - self.pos.centery
        elif self.pos.centery > 480:
            self.pos.centery = 42
        # tests if alien ship is intersecting space station
        # radius = 80 (shield) + 32 (border of alien ship)
        if testinside(self.pos.centerx, self.pos.centery, 113):
            self.vector = [-i for i in self.vector]
        # draws alien ship
        scr.area.blit(self.image, self.pos)
        # makes the previous position as the current one
        self.posprev = self.pos

    def fire(self):
        # define if it's OK to fire, the trajectory and the shield to be used
        if self.firestate == 0:
            # OK to fire, decides when
            if random.randint(1, 100) == 1:
                # change firestate to 'firing'
                self.firestate = 1
                # initial blast position = alien ship position
                self.blastpos.center = self.pos.center
                self.blastposprev.center = self.blastpos.center
                # define for each frame the blast delta X and Y
                dx = int((self.blastpos.centerx - 320) / 50)
                dy = int((self.blastpos.centery - 240) / 50)
                # define which shield must be used to defend
                if dx < 0 and dy < 0:
                    self.defenseshield = 1
                if dx > 0 and dy < 0:
                    self.defenseshield = 2
                if dx > 0 and dy > 0:
                    self.defenseshield = 3
                if dx < 0 and dy > 0:
                    self.defenseshield = 4
                # define vector; opposite signal as blast have to move in the opposite direction
                self.blastvector = [-dx, -dy]

    def moveblast(self, scr):
        # test if it's OK to move blast
        if self.firestate == 1:
            # erase the previous blast position
            scr.area.blit(scr.image, self.blastposprev, self.blastposprev)
            # update new position
            self.blastpos.centerx += self.blastvector[0]
            self.blastpos.centery += self.blastvector[1]
            # draw the new blast position
            scr.area.blit(self.blastimage, self.blastpos)
            # update previous position
            self.blastposprev.center = self.blastpos.center
            # test if blast is inside the space station (32 station radius) or outside margins
            if testinside(self.blastpos.centerx, self.blastpos.centery, 32) \
                    or self.blastpos.bottom < 0 or self.blastpos.top > 480 \
                    or self.blastpos.left > 640 or self.blastpos.right < 0:
                self.firestate = 0


# event loop
def eventloop(scr, fnt, clk, sco, sta, ali):
    # arguments: scr=screen, fnt=font, clk=clock, sco=score, sta=station, ali=alien
    a = 1
    while a == 1:
        # quit gracefully
        for event in pygame.event.get():
            if event.type == pygame.QUIT or pygame.key.get_pressed()[K_q]:
                sys.exit()
        # measure time
        clk.tick(60)
        # write text
        # scr.area.blit(scr.image, (120, 5, 50, 30), (120, 5, 50, 30))
        scr.area.blit(writetext(fnt, 'Shield', (200, 200, 200)), (10, 10))
        # temp shield to be used, to delete further
        scr.area.blit(scr.image, (600, 10, 30, 30))
        scr.area.blit(writetext(fnt, '{}'.format(ali.defenseshield), (200, 200, 200)), (600, 10))
        # draw station
        scr.area.blit(sta.image, sta.pos)
        # draw alien
        scr.area.blit(ali.image, ali.pos)
        # move alien
        ali.move(scr)
        # fire blast
        ali.fire()
        # move blast
        ali.moveblast(scr)
        # control actions
        sta.defend(scr)
        # draw fuel
        sta.burn(scr)
        # refresh display
        pygame.display.update()


# main routine
def main():
    print('\n ::: Input 06 - Deadly Enemies and Aliens :::\n\n       Press [Q] to quit.\n')
    # start Pygame
    pygame.init()
    pygame.mixer.init()
    font1 = pygame.font.Font('./fonts/Chicago Normal.ttf', 16)
    clock = pygame.time.Clock()
    score = 0
    # start the display
    # screen = Setupscreen()
    screen = Setupscreen('saturn.png')
    # space station
    station = Spacestation()
    # alien ship
    alien = Alien()
    # the actions
    # action = Action()
    # start the event loop
    eventloop(screen, font1, clock, score, station, alien)


# execute main
if __name__ == '__main__': 
    main()


