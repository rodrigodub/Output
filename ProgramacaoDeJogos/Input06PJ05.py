#################################################
#                   INPUT 6
# Programacao de Jogos 5
# Deadly Enemies and Aliens
#
# Usage:
# > python3 Input06PJ05.py
#
# v2.115
# 20180129
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
        return False
    else:
        return True


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


# Alien ship
class Alien(object):
    """Class to deal with the alien ship"""
    def __init__(self):
        # alien ship image and position
        self.image = load_image('alienship_64.png')
        self.pos = self.image.get_rect()
        self.pos.center = (random.randint(0, 640), random.randint(0, 480))
        self.posprev = self.pos
        # vector defines the amount of movement in each axis
        self.vector = [0, 0]

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
        if math.sqrt(pow((self.pos.centerx - 320), 2) + pow((self.pos.centery - 240), 2)) < 113:
            self.vector = [-i for i in self.vector]
        # draws alien ship
        scr.area.blit(self.image, self.pos)
        # makes the previous position as the current one
        self.posprev = self.pos


# Controller
class Action(object):
    def __init__(self):
        pass

    def defend(self, scr, sta):
        # params: scr=screen, sta=station
        keys = pygame.key.get_pressed()
        if keys[K_1]:
            scr.area.blit(sta.shield1, sta.shield1pos)
        else:
            scr.area.blit(scr.image, sta.shield1pos, sta.shield1pos)
            scr.area.blit(sta.image, sta.pos)
        if keys[K_2]:
            scr.area.blit(sta.shield2, sta.shield2pos)
        else:
            scr.area.blit(scr.image, sta.shield2pos, sta.shield2pos)
            scr.area.blit(sta.image, sta.pos)
        if keys[K_3]:
            scr.area.blit(sta.shield3, sta.shield3pos)
        else:
            scr.area.blit(scr.image, sta.shield3pos, sta.shield3pos)
            scr.area.blit(sta.image, sta.pos)
        if keys[K_4]:
            scr.area.blit(sta.shield4, sta.shield4pos)
        else:
            scr.area.blit(scr.image, sta.shield4pos, sta.shield4pos)
            scr.area.blit(sta.image, sta.pos)


# event loop
def eventloop(scr, fnt, clk, sco, sta, ali, act):
    # arguments: scr=screen, fnt=font, clk=clock, sco=score, sta=station, ali=alien, act=action
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
        scr.area.blit(writetext(fnt, 'OK: {}'.format(sco), (250, 250, 250)), (10, 10))
        # draw station
        scr.area.blit(sta.image, sta.pos)
        # draw alien
        scr.area.blit(ali.image, ali.pos)
        # move alien
        ali.move(scr)
        # control actions
        act.defend(scr, sta)
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
    action = Action()
    # start the event loop
    eventloop(screen, font1, clock, score, station, alien, action)


# execute main
if __name__ == '__main__': 
    main()


