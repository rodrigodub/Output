#################################################
#                   INPUT 6
# Programacao de Jogos 5
# Deadly Enemies and Aliens
#
# Usage:
# > python3 Input06PJ05.py
#
# v2.106
# 20180124
#################################################
__author__ = 'Rodrigo Nobrega'


# import
import os, sys, pygame
from pygame.locals import *
# import random
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


# screen
class Setupscreen(object):
    """Starts a screen and displays background"""
    def __init__(self, image_file=None):
        # physical parameters
        self.size = (640, 480)
        self.bgcolour = [230, 230, 230]
        # the canvas
        self.area = pygame.display.set_mode(self.size)
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
        #self.pos = self.image.get_rect().move(320-32, 240-32)
        self.pos = self.image.get_rect()
        self.pos.center = (320,240)
        # shield images
        self.shield1 = load_image('shield_1.png')
        self.shield2 = load_image('shield_2.png')
        self.shield3 = load_image('shield_3.png')
        self.shield4 = load_image('shield_4.png')
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
            #scr.area.blit(sta.image, Rect(sta.pos.left, sta.pos.top, 32, 32))
        if keys[K_2]:
            scr.area.blit(sta.shield2, sta.shield2pos)
        else:
            scr.area.blit(scr.image, sta.shield2pos, sta.shield2pos)
            scr.area.blit(sta.image, sta.pos)
            #scr.area.blit(sta.image, Rect(sta.pos.midleft, sta.pos.top, 32, 32))
        if keys[K_3]:
            scr.area.blit(sta.shield3, sta.shield3pos)
        else:
            scr.area.blit(scr.image, sta.shield3pos, sta.shield3pos)
            scr.area.blit(sta.image, sta.pos)
            #scr.area.blit(sta.image, Rect(sta.pos.midleft, sta.pos.midtop, 32, 32))
        if keys[K_4]:
            scr.area.blit(sta.shield4, sta.shield4pos)
        else:
            scr.area.blit(scr.image, sta.shield4pos, sta.shield4pos)
            scr.area.blit(sta.image, sta.pos)
            #scr.area.blit(sta.image, Rect(sta.pos.left, sta.pos.midtop, 32, 32))


# event loop
def eventloop(scr, fnt, sco, sta, act):
    # arguments: scr=screen, fnt=font, sco=score, sta=station, act=action
    a = 1
    while a == 1:
        # quit gracefully
        for event in pygame.event.get():
            if event.type == pygame.QUIT or pygame.key.get_pressed()[K_q]:
                sys.exit()
        # write text
        # scr.area.blit(scr.image, (120, 5, 50, 30), (120, 5, 50, 30))
        scr.area.blit(writetext(fnt, 'OK: {}'.format(sco), (250, 250, 250)), (10, 10))
        # draw station
        scr.area.blit(sta.image, sta.pos)
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
    score = 0
    # start the display
    # screen = Setupscreen()
    screen = Setupscreen('saturn.png')
    # space station
    station = Spacestation()
    # the actions
    action = Action()
    # start the event loop
    eventloop(screen, font1, score, station, action)


# execute main
if __name__ == '__main__': 
    main()


