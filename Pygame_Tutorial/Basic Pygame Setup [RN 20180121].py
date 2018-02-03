#################################################
#                   NAME
# Detail 1
# Detail 2
#
# Usage:
# > python3 name.py
#
# v2.125
# 20180203
#################################################
__author__ = 'Rodrigo Nobrega'


# import
import os, sys, pygame
from pygame.locals import *
# import random
# import math


# load image function
def load_image(file):
    path = os.path.join('images', file)
    return pygame.image.load(path).convert_alpha()


# write text
def writetext(font, text, colour):
    # colour: tuple (r, g, b)
    a = font.render(text, 0, colour)
    return a


# screen
class Screen(object):
    """Starts a screen and displays background"""
    def __init__(self, image_file=None):
        # physical parameters
        self.size = (1024, 576)
        self.bgcolour = [230, 230, 230]
        # the canvas
        self.display = pygame.display.set_mode(self.size)
        self.title = pygame.display.set_caption('Pygame app')
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
        self.display.fill(self.bgcolour)
        # blit background image
        if self.image != '':
            self.display.blit(self.image, (0, 0))


# event loop
def eventloop(scr, fnt, clk, sco):
    # arguments: scr=screen, fnt=font, clk=clock, tnk=tank, prt=paratrooper list, sco=score, min=mine
    a = 1
    while a == 1:
        # quit gracefully
        for event in pygame.event.get():
            if event.type == pygame.QUIT or pygame.key.get_pressed()[K_q]:
                sys.exit()
        # measure time
        clk.tick(60)
        # write text
        # scr.display.blit(scr.image, (120, 5, 50, 30), (120, 5, 50, 30))
        scr.display.blit(writetext(fnt, 'OK: {}'.format(sco), (100, 100, 100)), (10, 10))
        # refresh display
        pygame.display.flip()


# main routine
def main():
    print('\n ::: Basic Initial Setup :::\n\n       Press [Q] to quit.\n')
    # start Pygame
    pygame.init()
    pygame.mixer.init()
    font1 = pygame.font.Font('Chicago Normal.ttf', 16)
    clock = pygame.time.Clock()
    score = 0
    # start the display
    screen = Screen()
    #screen = Screen('background green 640x480.png')
    # start the event loop with tank moving right
    eventloop(screen, font1, clock, score)


# execute main
if __name__ == '__main__': 
    main()


