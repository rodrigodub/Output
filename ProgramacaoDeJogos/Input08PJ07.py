#################################################
#                   INPUT 8
# Programacao de Jogos 7
# Labirinth 2 - Treasure Hunt
# UK : Input 7
# Usage:
# > python3 Input08PJ07.py
#
# v2.136
# 20180204
#################################################
__author__ = 'Rodrigo Nobrega'


# import
import os, sys, pygame
from pygame.locals import *
# import random
# import math


# Global variables
BLACK = (0, 0, 0)
BACKGROUND = (230, 230, 230)
PIXELCOLOR = (255, 255, 255)
BORDER = (255, 128, 128)


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
        self.bgcolour = BACKGROUND
        # the canvas
        self.display = pygame.display.set_mode(self.size)
        self.title = pygame.display.set_caption('Treasure Hunt')
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


# Labirinth
class Labirinth(object):
    def __init__(self):
        self.blocksize = 20
        #self.numbercolumns = 2 * int(0.5 * 1024 / self.blocksize)
        self.numbercolumns = int(1024 / self.blocksize)
        self.numberlines = 2 * int(0.5 * 526 / self.blocksize)

    def drawmargin(self, scr):
        for i in range(0, self.numbercolumns):
            pygame.draw.rect(scr.display, BORDER, (i * self.blocksize, 50, self.blocksize, self.blocksize), 0)
            pygame.draw.rect(scr.display, BORDER, (i * self.blocksize, 556, self.blocksize, self.blocksize), 0)
        for j in range(0, self.numberlines):
            pygame.draw.rect(scr.display, BORDER, (0, j * self.blocksize + 50, self.blocksize, self.blocksize), 0)
            pygame.draw.rect(scr.display, BORDER, (1000, j * self.blocksize + 50, self.blocksize, self.blocksize), 0)



# event loop
def eventloop(scr, fnt, clk, maz):
    # arguments: scr=screen, fnt=font, clk=clock, maz=labirinth
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
        scr.display.blit(writetext(fnt, 'OK', BLACK), (10, 10))
        # draws maze
        maz.drawmargin(scr)
        # refresh display
        pygame.display.flip()


# main routine
def main():
    print('\n ::: Labirinth :::\n\n       Press [Q] to quit.\n')
    # start Pygame
    pygame.init()
    pygame.mixer.init()
    font1 = pygame.font.Font('./fonts/Chicago Normal.ttf', 16)
    clock = pygame.time.Clock()
    # score = 0
    # start the display
    screen = Screen()
    # creates the Labirinth
    maze = Labirinth()
    # start the event loop
    eventloop(screen, font1, clock, maze)


# execute main
if __name__ == '__main__': 
    main()


