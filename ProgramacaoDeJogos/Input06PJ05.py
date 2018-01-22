#################################################
#                   INPUT 6
# Programacao de Jogos 5
# Deadly Enemies and Aliens
#
# Usage:
# > python3 Input06PJ05.py
#
# v2.103
# 20180122
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
        self.pos = self.image.get_rect().move(320-32, 240-32)


# event loop
def eventloop(scr, fnt, sco, sta):
    # arguments: scr=screen, fnt=font, sco=score, sta=station
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
    # start the event loop
    eventloop(screen, font1, score, station)


# execute main
if __name__ == '__main__': 
    main()


